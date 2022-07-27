# Define version of node
FROM python
# Create app directory
WORKDIR /server
# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)

RUN apt install -y libpq-dev

RUN pip install "poetry"

COPY * ./

RUN poetry update
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:run()"]