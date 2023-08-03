#!/usr/bin/env bash
# A simple script to pull a .jar file from an S3 bucket
# And run the application



S1="s3://java-poc-project"
S2="s3://hi-mom-bucket-java"

F1="$S1/f1.jar"
F2="$S2/f2.jar"

#!/bin/bash

# check if JDK is installed on Debian/Ubuntu/Mint
function check_debian {
    if ! command -v java &>/dev/null; then
        echo "JDK not found. Installing OpenJDK..."
        sudo apt-get update
        sudo apt-get install -y openjdk-11-jdk
    else
        echo "JDK is already installed. Good to go."
    fi
}

# check if JDK is installed on Red Hat-based (CentOS) systems
function check_redhat {
    if ! command -v java &>/dev/null; then
        echo "JDK not found. Installing OpenJDK..."
        sudo dnf install -y java-11-openjdk-devel
    else
        echo "JDK is already installed."
    fi
}

# Function to check if JDK is installed on Arch-based systems
function check_arch {
    if ! command -v java &>/dev/null; then
        echo "JDK not found. Installing OpenJDK..."
        sudo pacman -S --noconfirm jdk11-openjdk
    else
        echo "JDK is already installed. Good to go"
    fi
}

# Detect the Linux distribution and call the appropriate function
# to install jdk
if [ -f "/etc/debian_version" ]; then
    check_debian
elif [ -f "/etc/redhat-release" ]; then
    check_redhat
elif [ -f "/etc/arch-release" ]; then
    check_arch
else
    echo "Unsupported Linux distribution. Please install JDK manually."
    exit 1
fi





