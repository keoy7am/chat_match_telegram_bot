FROM python:3.8.0

LABEL MAINTAINER="Elliot Chen <keoy7am@gmail.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD . /var/www/

ENV TZ=Asia/Taipei

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install -r requirements.txt

#RUN addgroup -g $GROUP_ID www
#RUN adduser -D -u $USER_ID -G www www -s /bin/sh

#USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "-k", "gevent", "--bind", "0.0.0.0:5000", "runserver:app", "–preload"]
