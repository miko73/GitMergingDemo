docker run -d -p 80:80 docker/getting-started
https://www.youtube.com/watch?v=i7ABlHngi1Q


https://www.cloudsvet.cz/?series=docker



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

/*========================================================================*/
miko docker run

==============================================================================
miko docker tunneling
https://www.ssh.com/academy/ssh/tunneling



==============================================================================
minecraft server v dockeru

stahne image pokud ho nenajde na locale
docker run -d -it -e EULA=TRUE -e 'JVM_OPTS=-Xmx1024M -Xms1024M' -m 2g -p 25565:25565 --name mc itzg/minecraft-server

Pro připojení se do dockeru lze použít příkaz níže. DOCKER_ID_OR_NAME nahraďte jménem dockeru, v našem případě "mc".

docker exec -it DOCKER_ID_OR_NAME bash
takze

PS C:\Users\micha> docker exec -it mc bash
bash-4.4#

docker start DOCKER_ID`
docker stop DOCKER_ID`
docker restart DOCKER_ID
docker ps                   # vypsání běžících procesů
docker ps -a                # vypsání všech procesů
docker images               # vypsání všech stažených kontejnerů


/*========================================================================*/
docker file start with

name is Dockerfile
FROM
FROM ubuntu, FROM debian
FROM scratch (empty image)
MAINTAINER reghav pal <miko73@seznam.cz>
RUN apt-get update
CMD ["echo", "Hello world from my first docker image :=)"]

when its saved use docker build to build image

docker build c:\user\micha\Dockerfile
or if I am switched in proper directory
docker build .
or file with tag
docker build -t myimage1:1.0 .

/*========================================================================*/


/*========================================================================*/
C:\projects\docker\app_Hello>docker build -t app_hello:1.0 .
[+] Building 31.2s (7/7) FINISHED
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 177B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  0.2s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/debian:latest                                                  12.5s
 => [auth] library/debian:pull token for registry-1.docker.io                                                      0.0s
 => [1/2] FROM docker.io/library/debian@sha256:b16f66714660c4b3ea14d273ad8c35079b81b35d65d1e206072d226c7ff78299   11.6s
 => => resolve docker.io/library/debian@sha256:b16f66714660c4b3ea14d273ad8c35079b81b35d65d1e206072d226c7ff78299    0.0s
 => => sha256:b16f66714660c4b3ea14d273ad8c35079b81b35d65d1e206072d226c7ff78299 1.85kB / 1.85kB                     0.0s
 => => sha256:a5edb9fa5b2a8d6665ed911466827734795ef10d2b3985a46b7e9c7f0161a6b3 529B / 529B                         0.0s
 => => sha256:e7d08cddf791fe3245267654331eb21b805458b3412d368018009355855044a3 1.46kB / 1.46kB                     0.0s
 => => sha256:b9a857cbf04d2c0d2f0f6b73e894b20a977a6d3b6edd9e27d080e03142954950 50.40MB / 50.40MB                   6.1s
 => => extracting sha256:b9a857cbf04d2c0d2f0f6b73e894b20a977a6d3b6edd9e27d080e03142954950                          4.5s
 => [2/2] RUN apt-get update                                                                                       6.1s
 => exporting to image                                                                                             0.5s
 => => exporting layers                                                                                            0.4s
 => => writing image sha256:4e5377c35090fa16bfaab254bef07cc74f0b9496b5658615613e545a9096fbd0                       0.0s
 => => naming to docker.io/library/app_hello:1.0                                                                   0.0s

/*========================================================================*/
running image

C:\projects\docker\app_Hello>docker run sha256:4e5377c35090fa16bfaab254bef07cc74f0b9496b5658615613e545a9096fbd0
Hello world from my first docker image :=)

C:\projects\docker\app_Hello>

all about docker file

https://github.com/wsargent/docker-cheat-sheet

/*========================================================================*/

C:\projects\docker\volume_mount>
docker run --rm -v C:\projects\docker\volume_mount:/myvol ubuntu /bin/bash -c "ls -lha > /myvol/myvile.txt"

C:\projects\docker\volume_mount>dir
 Volume in drive C has no label.
 Volume Serial Number is 0AEE-4B92

 Directory of C:\projects\docker\volume_mount

02/03/2021  09:49 AM    <DIR>          .
02/03/2021  09:49 AM    <DIR>          ..
02/03/2021  09:49 AM             1,279 myvile.txt
               1 File(s)          1,279 bytes
               2 Dir(s)  165,890,498,560 bytes free

C:\projects\docker\volume_mount>cat myvile.txt
total 56K
drwxr-xr-x   1 root root 4.0K Feb  3 08:49 .
drwxr-xr-x   1 root root 4.0K Feb  3 08:49 ..
-rwxr-xr-x   1 root root    0 Feb  3 08:49 .dockerenv
lrwxrwxrwx   1 root root    7 Oct  8 01:31 bin -> usr/bin
drwxr-xr-x   2 root root 4.0K Apr 15  2020 boot
drwxr-xr-x   5 root root  340 Feb  3 08:49 dev
drwxr-xr-x   1 root root 4.0K Feb  3 08:49 etc
drwxr-xr-x   2 root root 4.0K Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Oct  8 01:31 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Oct  8 01:31 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Oct  8 01:31 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Oct  8 01:31 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4.0K Oct  8 01:31 media
drwxr-xr-x   2 root root 4.0K Oct  8 01:31 mnt
drwxrwxrwx   1 root root  512 Feb  3 08:49 myvol
drwxr-xr-x   2 root root 4.0K Oct  8 01:31 opt
dr-xr-xr-x 172 root root    0 Feb  3 08:49 proc
drwx------   2 root root 4.0K Oct  8 01:34 root
drwxr-xr-x   1 root root 4.0K Oct 23 17:32 run
lrwxrwxrwx   1 root root    8 Oct  8 01:31 sbin -> usr/sbin
drwxr-xr-x   2 root root 4.0K Oct  8 01:31 srv
dr-xr-xr-x  11 root root    0 Feb  3 08:49 sys
drwxrwxrwt   2 root root 4.0K Oct  8 01:34 tmp
drwxr-xr-x   1 root root 4.0K Oct  8 01:31 usr
drwxr-xr-x   1 root root 4.0K Oct  8 01:34 var


/*========================================================================*/
miko powershell
https://docs.microsoft.com/cs-cz/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.1&viewFallbackFrom=powershell-6

/*========================================================================*/


docker run --rm -v C:\projects\docker\volume_mount:/myvol klutchell/rar a /myvol/myrar.rar /myvol/myfile.txt
ale klidne
docker run --rm -v C:\projects\docker\volume_mount:/coko klutchell/rar a /coko/myrar.rar /coko/myfile.txt

-w tag přepne na mojí instanci do adresáře, nezačíní v rootu a mohu si pak dovolit prikazy bez cesty

docker run --rm -v C:\projects\docker\volume_mount:/coko -w /coko klutchell/rar a myrar.rar myfile.txt

/*========================================================================*/
miko docker tut
miko tut
https://www.youtube.com/c/TomsCourses/videos





Get the command-by-command run-through:
https://medium.com/@tomw1808/docker-r...​

Find the full course here:
https://www.udemy.com/course/docker-a...​

More information here:
https://vomtom.at/docker-compose-hand...​


/*========================================================================*/
in https://hub.docker.com/


FROM alpine
RUN apk add --no-cache make
RUN wget http://www.rarlab.com/rar/rarlinux-5.4.0.tar.gz && \
  tar -xzvf rarlinux-5.4.0.tar.gz && \
  cd rar && \
  make && \
  mv rar_static /usr/local/bin/rar
ENTRYPOINT ["rar"]

docker run --rm -v C:\projects\docker\volume_mount:/coko -w /coko klutchell/rar a myrar.rar myfile.txt

/*========================================================================*/
running docker containers
docker ps
history of started docker containes
docker ps -a

PS C:\projects\docker\volume_mount> docker ps -a
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS                      PORTS                                                                                                      NAMES
436c8d423c1a   klutchell/rar                         "rar cat Dockerfile.…"   17 minutes ago   Exited (7) 17 minutes ago                                                                                                              peaceful_leavitt
4e790a2a869a   ubuntu                                "/bin/bash"              37 minutes ago   Exited (0) 17 minutes ago                                                                                                              nostalgic_heyrovsky
06e95ec9b743   4e5377c35090                          "echo 'Hello world f…"   2 hours ago      Exited (0) 2 hours ago                                                                                                                 amazing_sammet
765837f71aab   4e5377c35090                          "echo 'Hello world f…"   18 hours ago     Exited (0) 18 hours ago                                                                                                                determined_williamson
5d18b6875dc0   ubuntu:latest                         "/bin/bash"              20 hours ago     Exited (0) 20 hours ago                                                                                                                keen_liskov
78c459e8ce0b   gcr.io/k8s-minikube/kicbase:v0.0.14   "/usr/local/bin/entr…"   20 hours ago     Exited (32) 20 hours ago                                                                                                               silly_chaum
a1ec0831b82f   gcr.io/k8s-minikube/kicbase:v0.0.14   "/usr/local/bin/entr…"   20 hours ago     Exited (32) 20 hours ago                                                                                                               unruffled_burnell
d6e937da07db   gcr.io/k8s-minikube/kicbase:v0.0.14   "/usr/local/bin/entr…"   20 hours ago     Exited (32) 20 hours ago                                                                                                               cool_margulis
b52bb185849b   webapplication_web                    "python webapp.py"       2 months ago     Exited (255) 2 months ago   0.0.0.0:5000->5000/tcp                                                                                     webapplication_web_1
c300ff3c975f   hello-world                           "/hello"                 2 months ago     Exited (0) 2 months ago                                                                                                                nostalgic_wiles
2cf30e6b6538   redis:alpine                          "docker-entrypoint.s…"   2 months ago     Exited (255) 2 months ago   6379/tcp                                                                                                   webapplication_redis_1
849c5a4208c4   gcr.io/k8s-minikube/kicbase:v0.0.14   "/usr/local/bin/entr…"   2 months ago     Exited (255) 2 months ago   127.0.0.1:32771->22/tcp, 127.0.0.1:32770->2376/tcp, 127.0.0.1:32769->5000/tcp, 127.0.0.1:32768->8443/tcp   minikube
PS C:\projects\docker\volume_mount> docker start 4e
4e
PS C:\projects\docker\volume_mount> docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
4e790a2a869a   ubuntu    "/bin/bash"   38 minutes ago   Up 8 seconds             nostalgic_heyrovsky

PS C:\projects\docker\volume_mount> docker attacih 4e
root@4e790a2a869a:/#
/*========================================================================*/
docker rm CONTAINER ID
permanently remove

/*========================================================================*/
miko httpd

docker run -d http

-d = deatached

PS C:\projects\docker\volume_mount> docker run -d httpd
Unable to find image 'httpd:latest' locally
latest: Pulling from library/httpd
a076a628af6f: Pull complete
e444656f7792: Pull complete
0ec35e191b09: Pull complete
4aad5d8db1a6: Pull complete
eb1da3ea630f: Pull complete
Digest: sha256:2fab99fb3b1c7ddfa99d7dc55de8dad0a62dbe3e7c605d78ecbdf2c6c49fd636
Status: Downloaded newer image for httpd:latest
60d330853b470fc246f451ff7bc4bb19f083b404d7b1d1acda44f74e5bf1ab76
PS C:\projects\docker\volume_mount>
PS C:\projects\docker\volume_mount> docker ps
CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS          PORTS     NAMES
60d330853b47   httpd     "httpd-foreground"   21 seconds ago   Up 16 seconds   80/tcp    vibrant_diffie
PS C:\projects\docker\volume_mount> docker exec -it 60 /bin/bash
root@60d330853b47:/usr/local/apache2#
/*========================================================================*/
PS C:\projects\docker\volume_mount> docker run -d httpd
PS C:\projects\docker\volume_mount> docker ps
CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS          PORTS     NAMES
60d330853b47   httpd     "httpd-foreground"   21 seconds ago   Up 16 seconds   80/tcp    vibrant_diffie
PS C:\projects\docker\volume_mount> docker exec -it 60 /bin/bash
root@60d330853b47:/usr/local/apache2# curl localhost:80
bash: curl: command not found
installin all on container slide
 apt-get update
  apt-get install curl
  root@60d330853b47:/usr/local/apache2# curl localhost:80
<html><body><h1>It works!</h1></body></html>

docker logs 60 -f vrátí logy na containeru 60...
docker inspect 60 vrátí konfiguraci containeru 60...
docker rm -f 60 zmaže container 60...

docker run -d -p 8080:80 httpd

nastartuje container a port 80 na containeru routuje na port 8080 na našem poči.
teď už server vidim na svem pc http://localhost:8080/

PS C:\projects\docker\volume_mount> docker ps
CONTAINER ID   IMAGE     COMMAND              CREATED         STATUS         PORTS                  NAMES
3b28d3c21318   httpd     "httpd-foreground"   7 minutes ago   Up 7 minutes   0.0.0.0:8080->80/tcp   tender_wescoff
--
docker inspect 60 vrátí konfiguraci containeru 60...

            "NetworkMode": "default",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8080"
                    }
                ]
            },

/*========================================================================*/
?? protoc
docker run --rm -v $(pwd):$(pwd) -w $(pwd) znly/protoc --python_out=. -I. myfile.proto

/*========================================================================*/

C++ dockers
Dockerfile
FROM gcc:latest

COPY . /usr/src/ccp_test

WORKDIR /usr/src/ccp_test

RUN g++ -o Test main.cpp

CMD [ "./Test" ]



/*========================================================================*/

Digest: sha256:c42a12f8ced21af9419084a22ceaf5ff2a034bc6616912ad5bfab8cf45f7dd04
Status: Downloaded newer image for grpctesting/protobuf_70e53ae1868cce2192317507ba0f02618dfbb2ba:latest
docker.io/grpctesting/protobuf_70e53ae1868cce2192317507ba0f02618dfbb2ba:latest



/*========================================================================*/
PS C:\projects\docker\cpp_images\gcc1> dir

cat Dockerfile

FROM gcc:latest

COPY . /usr/src/ccp_test

WORKDIR /usr/src/ccp_test

RUN g++ -o Test ukazatel.cpp

CMD [ "./Test" ]


/*========================================================================*/


Directory: C:\projects\docker\cpp_images\gcc1


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          2/3/2021   4:35 PM            126 Dockerfile
-a----          2/3/2021   4:34 PM           1318 ukazatel.cpp


PS C:\projects\docker\cpp_images\gcc1> docker build . -t cpp_test
[+] Building 15.5s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                            0.3s
 => => transferring dockerfile: 163B                                                                                                                                                                            0.1s
 => [internal] load .dockerignore                                                                                                                                                                               0.2s
 => => transferring context: 2B                                                                                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/gcc:latest                                                                                                                                                   8.9s
 => [auth] library/gcc:pull token for registry-1.docker.io                                                                                                                                                      0.0s
 => [internal] load build context                                                                                                                                                                               0.1s
 => => transferring context: 1.52kB                                                                                                                                                                             0.0s
 => CACHED [1/4] FROM docker.io/library/gcc:latest@sha256:f418921b872c4831dfc9bc33aaec2a8480d37e46190da766c3497cd8d5fedb75                                                                                      0.0s
 => [2/4] COPY . /usr/src/ccp_test                                                                                                                                                                              0.3s
 => [3/4] WORKDIR /usr/src/ccp_test                                                                                                                                                                             0.3s
 => [4/4] RUN g++ -o Test ukazatel.cpp                                                                                                                                                                          4.5s
 => exporting to image                                                                                                                                                                                          0.7s
 => => exporting layers                                                                                                                                                                                         0.5s
 => => writing image sha256:1719aab4ebc255118d275532220e33afb2d3d499c662abda2c4032a4635c4d43                                                                                                                    0.0s
 => => naming to docker.io/library/cpp_test                                                                                                                                                                     0.0s
PS C:\projects\docker\cpp_images\gcc1>

/*========================================================================*/
PS C:\projects\docker\cpp_images\c_compiler> docker build . -t c_comp:1.0
[+] Building 9.9s (11/11) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                            0.2s
 => => transferring dockerfile: 251B                                                                                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                                                                               0.2s
 => => transferring context: 2B                                                                                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                                                                                                                0.0s
 => [1/6] FROM docker.io/library/ubuntu:latest                                                                                                                                                                  0.0s
 => [internal] load build context                                                                                                                                                                               0.1s
 => => transferring context: 283B                                                                                                                                                                               0.0s
 => CACHED [2/6] RUN apt-get -y update && apt-get install -y                                                                                                                                                    0.0s
 => CACHED [3/6] RUN apt-get -y install clang                                                                                                                                                                   0.0s
 => [4/6] COPY . /usr/src/cpp_test                                                                                                                                                                              0.2s
 => [5/6] WORKDIR /usr/src/cpp_test                                                                                                                                                                             0.3s
 => [6/6] RUN clang++ -o Test ukazatel.cpp                                                                                                                                                                      1.4s
 => exporting to image                                                                                                                                                                                          7.4s
 => => exporting layers                                                                                                                                                                                         7.2s
 => => writing image sha256:8f9be12eeb3361b4204b28d968ada5d6acdfdda26060c405871ffd298f922ebc                                                                                                                    0.0s
 => => naming to docker.io/library/c_comp:1.0                                                                                                                                                                   0.0s

docker run --rm -it c_comp:1.0
PS C:\projects\docker\cpp_images\c_compiler> docker run --rm -it c_comp:1.0
f = 5.500000
f2 = 5.500000
i = 10
uf = 4206763876, *uf=5.500000

/*========================================================================*/
cd C:\projects\docker\cpp_images\gcc1>
in Dockerfile

FROM gcc:latest

ENTRYPOINT ["g++"]

#end of file.


docker build . -t cpp_comp:1.2
docker run --rm -v ${PWD}:/coko -w /coko cpp_comp:1.2 -o /coko/ukazatel.cpp

docker run --rm -v ${PWD}:/coko -w /coko klutchell/rar a myrar.rar myfile.txt


/*========================================================================*/

FROM alpine
RUN apk add --no-cache make
RUN wget http://www.rarlab.com/rar/rarlinux-5.4.0.tar.gz && \
  tar -xzvf rarlinux-5.4.0.tar.gz && \
  cd rar && \
  make && \
  mv rar_static /usr/local/bin/rar
ENTRYPOINT ["rar"]

/*========================================================================*/

docker run --rm -it -v $(pwd):/project madduci/docker-cpp-env:latest "g++ ukazatel.cpp youroutput.o"

docker run --rm -v $(pwd):/coko -w /coko klutchell/rar a myrar.rar myfile.txt

/*========================================================================*/
https://www.codeguru.com/cpp/cpp/algorithms/using-c-with-docker-engine.html

/*========================================================================*/
docker run --rm -v ${PWD}:/HelloWorld -w /HelloWorld gcc:4.9 g++ --o HelloWorld HelloWorld.cpp
docker run --rm -v ${PWD}:/HelloWorld -w /HelloWorld gcc:4.9 ./HelloWorld

/*========================================================================*/


Dockerfile for c++ env preparation
#
# Dockerfile for building C++ project
#
# https://github.com/tatsy/dockerfile/ubuntu/cxx
#

# OS image
FROM ubuntu:16.04

# Install
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update -qq && \
  apt-get upgrade -qq && \
  apt-get install -qq build-essential clang && \
  apt-get install -qq software-properties-common && \
  apt-get install -qq byobu curl git htop man unzip vim wget && \
  apt-get install -qq subversion cmake && \
  rm -rf /var/lib/apt/lists/*

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]

# Update gcc/g++ to v4.9
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test
RUN apt-get update -qq
RUN apt-get install -qq gcc-4.9 g++-4.9
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 90
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 90
RUN update-alternatives --install /usr/bin/gcov gcov /usr/bin/gcov-4.9 90

# Install LCOV
RUN git clone https://github.com/linux-test-project/lcov.git
RUN make -C lcov install
RUN apt-get install -y ruby
RUN gem install coveralls-lcov

# Install OpenMP for LLVM
RUN svn co http://llvm.org/svn/llvm-project/openmp/trunk openmp
RUN \
  cd openmp && \
  mkdir build && \
  cd build && \
  cmake .. && \
  make omp && \
  make install && \
  cd -

# Update CMake to v3.5.1
RUN git clone --depth 1 -b v3.5.1 https://github.com/Kitware/CMake.git
RUN \
  cd CMake && \
  mkdir build && \
  cd build && \
  cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr && \
  make -j4 && \
  make install && \
  ldconfig && \
  cd ../.. && \
  cmake --version

# Install Qt 5
RUN apt-get install -qq qt5-default
ENV CMAKE_PREFIX_PATH=$CMAKE_PREFIX_PATH:/opt/qt5

# Clean working directory
RUN rm -rf openmp
RUN rm -rf CMake
RUN rm -rf lcov
RUN rm -rf /usr/src/gtest

# Show environments
RUN echo "--- Build Enviroment ---"
RUN cat /etc/lsb-release
RUN gcc --version | grep gcc
RUN g++ --version | grep g++
RUN lcov --version | grep version
RUN clang --version | grep version
RUN clang++ --version | grep version
RUN cmake --version | grep version
RUN echo "------------------------"

/*========================================================================*/
PS C:\projects\docker\cpp_images\clang> cat .\Dockerfile
FROM ricejasonf/cppdock:linux_64

COPY main.cpp /opt/build

WORKDIR /opt/build

RUN clang++ -stdlib=libc++ -lc++abi main.cpp

CMD ["./a.out"]

/*========================================================================*/

cd C:\projects\docker\protobuf\protobuf-on-docker\ubuntu-15
# docker build -t protobuf_ubuntu:1.0 .
docker run -v ${PWD}:/DockerShare -it protobuf_ubuntu /bin/bash



=> exporting to image                                                                                                                                                                                         20.6s
=> => exporting layers                                                                                                                                                                                        20.3s
=> => writing image sha256:54cd70e0dc4cd8ba3cdcde2e7dc6e16910c8d895713a50e89bb9cfbb85f89c6a                                                                                                                    0.0s
=> => naming to docker.io/library/
protobuf_ubuntu:1.0
miko sudo
apt update
apt install sudo

miko git installation
$ sudo apt-get update
$ sudo apt-get install git


git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf
git submodule update --init --recursive
./autogen.sh

./configure
 make
 make check
 sudo make install
 sudo ldconfig # refresh shared library cache.


apt-get update
apt-get install pkg-config

root@03034e962516:/ws/protobuf# pkg-config --cflags protobuf
-pthread -I/usr/local/include
root@03034e962516:/ws/protobuf# pkg-config --libs protobuf
-L/usr/local/lib -lprotobuf -lpthread
root@03034e962516:/ws/protobuf# pkg-config --cflags --libs protobuf
-pthread -I/usr/local/include -L/usr/local/lib -lprotobuf -lpthread



g++ add_write.cpp addressbook.pb.cc `pkg-config --cflags --libs protobuf` -o add_write


root@03034e962516:/HelloWorld/addressbook# ./add_write ./myPhoneBook.bin
./myPhoneBook.bin: File not found.  Creating a new file.
Enter person ID number: 123
Enter name: Michal Kočandrle
Enter email address (blank for none): miko73@seznam.cz
Enter a phone number (or leave blank to finish): 602495382
Is this a mobile, home, or work phone? mobile
Enter a phone number (or leave blank to finish): 122345567
Is this a mobile, home, or work phone? home
Enter a phone number (or leave blank to finish):

done ;-)


/*========================================================================*/

g++ add_main.cpp addressbook.pb.cc `pkg-config --cflags --libs protobuf` -o add_main

g++ $(pkg-config --cflags --libs opencv4) -std=c++11  one.cpp -o one

root@03034e962516:/HelloWorld/addressbook# ls -l
total 80
-rwxrwxrwx 1 root root  1986 Feb  4 18:39 add_main.cpp
-rw-r--r-- 1 root root 36089 Feb  4 18:33 addressbook.pb.cc
-rw-r--r-- 1 root root 39083 Feb  4 18:33 addressbook.pb.h
-rwxrwxrwx 1 root root   436 Feb  4 18:21 addressbook.proto
root@03034e962516:/HelloWorld/addressbook# g++ add_main.cpp addressbook.pb.cc `pkg-config --cflags --libs protobuf`
root@03034e962516:/HelloWorld/addressbook# ls -la
total 204
drwxrwxrwx 1 root root    512 Feb  4 19:00 .
drwxrwxrwx 1 root root    512 Feb  4 18:21 ..
-rwxr-xr-x 1 root root 124560 Feb  4 19:00 a.out
-rwxrwxrwx 1 root root   1986 Feb  4 18:39 add_main.cpp
-rw-r--r-- 1 root root  36089 Feb  4 18:33 addressbook.pb.cc
-rw-r--r-- 1 root root  39083 Feb  4 18:33 addressbook.pb.h
-rwxrwxrwx 1 root root    436 Feb  4 18:21 addressbook.proto




g++ add_write.cpp addressbook.pb.cc `pkg-config --cflags --libs protobuf` -o add_write
g++ add_read.cpp addressbook.pb.cc `pkg-config --cflags --libs protobuf` -o add_read

root@03034e962516:/HelloWorld/addressbook# ./add_read ./myPhoneBook.bin
Person ID: 123
  Name: Michal Kočandrle
  E-mail address: mikoý73@seznam.cz
  Mobile phone #: 602495382
  Home phone #: 122345567



in C:\projects\docker\protobuf\protobuf-on-docker\ubuntu-15>





/*========================================================================*/
 => [24/33] RUN echo "#######################"                                                                                                                                                                  0.8s
 => [25/33] RUN tar -xvf /ws/protobuf-3.0.0-beta-3.2.tar                                                                                                                                                        1.6s
 => [26/33] RUN ls -R /ws/protobuf-3.0.0-beta-3.2/                                                                                                                                                              1.1s
 => [27/33] RUN echo "#######################"                                                                                                                                                                  1.0s
 => ERROR [28/33] RUN ls -R /ws/protobuf-3.0.0-beta-3.2/lib-gcc53/                                                                                                                                              0.8s
------
 > [28/33] RUN ls -R /ws/protobuf-3.0.0-beta-3.2/lib-gcc53/:
#32 0.697 ls: cannot access '/ws/protobuf-3.0.0-beta-3.2/lib-gcc53/': No such file or directory
------
executor failed running [/bin/sh -c ls -R /ws/protobuf-3.0.0-beta-3.2/lib-gcc53/]: exit code: 2

https://github.com/protocolbuffers/protobuf/blob/master/src/README.md

/*========================================================================*/

root@03034e962516:/HelloWorld/addressbook# protoc -I=. --cpp_out=. addressbook.proto
root@03034e962516:/HelloWorld/addressbook# ls -l
total 76
-rw-r--r-- 1 root root 36089 Feb  4 17:33 addressbook.pb.cc
-rw-r--r-- 1 root root 39083 Feb  4 17:33 addressbook.pb.h
-rwxrwxrwx 1 root root   436 Feb  4 17:21 addressbook.proto

/*========================================================================*/
protobuf ubuntu installation overview
apt-get install autoconf automake libtool curl make g++ unzip
wget https://github.com/protocolbuffers/protobuf/release/download/v3.11.0/protobuf-cpp-33.11.0.tar.gz
tar -xvzf protobuf-cpp-33.11.0.tar.gz
cd protobuf-cpp-33.11.0
./configure
make
make install
ldconfig

# project part
protoc -I. --cpp_out=. helloproto.proto
g++ -std=c++17 helloproto.cpp helloproto.pb.cc -o helloproto `pkg-config --cflags --libs protobuf`

./binaryfilename

/*========================================================================*/
install python

Installing Python 3.9 on Ubuntu with Apt
Installing Python 3.9 on Ubuntu with apt is a relatively straightforward process and takes only a few minutes to complete.

Update the packages list and install the prerequisites:

  sudo apt update
  sudo apt install software-properties-common

Add the deadsnakes PPA to your system’s sources list:

  sudo add-apt-repository ppa:deadsnakes/ppa

When prompted, press [Enter] to continue.

Once the repository is enabled, you can install Python 3.9 by executing:

  sudo apt install python3.9
Verify that the installation was successful by typing:
  python3.9 --version
   Python 3.9.1+

Installing Python 3.9 on Ubuntu from Source
Compiling Python from the source allows you to install the latest Python version and customize the build options. However, you won’t be able to maintain your Python installation through the apt package manager.
The following steps explain how to compile Python 3.9 from the source:

Install the dependencies necessary to build Python:

  sudo apt update
  sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
Download the latest release’s source code from the Python download page with wget :

  wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
Once the download is complete, extract the gzipped archive :

  tar -xf Python-3.9.1.tgz
Switch to the Python source directory and run the configure script, which performs a number of checks to make sure all of the dependencies on your system are present:

  cd Python-3.9.1
  ./configure --enable-optimizations
The --enable-optimizations option optimizes the Python binary by running multiple tests. This makes the build process slower.

Start the Python 3.9 build process:

  make -j 12
For faster build time, modify the -j to correspond to the number of cores in your processor. You can find the number by typing nproc.

When the build process is complete, install the Python binaries by typing:

  sudo make altinstall
We’re using altinstall instead of install because later will overwrite the default system python3 binary.

That’s it. Python 3.9 has been installed and ready to be used. To verify it, type:

  python3.9 --version

The output should show the Python version:
Python 3.9.1


/*========================================================================*/
gn configuration
https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up
cd /ws
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH=/ws/depot_tools:$PATH






git config --global user.name "Michal Kocandrle"
git config --global user.email "miko73@seznam.cz"
git config --global core.autocrlf false
git config --global core.filemode false
# and for fun!
git config --global color.ui true



/*========================================================================*/
disk space available for images
??? grpctesting/protobuf_70e53ae1868cce2192317507ba0f02618dfbb2ba
protobuf_ubuntu

cd C:\projects\docker\protobuf\protobuf-on-docker\ubuntu-15
# docker build -t protobuf_ubuntu:1.0 .

docker run -v ${PWD}:/HelloWorld -it miko73/protobuf_ubuntu:1.0 /bin/bash




docker rm


root@f49f8e25c4ff:/# df -k
Filesystem     1K-blocks      Used Available Use% Mounted on
overlay        263174212  32438820 217297236  13% /
tmpfs              65536         0     65536   0% /dev
tmpfs            3212296         0   3212296   0% /sys/fs/cgroup
shm                65536         0     65536   0% /dev/shm
C:\            387482620 260456164 127026456  68% /HelloWorld
/dev/sdc       263174212  32438820 217297236  13% /etc/hosts
tmpfs            3212296         0   3212296   0% /proc/acpi
tmpfs            3212296         0   3212296   0% /sys/firmware


root@03034e962516:/ws# df -k
Filesystem     1K-blocks      Used Available Use% Mounted on
overlay        263174212  32438408 217297648  13% /
tmpfs              65536         0     65536   0% /dev
tmpfs            3212296         0   3212296   0% /sys/fs/cgroup
shm                65536         0     65536   0% /dev/shm
C:\            387482620 261938072 125544548  68% /HelloWorld
/dev/sdc       263174212  32438408 217297648  13% /etc/hosts
tmpfs            3212296         0   3212296   0% /proc/acpi
tmpfs            3212296         0   3212296   0% /sys/firmware

root@03034e962516:/ws# df -k
Filesystem     1K-blocks      Used Available Use% Mounted on
overlay        263174212  32438420 217 297 636  13% /
tmpfs              65536         0     65536   0% /dev
tmpfs            3212296         0   3212296   0% /sys/fs/cgroup
shm                65536         0     65536   0% /dev/shm
C:\            387482620 261938264 125544356  68% /HelloWorld
/dev/sdc       263174212  32438420 217297636  13% /etc/hosts
tmpfs            3212296         0   3212296   0% /proc/acpi
tmpfs            3212296         0   3212296   0% /sys/firmware

/*========================================================================*/
PS C:\projects\minikube> docker push miko73/protobuf_ubuntu:1.0



The push refers to repository [docker.io/miko73/protobuf_ubuntu]
03d3a4fc56a7: Pushed
5f70bf18a086: Mounted from grpctesting/protobuf_70e53ae1868cce2192317507ba0f02618dfbb2ba
5fa899cc3ab0: Pushed
211127c7724a: Pushed
107924cbaa22: Pushed
f2d31abc5534: Pushed
e75e4f367f42: Pushed
f5e390ce1f7e: Pushed
4b2ec73b5a63: Pushed
5ace4715f03e: Pushed
298814f6db94: Pushed
ce2baf64895f: Pushed
e79521344271: Pushed
8fdbcc70f29e: Pushed
1bd184e1398a: Pushed
fe85fa9f5d7d: Pushed
14773191ee32: Pushed
cc9d18e90faa: Mounted from miko73/ubuntu
0c2689e3f920: Mounted from miko73/ubuntu
47dde53750b4: Mounted from miko73/ubuntu
1.0: digest: sha256:6de8fc1ecf5c585f97ac6a2e1eec6c2d4c85867da36f1c9f7c8f8bc136cacd2f size: 5320

/*========================================================================*/
PS C:\projects\minikube> docker commit 9bb07a0f708b miko73/protobuf_ubuntu:1.1
sha256:d960198eb0326b463c40aaf79482a173f7d61eaab5a0189d40de7aa6a3e78490

PS C:\projects\minikube\kubernetes-example\client> docker commit 9bb07a0f708b miko73/protobuf_ubuntu:1.1
sha256:039df508aef81d615e5b0727c466be0b4d75a8ef6c27d1f01dd99b8f061e9be8

PS C:\Users\micha> docker commit 9bb07a0f708b miko73/protobuf_ubuntu:1.1
sha256:89fdb00331a8e0958652e3b0f866699de921f53cea1172f68232a721fb8cd82f

PS C:\projects\minikube> docker push miko73/protobuf_ubuntu:1.1

The push refers to repository [docker.io/miko73/protobuf_ubuntu]
acd398826e5a: Pushed
03d3a4fc56a7: Layer already exists
5f70bf18a086: Layer already exists
5fa899cc3ab0: Layer already exists
211127c7724a: Layer already exists
107924cbaa22: Layer already exists
f2d31abc5534: Layer already exists
e75e4f367f42: Layer already exists
f5e390ce1f7e: Layer already exists
4b2ec73b5a63: Layer already exists
5ace4715f03e: Layer already exists
298814f6db94: Layer already exists
ce2baf64895f: Layer already exists
e79521344271: Layer already exists
8fdbcc70f29e: Layer already exists
1bd184e1398a: Layer already exists
fe85fa9f5d7d: Layer already exists
14773191ee32: Layer already exists
cc9d18e90faa: Layer already exists
0c2689e3f920: Layer already exists
47dde53750b4: Layer already exists
1.1: digest: sha256:e3218c7f8ac6b093197a96dd35fd13383990002ccbeb9ca537224a87e1f65748 size: 5533

/*========================================================================*/
docker commit e9e3d530133b miko73/protobuf_ubuntu:1.
PS C:\Users\micha> docker commit e9e3d530133b miko73/protobuf_ubuntu:1.3
sha256:43f5ea916ad27c744069ab93ab559eeeb1d72125cde5fe65730fa8b11e680514
docker commit 9ab808cce2e9 miko73/protobuf_ubuntu:1.4


docker run -v ${PWD}:/HelloWorld -it protobuf_ubuntu_local:1.0 /bin/bash

docker run -v ${PWD}:/HelloWorld -it miko73/protobuf_ubuntu:1.3 /bin/bash

docker run -v ${PWD}:/HelloWorld -it miko73/protobuf_ubuntu:1.1 /bin/bash

docker commit 9ab808cce2e9 miko73/protobuf_ubuntu:1.4



/*========================================================================*/

https://github.com/google/protobuf/tree/master/python#c-implemetation
o
==============================================================================
miko inseznam
cd ~/ftxt-indexer
k8s-infra/nginx-ingress/images/nginx-slim/Dockerfile
k8s-infra/monitoring/fresh_statistic/Dockerfile
k8s-infra/monitoring/alertmanager/Dockerfile
k8s-infra/monitoring/prometheus/Dockerfile
k8s-infra/k8s-deployer/tiller.Dockerfile
mega-indexer-fulltext/deploy/Dockerfile
indexer/test-service/deploy/Dockerfile
k8s-infra/k8s-deployer/Dockerfile
k8s-infra/fake-feeder/Dockerfile
mega-incontrol/deploy/Dockerfile
k8s-infra/grafana/Dockerfile
k8s-infra/logging/Dockerfile
==============================================================================

mega-indexer-fulltext/deploy/Dockerfile

ARG BUILD_DISTRO=stretch

 FROM docker.dev.dszn.cz/debian:$BUILD_DISTRO

 COPY *.deb run.sh revinfo.txt /

 ENV DEBIAN_FRONTEND noninteractive

 RUN echo "deb http://repo/repo/buster-testing buster-testing main" >> /etc/apt/sources.list \
     && dpkg -i /*.deb || apt-get update \
     && apt-get -f -y install --no-install-recommends \
     && apt-get -y install logrotate \
     && rm -f /*.deb \
     &&  rm -rf /var/lib/apt/lists/*

 ENTRYPOINT ["/run.sh"]
==============================================================================


