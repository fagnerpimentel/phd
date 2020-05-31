#!/bin/bash

# X-server
apt-get install xvfb 

# https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04
## DOCKER ##
# Step 1: Update Software Repositories
apt-get update
# Step 2: Uninstall Old Versions of Docker
apt-get remove docker docker-engine docker.io
# Step 3: Install Docker
apt-get install docker.io
# Step 4: Start and Automate Docker
systemctl start docker
systemctl enable docker
# Step 5 (Optional): Check Docker Version
docker --version
