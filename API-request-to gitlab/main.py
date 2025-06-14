import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
print(response.json())
projects = response.json()

for project in projects:
    print(f"Project Name: {project['name']}\nProject URL: {project['web_url']}\n")

