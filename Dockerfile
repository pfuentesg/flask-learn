FROM python:3.6.6
RUN mkdir /code
WORKDIR /code

 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
RUN useradd -ms /bin/bash uwsgi
USER uwsgi
 EXPOSE 5000
 ADD . /code/
ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:5000", "--module", "app:app", "--processes", "1", "--threads", "8"]

