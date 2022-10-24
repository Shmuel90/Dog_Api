# Python Base Image
FROM python:3.10.6

# Link to backend
ENV APP_ROOT /var/www/backend
RUN mkdir /var/www;
RUN mkdir /var/www/backend
WORKDIR ${APP_ROOT}

# Python Dependencies
RUN pip3 install Django
RUN pip3 install djangorestframework
RUN pip3 install markdown
RUN pip3 install django-filter
RUN pip3 install psycopg2-binary
RUN pip3 install django-templated-email
RUN pip3 install gunicorn
RUN pip3 install requests
RUN pip3 install djangorestframework-jsonapi
