#!/bin/bash

## DOCKER ##
# https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04
# Step 1: Update Software Repositories
sudo apt-get update
# Step 2: Uninstall Old Versions of Docker
sudo apt-get remove docker docker-engine docker.io
# Step 3: Install Docker
sudo apt install docker.io
# Step 4: Start and Automate Docker
sudo systemctl start docker
sudo systemctl enable docker
# Step 5 (Optional): Check Docker Version
docker --version

