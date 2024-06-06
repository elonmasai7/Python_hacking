import subprocess
import shlex

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

# Example usage
if __name__ == '__main__':
    path = 'path/to/code'  # replace with the actual path
    sanitized_path = shlex.quote(path)
    run_bandit(sanitized_path)
    run_flake8(sanitized_path)
    run_pylint(sanitized_path)
