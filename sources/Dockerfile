FROM ubuntu:17.04
MAINTAINER Hans Fangohr <hans.fangohr@xfel.eu>

# Update OS
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install git

# Install dependencies
RUN apt-get install -y python3 python3-pip
RUN pip3 install pelican
RUN pip3 install typogrify



# install theme
RUN mkdir -p /home/pelican
WORKDIR /home/pelican

RUN git clone https://github.com/duilio/pelican-octopress-theme.git
RUN pelican-themes --install pelican-octopress-theme --verbose

WORKDIR /io

RUN useradd pelican
RUN chown -R pelican /home/pelican
USER pelican


# Expose default Pelican port
EXPOSE 8000

# Run Pelican
CMD make devserver
