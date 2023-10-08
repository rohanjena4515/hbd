# HBD &middot;

>With more than 800 friends on facebook and otherwise, I felt baffled and helpless having lost the opportunity to wish some of the dear ones.

A birthday reminder flask service

## Installing / Getting started

A quick introduction of the minimal setup you need to get the development environment setup

Please use Python  v3.10.4 (you may use [pyenv](https://pypi.org/project/pyenv/) to switch if you're on a different version)

```shell
git clone https://github.com/sneaky-potato/hbd.git
cd hbd
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

- Setup a SQL database (I used a postgres database provided by [Supabase](https://supabase.com/))
- Get [redis](https://redis.io/) service up and running on the host

Do setup an ```.env``` file by taking the reference from ```.env.example```

## API Reference

<!-- [Postman Documentation](https://documenter.getpostman.com/view/19757323/UVyn2z4D) -->

- [GET] /
- [POST] /birthday
- [GET, POST] /birthday/search

### /

Basic API to check if the server is up and running or not

```shell
{
    'data': 'API is working'
}
```

### /birthday

API for adding birthdays

> Request Body (application/json)  

```shell
{
    "name": "John Doe",
    "bda_day": 1,
    "bday_month": 1
}
```

### /birthday/search

API for searching a birthday from the database

> Accepts 3 optional parameters: name, bday_day and bday_month else prints all birthdays

## Running the server

Make sure you've configured everything correctly by setting up an ```.env``` file, reference for the same is [here](https://github.com/sneaky-potato/hbd/blob/main/.env.example/)

- Locally with Docker compose (requires ```redis``` service configured, up and running on the host)

```shell
docker compose up --build    
```

The latest docker image is pushed to dockerhub via ```dockerhub_push.yml``` GitHub action

Pull the latest build image using-

```shell
docker pull sneakyp0tat0/hbd
```

## Todos

- Frontend for interacting with the application
- Authentication setup
- Automatic importing of birthdays from one's facebook credentials
- Better customizable emailing service (currently using SMTP password setup of Gmail)
