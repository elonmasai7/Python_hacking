import subprocess
import os
import shlex

def run_bandit(path):
    sanitized_path = shlex.quote(path)
    result = subprocess.run(['/usr/local/bin/bandit', '-r', sanitized_path], capture_output=True, text=True)
    print(result.stdout)

def run_flake8(path):
    sanitized_path = shlex.quote(path)
    result = subprocess.run(['/usr/local/bin/flake8', sanitized_path], capture_output=True, text=True)
    print(result.stdout)

def run_pylint(path):
    sanitized_path = shlex.quote(path)
    result = subprocess.run(['/usr/local/bin/pylint', sanitized_path], capture_output=True, text=True)
    print(result.stdout)

# Example usage
run_bandit('/path/to/your/code')
run_flake8('/path/to/your/code')
run_pylint('/path/to/your/code')
