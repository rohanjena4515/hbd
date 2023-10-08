FROM python:3.10.4-slim

LABEL maintainer="Ashwani Kumar Kamal (sneaky-potato) <ashwanikamal.im421@gmail.com>"

WORKDIR /app

COPY requirements.txt requirements.txt

ARG FLASK_ENV="development"
ENV FLASK_ENV="${FLASK_ENV}" \
    PYTHONUNBUFFERED="true"

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]