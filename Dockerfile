FROM python:3.7-alpine

RUN adduser -D microblog

WORKDIR /home/microblog

ENV MAIL_SERVER=localhost MAIL_PORT=8025 FLASK_APP=microblog.py

EXPOSE 5000

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

RUN chown -R microblog:microblog ./

USER microblog

ENTRYPOINT [ "./boot.sh" ]
