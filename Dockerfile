FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /my_dinner_api
WORKDIR /my_dinner_api
ADD requirements /my_dinner_api/
RUN pip install -r requirements
ADD . /my_dinner_api/
