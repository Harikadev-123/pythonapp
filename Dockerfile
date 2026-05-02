FROM python:3
WORKDIR /usr/src/app
copy app.py .
CMD [ "python", "app.py" ]
