FROM python:3.6-onbuild
ADD . /usr/src/app/
EXPOSE 8089
RUN python setup.py install
