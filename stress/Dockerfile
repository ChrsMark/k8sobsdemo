FROM ubuntu

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    stress

CMD [ "stress", "--cpu", "3" ]
