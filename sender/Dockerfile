FROM python:3.9
RUN apt-get update -y
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8082
CMD ["python3","sender.py"]