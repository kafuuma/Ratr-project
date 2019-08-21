FROM python:3.7

WORKDIR /usr/src/app

RUN apt-get install libpq-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN chmod a+x ./start_server.sh

# CMD [ "python", "manage.py", "run", "--host=0.0.0.0"]
CMD ["./start_server.sh"]
