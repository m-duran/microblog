FROM python:3.7

WORKDIR /app

ENV MAIL_SERVER=localhost MAIL_PORT=8025 FLASK_APP=microblog.py

EXPOSE 5000

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN flask db upgrade

ENTRYPOINT [ "python" ]

CMD [ "-m", "flask", "run", "--host=0.0.0.0" ]
