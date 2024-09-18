import subprocess

# Docker command
docker_command = [
    'sudo', 'docker', 'run', '-v', 
    '/mnt/c/Users/alee9/pro-gramming/github-repos/EDA_daily-/day-6/Airbnb_Data.csv:/data/Airbnb_Data.csv', 
    'alee97422/dockerdata1:latest', 
    'python', 'app.py', '/data/Airbnb_Data.csv'
]

# Run the Docker command
result = subprocess.run(docker_command, capture_output=True, text=True)

# Print the output
print(result.stdout)
print(result.stderr)
