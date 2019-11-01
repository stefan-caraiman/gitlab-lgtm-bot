FROM python:3.8
ADD . /usr/src/app/
EXPOSE 8089
RUN python setup.py install
