# Test-bot

This bot created to add and get users

# how to run

1. `docker_build.sh` to build this project image
2. `docker compose up` to start

# project structure
docker_build.sh, docker-compose.yml and Dockerfile are docker utility files

poetry.lock and pyproject.toml stands for poetry package manager (same as npm actually but for python)

evolve_db.sh is an example of migration for database
evolve.py is the source code required for migration (it will do everything automagically)

wsgi.py is the server entrypoint
server.py is the server body (a bit complex but I copy-pasted it, please ignore this file)
server_handler.py is my file with business-logic

storage.py is file with DB model

# how DB model works
in storage.py you decliring your table as a structure, like Users table, and after that you can easily iterate it, put or get entries
look for declaration in storage.py:14
iterating table is in server_handler.py:7
