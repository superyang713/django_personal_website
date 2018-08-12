# start from an official image
FROM python:3.6

RUN mkdir -p /opt/services/personal_website/src
WORKDIR /opt/services/personal_website/src

# copy project code
COPY . /opt/services/personal_website/src

# install our dependencies
RUN pip install -r requirements.txt

# Collect static files
RUN cd app && python manage.py collectstatic

# expose the port 8000
EXPOSE 8000
