current_user=$(whoami)
install_dir="/home/$current_user/.local/bin"

if [ "$1" = "uninstall" ]; then
    # uninstall
    rm -rf "$install_dir/urbancli"
    rm -f "$install_dir/urban"

    read -p "Do you want to remove the python-urbandict package? (Y/n): " response
    response=${response,,}

    # Check the user's response
    if [[ "$response" == "y" || "$response" == "" ]]; then
        pip uninstall python-urbandict
    elif [[ "$response" == "n" ]]; then
        :
    else
        echo "Invalid response. Please enter Y or n."
    fi
else
    # install
    pip install python-urbandict 

    mkdir -p "$install_dir/urbancli"
    cp -r . "$install_dir/urbancli"
    cp urban "$install_dir"
    chmod +x "$install_dir/urban"
fi
