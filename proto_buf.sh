/*========================================================================*/
docker run -v ${PWD}:/HelloWorld -it protobuf_ubuntu:1.0 /bin/bash
docker run -v ${PWD}:/HelloWorld -it ubuntu /bin/sh

=> exporting to image                                                                                                                                                                                         20.6s
=> => exporting layers                                                                                                                                                                                        20.3s
=> => writing image sha256:54cd70e0dc4cd8ba3cdcde2e7dc6e16910c8d895713a50e89bb9cfbb85f89c6a                                                                                                                    0.0s
=> => naming to docker.io/library/
protobuf_ubuntu:1.0

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

oot@03034e962516:/HelloWorld/addressbook# protoc -I=. --cpp_out=. addressbook.proto
root@03034e962516:/HelloWorld/addressbook# ls -l
total 76
-rw-r--r-- 1 root root 36089 Feb  4 17:33 addressbook.pb.cc
-rw-r--r-- 1 root root 39083 Feb  4 17:33 addressbook.pb.h
-rwxrwxrwx 1 root root   436 Feb  4 17:21 addressbook.proto


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


docker build -t protobuf_ubuntu:1.0 .



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
