current_user=$(whoami)
install_dir="/home/$current_user/.local/bin"

if [ "$1" = "uninstall" ]; then
    # uninstall
    rm -rf "$install_dir/urbancli"
    rm -f "$install_dir/urban"
else
    # install
    mkdir -p "$install_dir/urbancli"
    cp -r . "$install_dir/urbancli"
    cp urban "$install_dir"
    chmod +x "$install_dir/urban"
fi