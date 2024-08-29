FROM python:3.11

RUN apt-get update && apt-get install -y gcc

# install poetry
RUN pip install poetry

# set working directory
WORKDIR /app

# copy project
COPY . /app

# install dependencies
RUN poetry install

# Windows
# CMD ["poetry", "run", "waitress-serve", "--port", "80", "app:app"]

# Linux
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:80" ,"app:server","--threads=4"]
