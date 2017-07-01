FROM ubuntu:17.04
MAINTAINER Hans Fangohr <hans.fangohr@xfel.eu>

# Update OS
RUN apt-get update
RUN apt-get -y upgrade

# Install dependencies
RUN apt-get install -y python3 python3-pip
RUN pip3 install pelican
RUN pip3 install typogrify
WORKDIR /io

RUN useradd pelican
USER pelican
# Expose default Pelican port
EXPOSE 8000

# Run Pelican
#CMD make devserver
