#!/usr/bin/env bash
# Chrome channel evening meetup
# A simple script to install apache httpd webserver on an ec2 instance

sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable --now  httpd
