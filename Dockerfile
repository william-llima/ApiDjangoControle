FROM python:3.10.6
WORKDIR /app
COPY . ./
run python -m pip install Django
run python -m pip install pymysql
run python -m pip install djangorestframework
run python -m pip install markdown      
run python -m pip install django-filter
run python -m pip install django-cors-headers
run python -m pip install mysqlclient
