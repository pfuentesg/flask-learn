FROM python:3.6.6
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 EXPOSE 5000
 ADD . /code/
 CMD [ "python3" ,"app.py"]