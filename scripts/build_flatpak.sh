cd ../
flatpak-builder build-dir flatpak.yml --force-clean
flatpak build-export dev-repo build-dir
flatpak build-bundle dev-repo RcloneNavigator.flatpak org.mazur.RcloneNavigator
flatpak uninstall -y org.mazur.RcloneNavigator
flatpak install -y --bundle --user RcloneNavigator.flatpak
flatpak run org.mazur.RcloneNavigator
