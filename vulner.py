import subprocess
import shlex

def run_bandit(path):
    sanitized_path = shlex.quote(path)
    command = ['/usr/local/bin/bandit', '-r', sanitized_path]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print(result.stdout)

def run_flake8(path):
    sanitized_path = shlex.quote(path)
    command = ['/usr/local/bin/flake8', sanitized_path]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print(result.stdout)

def run_pylint(path):
    sanitized_path = shlex.quote(path)
    command = ['/usr/local/bin/pylint', sanitized_path]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print(result.stdout)

# Example usage
run_bandit('/path/to/your/code')
run_flake8('/path/to/your/code')
run_pylint('/path/to/your/code')
