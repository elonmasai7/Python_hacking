import subprocess
import os
import shlex

def run_bandit(path):
    print(f"Running Bandit on {path}")
    sanitized_path = shlex.quote(path)
    result = subprocess.run(['/usr/local/bin/bandit', '-r', sanitized_path], capture_output=True, text=True)
    print(result.stdout)

def run_flake8(path):
    print(f"Running Flake8 on {path}")
    sanitized_path = shlex.quote(path)
    result = subprocess.run(['/usr/local/bin/flake8', sanitized_path], capture_output=True, text=True)
    print(result.stdout)

def run_pylint(path):
    print(f"Running Pylint on {path}")
    sanitized_path = shlex.quote(path)
    result = subprocess.run(['/usr/local/bin/pylint', sanitized_path], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    path = "your_path_here"  # Replace with the actual path
    run_bandit(path)
    run_flake8(path)
    run_pylint(path)
