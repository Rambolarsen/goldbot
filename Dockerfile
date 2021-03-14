FROM python:3.8-slim-buster

ENV TZ=Europe/Oslo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /src
WORKDIR /src
ADD . /src/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "src/bot.py" ]