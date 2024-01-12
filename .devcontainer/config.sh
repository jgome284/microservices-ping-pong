#!/bin/bash

# create global config file
touch /root/.gitconfig

echo # add white space for formatting

# create git config file not added to debian distributions by default
echo "Configuring Git..."
echo "-----------------------------------------"

# config username and print for confirmation
echo "User: $(grep User ../.devcontainer/credentials.txt | cut -d : -f 2)"
grep User ../.devcontainer/credentials.txt | cut -d : -f 2 | git config --global user.name

# config email and print for confirmation
echo "Email: $(grep Email ../.devcontainer/credentials.txt| cut -d : -f 2)" 
grep Email ../.devcontainer/credentials.txt | cut -d : -f 2 | git config --global user.email

echo # add white space for formatting

echo "Displaying OS Info..."
echo "-----------------------------------------"
cat /etc/os-release

echo # add white space for formatting