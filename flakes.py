import subprocess
import os
import shlex

def run_bandit(path):
    sanitized_path = shlex.quote(path)
    command = ['/usr/local/bin/bandit', '-r', sanitized_path]
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    print(result.stdout)

def run_flake8(path):
    sanitized_path = shlex.quote(path)
    command = ['/usr/local/bin/flake8', sanitized_path]
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    print(result.stdout)

def run_pylint(path):
    sanitized_path = shlex.quote(path)
    command = ['/usr/local/bin/pylint', sanitized_path]
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    print(result.stdout)
