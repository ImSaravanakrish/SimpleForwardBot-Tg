FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt
RUN pip3 install -U https://github.com/pyrogram/pyrogram/archive/master.zip
COPY . /app

CMD python3 bot.py
