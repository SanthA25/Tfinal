FROM gitpod/workspace-base:latest 
# branch-se-extract-base
RUN sudo apt-get update
RUN sudo apt-get install -y python3-venv python3-pip
USER gitpod