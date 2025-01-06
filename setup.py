import os
import subprocess

def install_requirements():
    """Install requirements from requirements.txt"""
    subprocess.check_call(["pip", "install", "--upgrade", "pip"])
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    print("Installing requirements...")
    install_requirements()
    print("Setup complete!")
