current_user=$(whoami)
install_dir="/home/$current_user/.local/bin"

if [ "$1" = "uninstall" ]; then
    # uninstall
    echo "Uninstalling urbancli..."

    echo "Removing $install_dir/urbancli"
    rm -rf "$install_dir/urbancli"
    echo "Removing $install_dir/urban"
    rm "$install_dir/urban"

    read -p "Do you want to remove the python-urbandict package? (Y/n): " response
    response=${response,,}

    # Check the user's response
    if [[ "$response" == "y" || "$response" == "" ]]; then
        echo "Uninstalling python-urbandict package"
        pip uninstall python-urbandict
    elif [[ "$response" == "n" ]]; then
        :
    else
        echo "Invalid response. Please enter Y or n."
    fi

    echo "urbancli is now removed from your system!"
else
    # install
    echo "Installing urbancli..."

    echo "Installing python-urbandict from PyPI"
    pip install python-urbandict 

    echo "Creating $installdir/urbancli directory"
    mkdir -p "$install_dir/urbancli"
    echo "Copying repo to $installdir/urbancli"
    cp -r . "$install_dir/urbancli"
    echo "Copying urban script to $install_dir"
    cp urban "$install_dir"
    echo "Giving executable permissions to urban script"
    chmod +x "$install_dir/urban"

    echo "urbancli is now installed on your system!"
    echo "For more information run urban --help"
fi
