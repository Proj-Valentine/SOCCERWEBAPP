import paramiko
from pathlib import Path
import glob
import os

# SSH connection details
hostname = 'ec2-user@3.98.145.209'
username = 'LAPTOP-CFAV6L5M\vkamp'
private_key_path = '/path/to/your/private_key.pem'

# Git repository details
repo_url = 'https://github.com/your_username/your_repo.git'
repo_branch = 'main'
file_path_in_repo = 'path/to/file'

# Remote file path
remote_file_path = '/path/to/remote/file'

# Clone or pull the repository on the EC2 instance
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, username=username, key_filename=private_key_path)

# Check if the repository already exists on the instance
git_repo_dir = '/tmp/repo'
_, stdout, _ = ssh_client.exec_command(f'[ -d "{git_repo_dir}" ] && echo 1 || echo 0')
repo_exists = stdout.read().decode().strip() == '1'

# Clone the repository if it doesn't exist
if not repo_exists:
    git_clone_cmd = f'git clone -b {repo_branch} {repo_url} {git_repo_dir}'
    _, stdout, _ = ssh_client.exec_command(git_clone_cmd)
    stdout.channel.recv_exit_status()

# Pull the latest changes if the repository already exists
git_pull_cmd = f'cd {git_repo_dir} && git pull origin {repo_branch}'
_, stdout, _ = ssh_client.exec_command(git_pull_cmd)
stdout.channel.recv_exit_status()

# Close the SSH connection
ssh_client.close()

# Create an SFTP client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, username=username, key_filename=private_key_path)
sftp_client = ssh_client.open_sftp()

# Upload the updated file to the remote server
local_file_path = f'{git_repo_dir}/{file_path_in_repo}'
sftp_client.put(local_file_path, remote_file_path)

# Close the SFTP client and SSH connection
sftp_client.close()
ssh_client.close()
