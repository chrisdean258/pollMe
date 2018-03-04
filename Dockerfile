FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3 python3-pymysql
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8
RUN export FLASK_APP=app.py

ENTRYPOINT ["sh"]
CMD ["run_app.sh"]
