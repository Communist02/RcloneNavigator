import asyncio
import os
import shutil
import subprocess
import json
from pathlib import Path


class CheckRclone:
    def __init__(self, rclone):
        self.rclone = rclone

    def __call__(self, rclone):
        if rclone:
            return rclone
        if not rclone:
            pyrclonec = f'{Path.home()}/.pyrclonec'
            if Path(pyrclonec).exists():
                with open(pyrclonec) as f:
                    rclone = f.read().rstrip()
            else:
                print(
                    'Could not find rclone in your PATH. Enter it manually '
                    'and the program will remember it.')
                rclone = input('Path to rclone binary: ')
                if not Path(rclone).exists():
                    print('The rclone path you entered does not exist.')
                    raise FileNotFoundError
                else:
                    with open(pyrclonec, 'w') as f:
                        f.write(rclone)
            return rclone


class Rclone(CheckRclone):
    debug = True

    def __init__(self, debug: bool = True):
        self.debug = debug
        self.rclone = shutil.which('rclone')

    async def async_process(self, subcommand, arg1='', arg2='', arg3='', arg4='', *args):
        _args = ' '.join(args)
        command = f'{self.rclone} {subcommand} {arg1} {arg2} {arg3} {arg4} {_args}'

        if self.debug:
            print(f'Executing: {command}')

        process = subprocess.Popen(command, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        loop = asyncio.get_running_loop()
        OUT, ERR = await loop.run_in_executor(None, process.communicate)
        OUT = OUT.decode()

        if ERR:
            print(ERR.decode())
            if subcommand == 'purge' or subcommand == 'deletefile' or subcommand == 'mkdir':
                return ERR.decode()

        if subcommand == 'size':
            total_objects = int(OUT.split('Total objects: ')[
                                1].split(' (')[1].split(')')[0])
            total_size = int(OUT.split('Total size: ')[1].split(
                ' (')[1].split(')')[0].split(' Byte')[0])
            return {'total_objects': total_objects, 'total_size': total_size}
        elif subcommand == 'lsjson' or subcommand == 'config' and arg1 == 'dump' or subcommand == 'about':
            try:
                return json.loads(OUT)
            except json.decoder.JSONDecodeError:
                return {}
        else:
            return OUT

    def sync_process(self, subcommand, arg1='', arg2='', arg3='', arg4='', communicate=True, *args):
        if subcommand in ['copy', 'copyto']:
            P = '-P'
        else:
            P = ''

        if subcommand == 'mount' and os.getenv('container'):
            rclone = 'flatpak-spawn --host /tmp/rclone'
            if not os.path.exists('/tmp/rclone'):
                shutil.copyfile('/app/bin/rclone', '/tmp/rclone')
                os.system('flatpak-spawn --host chmod +x /tmp/rclone')
        else:
            rclone = self.rclone

        _args = ' '.join(args)
        command = f'{rclone} {subcommand} {arg1} {arg2} {arg3} {arg4} {P} {_args}'

        if self.debug:
            print(f'Executing: {command}')

        if not communicate and os.name == 'nt':
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        else:
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if communicate:
            OUT, ERR = process.communicate()
            OUT = OUT.decode()

            if ERR:
                print(ERR.decode())

            if subcommand == 'size':
                total_objects = int(OUT.split('Total objects: ')[
                                    1].split(' (')[1].split(')')[0])
                total_size = int(OUT.split('Total size: ')[1].split(
                    ' (')[1].split(')')[0].split(' Byte')[0])
                return {'total_objects': total_objects, 'total_size': total_size}
            elif subcommand == 'lsjson' or subcommand == 'config' and arg1 == 'dump' or subcommand == 'about' or subcommand == 'config providers':
                return json.loads(OUT)
            elif subcommand == 'config' and 'file' in command:
                return OUT.strip().split('\n')[-1]
            else:
                return OUT
        else:
            return process

    async def mkdir(self, folder_path: str):
        return await self.async_process('mkdir', f'"{folder_path}"')

    def copy(self, source_path: str, destination_path: str):
        return self.sync_process('copy', f'"{source_path}"', f'"{destination_path}"', '--create-empty-src-dirs', communicate=False)

    def lsjson(self, path: str, max_depth: int = -1):
        return self.sync_process('lsjson', f'"{path}"', f'--max-depth {max_depth}', communicate=False)

    def search(self, path: str, max_depth: int = -1):
        return self.sync_process('lsjson', f'"{path}"', f'--max-depth {max_depth}', communicate=False)

    def listremotes(self, long=False) -> str | dict[str]:
        if long:
            remotes = self.sync_process('listremotes', '--long')
            if remotes != '':
                remotes = remotes[:-1]
                remotes = remotes.split('\n')
                result = []
                for remote in remotes:
                    result.append({'name': remote.split(
                        ':')[0], 'type': remote.split(':')[-1].strip()})
                return result
            else:
                return []
        else:
            return self.sync_process('listremotes')

    def config(self, command: str, arg1: str = '', arg2: str = '', arg3: str = ''):
        return self.sync_process('config', command, arg1, arg2, arg3)

    def mount(self, remote: str, mount_point: str = '', arg: str = ''):
        return self.sync_process('mount', f'"{remote}"', f'"{mount_point}"', arg, communicate=False)

    def providers(self):
        return self.sync_process('config providers')

    def create_remote(self, remote_name, remote_type, args='', **kwargs):
        for key, value in kwargs.items():
            match value:
                case str():
                    args += f' {key}="{value}"'
                case int():
                    args += f' {key}={value}'
                case bool():
                    args += f' {key}={str(value).lower()}'
        return self.sync_process(f'config create "{remote_name}" {remote_type} {args}')

    def serve(self, protocol: str, path: str, username: str = '', password: str = '', address: str = '', read_only: bool = False, args: str = ''):
        if read_only:
            args += ' --read-only'
        if address:
            args += f' --addr {address}'
        if protocol != 's3':
            if username:
                args += f' --user {username}'
            if password:
                args += f' --pass {password}'
        else:
            if username and password:
                args += f' --auth-key {username},{password}'
        return self.sync_process('serve', protocol, f'"{path}"', args, communicate=False)

    async def execute(self, command):
        return await self.async_process(subcommand=command, _execute=True)

    async def deletefile(self, path: str):
        return await self.async_process('deletefile', f'"{path}"')

    async def purge(self, path: str):
        return await self.async_process('purge', f'"{path}"')

    async def moveto(self, source_path: str, destination_path: str):
        return await self.async_process('moveto', f'"{source_path}"', f'"{destination_path}"')

    def about(self, remote_name: str):
        return self.sync_process('about', f'"{remote_name}"', '--json', communicate=False)

    async def is_dir(self, path: str):
        p = subprocess.Popen(f'{self.rclone} deletefile "{path}" --dry-run',
                             shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        loop = asyncio.get_running_loop()
        OUT, ERROR = await loop.run_in_executor(None, p.communicate)
        return 'ERROR :' in ERROR.decode()

    def version(self):
        return self.sync_process('version')

    def __getattr__(self, attr):
        def wrapper(*args, **kwargs):
            return self.sync_process(attr, *args, **kwargs)
        return wrapper
