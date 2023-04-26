import subprocess

# clone the repo
subprocess.run("git clone https://github.com/sachith-d/AI-Image-Generator.git".split())

# # navigate to the directory
subprocess.run("cd AI-Image-Generator".split())

# install the requirements
subprocess.run("python3 -m pip install -r requirements.txt".split())