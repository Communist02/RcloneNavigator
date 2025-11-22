cd ../
flatpak-builder build-dir flatpak.yml --force-clean
flatpak build-export dev-repo build-dir
flatpak build-bundle dev-repo rclone_navigator_x86_64.flatpak io.github.communist02.RcloneNavigator
flatpak uninstall -y io.github.communist02.RcloneNavigator
flatpak install -y --bundle --user rclone_navigator_x86_64.flatpak
flatpak run io.github.communist02.RcloneNavigator
