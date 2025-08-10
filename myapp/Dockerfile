FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /django-app
RUN pip install --upgrade pip
COPY requirements.txt /django-app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /django-app
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "192.168.2.1:8000"]
