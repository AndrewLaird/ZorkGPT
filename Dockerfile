#FROM ubuntu:latest
#RUN apt-get -y update
#RUN apt-get -y install git

FROM ubuntu:latest

RUN apt-get update -y 
RUN apt-get install -y frotz wget

RUN wget http://ifarchive.org/if-archive/games/zcode/zork1.z5

CMD ["frotz", "zork1.z5"]


