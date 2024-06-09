import subprocess
import shlex

# Example of sanitizing inputs before using in subprocess.run
def run_bandit(sanitized_path):
    command = ['/usr/local/bin/bandit', '-r', sanitized_path]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print(result.stdout)

def run_flake8(sanitized_path):
    command = ['/usr/local/bin/flake8', sanitized_path]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print(result.stdout)

def run_pylint(sanitized_path):
    command = ['/usr/local/bin/pylint', sanitized_path]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print(result.stdout)
