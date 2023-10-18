# Use an existing image as a base
FROM ubuntu:20.04

# Run commands to install software
RUN apt-get update && apt-get install -y nginx

# Specify the command to run when the container starts
CMD ["nginx", "-g", "daemon off;"]
