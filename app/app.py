import os
os.system("./gh auth login")
os.system("mkdir data")

org = input("Enter the name of the organization: ")
os.system(f"./gh repo list {org} -L 100 > repos.txt")

with open("repos.txt", "r") as f:
    for line in f:
        repo = line.split()[0]
        print(f"Cloning {repo}...")
        os.system(f"./gh repo clone {repo} data/{repo}")

with open("repos.txt", "r") as f:
    for line in f:
        repo = line.split()[0]
        print(f"Scanning {repo}...")
        os.system(f"cd data/{repo} && ../../../gitleaks detect --verbose --no-banner --no-color --log-level warn | grep Finding")

while True:
    pass