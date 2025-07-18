cd ../
flatpak-builder build-dir flatpak.yml --force-clean
flatpak build-export dev-repo build-dir
flatpak build-bundle dev-repo RcloneNavigator.flatpak com.mazur.RcloneNavigator
flatpak uninstall -y com.mazur.RcloneNavigator
flatpak install -y --bundle --user RcloneNavigator.flatpak
flatpak run com.mazur.RcloneNavigator
