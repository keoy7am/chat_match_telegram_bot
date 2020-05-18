FROM python:3.8.0

LABEL MAINTAINER="Elliot Chen <keoy7am@gmail.com>"

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /volume/app

COPY start.sh .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["sh","start.sh"]
