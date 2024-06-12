import subprocess
import os

def run_bandit(path):
    print(f"Running Bandit on {path}")
    result = subprocess.run(['/usr/local/bin/bandit', '-r', path], capture_output=True, text=True)
    print(result.stdout)

def run_flake8(path):
    print(f"Running Flake8 on {path}")
    result = subprocess.run(['/usr/local/bin/flake8', path], capture_output=True, text=True)
    print(result.stdout)

def run_pylint(path):
    print(f"Running Pylint on {path}")
    result = subprocess.run(['/usr/local/bin/pylint', path], capture_output=True, text=True)
    print(result.stdout)
