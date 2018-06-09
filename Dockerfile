FROM python:3.6-alpine

ENV FLASK_APP quotes.py
ENV FLASK_CONFIG docker

RUN adduser -D quotes
USER quotes

WORKDIR /home/quotes

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY quotes.py config.py boot.sh ./

# runtime configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
