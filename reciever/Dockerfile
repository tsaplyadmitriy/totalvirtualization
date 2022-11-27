# syntax=docker/dockerfile:1
FROM python:3.9
RUN apt-get update -y
COPY . .
RUN pip3 install --no-cache-dir -r  requirements.txt
EXPOSE 8083
CMD ["python3","reciever.py"]