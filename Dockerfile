FROM python:3.8-slim-buster
WORKDIR /app
COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt
COPY . .
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
