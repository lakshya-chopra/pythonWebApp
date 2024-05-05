
FROM python:3

WORKDIR myApp/app
RUN apt update
RUN pip3 install flask

COPY app .

EXPOSE 80

CMD ["python", "app.py", "runserver", "0.0.0.0:8008"]
