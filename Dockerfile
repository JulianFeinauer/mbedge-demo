# Documentation:
# Starts the Django Application
# With the COMD Arg:
# "celery-beat" - it starts the celery beat
# "celery-worker" - it starts the celery worker
FROM python:3.8-buster

COPY . /app/
WORKDIR /app
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python", "main.py"]
