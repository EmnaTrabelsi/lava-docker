FROM bitnami/minideb:stretch
RUN apt-get update || apt-get update
RUN apt-get -qq install git
RUN mkdir /website
RUN cd /website && git clone https://github.com/ivoire/Artifactorial
RUN apt-get -qq install python python-pip
RUN cd /website && pip install -r Artifactorial/requirements.txt && pip install django-extensions
RUN cd /website && django-admin startproject myproject
RUN cd /website && mv Artifactorial/*  myproject
RUN mkdir /website/myproject/local_directory
COPY configs/settings.py/ /website/myproject/myproject
COPY configs/urls.py/ /website/myproject/myproject
RUN mkdir -p /website/myproject/scripts
RUN touch /website/myproject/scripts/__init__.py
COPY configs/create_admin.py/ /website/myproject/scripts
EXPOSE 8000
CMD python /website/myproject/manage.py migrate && python /website/myproject/manage.py runscript create_admin && python /website/myproject/manage.py runserver 0.0.0.0:8000

