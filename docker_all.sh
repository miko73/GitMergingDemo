docker image is the class for the container,
it is the matrics how to make container.

Container is running instance fo application, its is setup and ready to work in second.
There are several softwares with docker ready images, like mongoDB, Alpine, redis etc.
============================================================================== 
on youtube
cesky
https://www.youtube.com/watch?v=A1nngnx8WDg



============================================================================== 
english

https://youtu.be/i7ABlHngi1Q and 

manager dockers easely
https://www.youtube.com/watch?v=4I8CRAzPLD4


workpres docker
https://www.youtube.com/watch?v=g7LvDt7XcWY

creating docker image 
all about the Dockerfile
https://gist.github.com/adamveld12/4815792fadf119ef41bd
how to create docker file for images
https://www.slideshare.net/dotCloud/building-images-from-dockerfiles-27105810
============================================================================== 
c-grupy = controlgroups - slouzi k nastaveni limitu procesu / kontejneru

namespaces -
kernel namespace - izolace procesu
mount namespace - izolace file systemu
process namespace - izolace procesu
network namespace - izolace sítového rozhrani
interproces comunication - fronty a locky
user namespace - izolace struktury useru (vnitrne to simuluje roota, ale z pohledu hosta to root neni, je to jen root v containeru)

process name
============================================================================== 


1) crete directory
2) create Dockerfile
    FROM node:latest
    RUN mkdir -p /app/scr
    WORKDIR /app/src
    COPY package.json .
    RUN	npm install
    COPY . .
    EXPOSE 3000
    CMD ["npm","start"]


in commnd line
  to view all images on computer
    docker images
  what conteiners are running
    docker ps
  to build the docker 
    docker build . -t youtubereactapp
  izolace containeru z hlediska bezpecnosti
    slinux

  docker není container, 
  ale rozhraní a nástroj na rizeni kontejneru.


============================================================================== 
https://docs.microsoft.com/cs-cz/windows/wsl/install-win10
============================================================================== 
