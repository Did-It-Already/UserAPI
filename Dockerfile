FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


RUN pip install "python-dotenv[cli]"
EXPOSE 8001
CMD ["dotenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8001"]