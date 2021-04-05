FROM python:3.8-buster
WORKDIR /myapp
COPY . /myapp
RUN apt-get update
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]

