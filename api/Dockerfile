FROM docker.io/centos

RUN yum -y install epel-release git
RUN yum -y install nodejs
RUN yum -y install npm
RUN git clone https://github.com/codecowboydotio/swapi-json-server
WORKDIR /swapi-json-server
RUN npm install
EXPOSE 3000
user root
CMD ["/usr/bin/npm", "start"]
