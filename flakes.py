import subprocess
import os

def run_bandit(path):
    print(f"Running Bandit on {path}")
    result = subprocess.run(['bandit', '-r', path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Bandit found issues.")
    else:
        print("No issues found by Bandit.")

def run_flake8(path):
    print(f"Running Flake8 on {path}")
    result = subprocess.run(['flake8', path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Flake8 found issues.")
    else:
        print("No issues found by Flake8.")

def run_pylint(path):
    print(f"Running Pylint on {path}")
    result = subprocess.run(['pylint', path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Pylint found issues.")
    else:
        print("No issues found by Pylint.")

def run_sonarqube(path):
    # Placeholder for SonarQube analysis
    # SonarQube setup and analysis typically require a server and scanner CLI configuration
    print("Running SonarQube analysis...")
    # Example: 
    # result = subprocess.run(['sonar-scanner', '-Dsonar.projectKey=myproject', '-Dsonar.sources=' + path], capture_output=True, text=True)
    # print(result.stdout)
    print("SonarQube analysis would be here (requires additional setup).")

def main():
    # Set your codebase path
    codebase_path = os.path.abspath('.')  # Use current directory for example

    print(f"Checking codebase at {codebase_path}")

    run_bandit(codebase_path)
    run_flake8(codebase_path)
    run_pylint(codebase_path)
    run_sonarqube(codebase_path)

if __name__ == "__main__":
    main()
