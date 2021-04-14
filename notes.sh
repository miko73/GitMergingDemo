
chromium_all.ssh
docker_all.sh
gn_all.md
linux.sh  notes.txt
proto_buf.sh
python_all.py
scripts_all.sql
sez_knowledge.txt
seznam_all.md
vim.txt
vyvojove_prostredi.txt

ssh debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz

export PATH=$PWD:$PATH

https://teams.szn.cz/login

MpAy2FVMM960
Plesoun.73

https://teams.szn.cz/vyhledavani/channels/town-square

top bibiner doc
https://srch.gitlab.seznam.net/overview/tech/newbies/


https://neznam.szn.cz/
https://posta.szn.cz/
https://gitlab.seznam.net
https://gitlab.seznam.net/-/profile/keys




https://repo-web.dev.dszn.cz/mirrors

docker-buster deb http://repo/mirror/docker-buster docker-buster stable	https://download.docker.com/linux/debian buster stable	amd64

# docker-buster (origin: 'https://download.docker.com/linux/debian buster stable')
deb http://repo/mirror/docker-buster docker-buster stable


sudo add-apt-repository \
   "deb [arch=arm64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

sudo add-apt-repository "deb http://repo/mirror/docker-buster docker-buster stable"

sudo add-apt-repository "deb http://repo/mirror/docker-buster docker-buster stable"





/home/debian/ $ apt-cache madison docker-ce
 docker-ce | 5:20.10.3~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:20.10.2~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:20.10.1~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:20.10.0~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.15~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.14~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.13~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.12~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.11~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.10~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.9~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.8~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.7~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.6~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.5~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.4~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.3~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.2~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.1~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:19.03.0~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.9~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.8~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.7~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.6~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.5~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.4~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.3~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.2~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.1~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 5:18.09.0~3-0~debian-buster | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 18.06.3~ce~3-0~debian | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 18.06.2~ce~3-0~debian | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 18.06.1~ce~3-0~debian | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 18.06.0~ce~3-0~debian | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 18.03.1~ce-0~debian | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 18.03.0~ce-0~debian | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 17.12.1~ce-0~debian | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages
 docker-ce | 17.12.0~ce-0~debian | http://repo/mirror/docker-buster docker-buster/stable amd64 Packages



miko start it

sudo apt-get install docker-ce=5:20.10.3~3-0~debian-buster docker-ce-cli=5:20.10.3~3-0~debian-buster containerd.io


/home/debian/ $ docker --version
Docker version 20.10.3, build 48d30b5
/home/debian/ $



/home/debian/ $ sudo service docker status
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2021-02-08 16:24:30 CET; 10min ago
     Docs: https://docs.docker.com
 Main PID: 11992 (dockerd)
    Tasks: 24
   Memory: 56.4M
   CGroup: /system.slice/docker.service
           └─11992 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Feb 08 16:24:29 miko-debian-dev dockerd[11992]: time="2021-02-08T16:24:29.644821390+01:00" level=info msg="ClientConn switching balancer to \"pick_first\"" module=grpc
Feb 08 16:24:29 miko-debian-dev dockerd[11992]: time="2021-02-08T16:24:29.685996930+01:00" level=warning msg="Your kernel does not support swap memory limit"
Feb 08 16:24:29 miko-debian-dev dockerd[11992]: time="2021-02-08T16:24:29.686020262+01:00" level=warning msg="Your kernel does not support CPU realtime scheduler"
Feb 08 16:24:29 miko-debian-dev dockerd[11992]: time="2021-02-08T16:24:29.686179905+01:00" level=info msg="Loading containers: start."
Feb 08 16:24:29 miko-debian-dev dockerd[11992]: time="2021-02-08T16:24:29.925193278+01:00" level=info msg="Default bridge (docker0) is assigned with an IP address 172.17.0.0/16. Daemon option --bip can b
Feb 08 16:24:30 miko-debian-dev dockerd[11992]: time="2021-02-08T16:24:30.002626967+01:00" level=info msg="Loading containers: done."
Feb 08 16:24:30 miko-debian-dev dockerd[11992]: time="2021-02-08T16:24:30.051682206+01:00" level=info msg="Docker daemon" commit=46229ca graphdriver(s)=overlay2 version=20.10.3
Feb 08 16:24:30 miko-debian-dev dockerd[11992]: time="2021-02-08T16:24:30.051788309+01:00" level=info msg="Daemon has completed initialization"
Feb 08 16:24:30 miko-debian-dev systemd[1]: Started Docker Application Container Engine.
Feb 08 16:24:30 miko-debian-dev dockerd[11992]: time="2021-02-08T16:24:30.077943374+01:00" level=info msg="API listen on /var/run/docker.sock"

"

/home/debian/ $ sudo docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
/home/debian/ $ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES




svn install
sudo apt-get install subversion





miko-debian-dev
miko-debian-dev	debian-10-amd64	10.244.14.176, 2a02:598:244::667 t1.16c16r100d	mysshkey Active	az1	None Running 14 minut



/home/michal-kocanrdle/.ssh

Open Stack
https://horizon.ko1.os.ops.iszn.cz/
(login using standrad credentials)

debian@miko-debian-dev:~$ ssh-keygen -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/debian/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/debian/.ssh/id_rsa.
Your public key has been saved in /home/debian/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:vy3Nu2HBseLykIxZuNgBmXxyKI/9wjGqvgIkNaTSz4U debian@miko-debian-dev
The key's randomart image is:
+---[RSA 4096]----+
| ..              |
| oo. =           |
|o.o.E +     .    |
|o. B * .   . o   |
|o . B o S . +    |
|.  o * B + . .   |
|. . + * = ooo    |
|..   .   +.+o.   |
|+o.       o.+o   |
+----[SHA256]-----+



instance name

in openstack
in instances - launch instance

instance name - myname
image name = debian-10-amd64
Flavor  =  t1.16c16r100d
sshkey
availability = áz







A DNS entry is automatically created for each virtual server (an A, AAAA and PTR record) + deleted once the Instance is gone.
It has the format of <instance-name>.<project-name>.<cluster-name>.os.scif.cz (e.g. instance-name.my-project.ko1.os.scif.cz).
To log into the Instance, use SSH login. Use your SSH RSA key with the user debian or ubuntu (depends on the image):



ssh debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz

export PATH=/home/debian/gn/out:/home/debian/sluha:.:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games




michal-kocanrdle@kocandrle-m:~$ ssh debian@miko-debian-dev.my-project.ko1.os.scif.cz
ssh: Could not resolve hostname miko-debian-dev.my-project.ko1.os.scif.cz: Name or service not known
michal-kocanrdle@kocandrle-m:~$ ssh debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz
The authenticity of host 'miko-debian-dev.fulltext-dev.ko1.os.scif.cz (10.244.14.176)' can't be established.
ECDSA key fingerprint is SHA256:LeI5zEpNBTf+bKfiSqBBgYmx1gw2f40FBz+AHxOtwck.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'miko-debian-dev.fulltext-dev.ko1.os.scif.cz,10.244.14.176' (ECDSA) to the list of known hosts.
Linux miko-debian-dev 4.19.0-8-amd64 #1 SMP Debian 4.19.98-1 (2020-01-26) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
debian@miko-debian-dev:~$




miko-debian-dev.fulltext-dev.ko.os.scif.cz mikodeb






VPN
https://neznam.szn.cz/wiki/sekce/200-vpn-na-linuxu

https://vpnka.kancelar.seznam.cz/list?all=all
michal.kocandrle-1
2021-02-08 10:20:31
požádáno o VPN certifikát
None


michal.kocandrle-1


vpn.cfg

connection]
id=szn-vpn
uuid=65f69227-bb60-4286-aba0-4f4d46afcf30
type=vpn
autoconnect=false
permissions=user:tcechal:;
secondaries=

[vpn]
float=yes
connection-type=tls
remote=77.75.74.222
cipher=AES-256-CBC
comp-lzo=yes
cert-pass-flags=0
ns-cert-type=server
port=1193
tun-ipv6=yes
dev-type=tun
cert=/home/tcechal/.vpn/michal.kocandrle-1-cert.pem
ca=/home/tcechal/.vpn/cacert.pem
key=/home/tcechal/.vpn/michal.kocandrle-1-key.pem
ta=/home/tcechal/.vpn/ta-key.pem
service-type=org.freedesktop.NetworkManager.openvpn

[ipv4]
dns-search=
method=auto

[ipv6]
addr-gen-mode=stable-privacy
dns-search=
method=auto

/*===============================================================================================*/


https://neznam.szn.cz/novinky/zprava/15446-zveme-rodice-na-online-setkani-o-vzdelavani-deti

/*===============================================================================================*/

Standup




/*===============================================================================================*/

https://youtrack.seznam.cz/agiles.
YT
SRCH-4406 (priklad tasku)

skupiny

Tech Ready
Planded
In progress
code review
acceptance
ready for rlease
Done

open stack ??

/*===============================================================================================*/
h-base updates do ptototyeps ??


/*===============================================================================================*/

ebian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Feb  8 21:43:24 2021 from 10.0.117.214
debian@miko-debian-dev:~$ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json: dial unix /var/run/docker.sock: connect: permission denied
debian@miko-debian-dev:~$ sudo docker ps
CONTAINER ID   IMAGE                        COMMAND       CREATED          STATUS          PORTS     NAMES
4ef92cc37500   miko73/protobuf_ubuntu:1.1   "/bin/bash"   39 minutes ago   Up 39 minutes             peaceful_brattain

docker commit 9bb07a0f708b miko73/protobuf_ubuntu:1.1
sha256:a7cc8808aeaffc4c353a2814f49c1de47ed569add0c7ce80ae63927942869167
/*===============================================================================================*/
now installin development env according wiht
https://github.com/protocolbuffers/protobuf/blob/master/src/README.md
For advanced usage information on configure and make, please refer to the autoconf documentation:

http://www.gnu.org/software/autoconf/manual/autoconf.html#Running-configure-Scripts

https://github.com/protocolbuffers/protobuf/blob/master/src/README.md
https://github.com/dense-analysis/ale + https://github.com/MaskRay/ccls

on https://gitlab.seznam.net/
zatim mrkni na https://gitlab.seznam.net/opes/build/opes-gnbuild a https://gitlab.seznam.net/opes/build/sluha

debian@miko-debian-dev:~$ sudo git clone https://gitlab.seznam.net/opes/build/sluha.git


debian@miko-debian-dev:~$ sudo git clone https://gitlab.seznam.net/opes/build/opes-gnbuild.git

sluha update
in ~/.ssh

chmod 600 miko_rsa

eval $(ssh-agent -s)
ssh-add ./miko_rsa


debian@miko-debian-dev:~/sluha/ftxt-indexer$ cd ~/.ssh
debian@miko-debian-dev:~/.ssh$ eval $(ssh-agent -s)
Agent pid 6571
debian@miko-debian-dev:~/.ssh$ ssh-add ./miko_rsa
Enter passphrase for ./miko_rsa:
Identity added: ./miko_rsa (michal-kocanrdle@kocandrle-m)





E: Unable to locate package szn-gn
Resolved with
 sudo add-apt-repository "deb http://repo/repo/buster-dev buster-dev main"
 sudo add-apt-repository "deb http://repo/mirror/docker-buster docker-buster stable"


!!! it is necessary
debian@miko-debian-dev:~$ sudo apt update



debian@miko-debian-dev:~$ sudo apt update
Hit:1 http://repo/mirror/debian buster InRelease
Hit:2 http://repo/mirror/debian buster-security InRelease
Hit:3 http://repo/mirror/debian buster-updates InRelease
Get:4 http://repo/repo/buster-stable buster-stable InRelease [7576 B]
Hit:5 http://repo/mirror/debian-backports buster-backports InRelease
Get:6 http://repo/repo/buster-dev buster-dev InRelease [4486 B]
Hit:7 http://repo/mirror/docker-buster docker-buster InRelease
Hit:8 https://apt.llvm.org/buster llvm-toolchain-buster-10 InRelease
Get:9 http://repo/repo/buster-stable buster-stable/main amd64 Packages [445 kB]
Get:10 http://repo/repo/buster-dev buster-dev/main amd64 Packages [190 kB]
Fetched 647 kB in 1s (861 kB/s)
Reading package lists... Done
Building dependency tree
Reading state information... Done
62 packages can be upgraded. Run 'apt list --upgradable' to see them.
debian@miko-debian-dev:~$ sudo apt-get install szn-gn ninja-build git python
Reading package lists... Done
Building dependency tree
Reading state information... Done
git is already the newest version (1:2.20.1-2+deb10u3).
ninja-build is already the newest version (1.8.2-1).
python is already the newest version (2.7.16-1).
The following NEW packages will be installed:
  szn-gn
0 upgraded, 1 newly installed, 0 to remove and 62 not upgraded.
Need to get 651 kB of archives.
After this operation, 2032 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://repo/repo/buster-dev buster-dev/main amd64 szn-gn amd64 1.0.1578 [651 kB]
Fetched 651 kB in 0s (14.9 MB/s)
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package szn-gn.
(Reading database ... 42488 files and directories currently installed.)
Preparing to unpack .../szn-gn_1.0.1578_amd64.deb ...
Unpacking szn-gn (1.0.1578) ...
Setting up szn-gn (1.0.1578) ...





deb http://repo/repo/buster-dev buster-dev main
deb http://repo/repo/buster-dev buster-dev main
sudo add-apt-repository "deb http://repo/repo/buster-dev buster-dev main
sudo add-apt-repository "deb http://repo/repo/buster-dev buster-dev main



git clone ssh://git@gitlab.seznam.net:opes/build/sluha.git && cd sluha


ssh://git@gitlab.seznam.net/indexer-fulltext



WARNING: subprocess '"git" "clone" "--no-checkout" "--progress" "ssh://git@gitlab.seznam.net/indexer-fulltext/mega-indexer-fulltext.git" "/home/debian/ftxt-indexer/.slh_cache/gitlab.seznam.net-indexer--fulltext-mega--indexer--fulltext.git/_slh_mega-indexer-fulltext_4d3bd31c6fd375b73ea3c40137a7c54b3e164504_wDJcc8"' in /home/debian/ftxt-indexer/.slh_cache/gitlab.seznam.net-indexer--fulltext-mega--indexer--fulltext.git failed; will retry after a short nap...

apt-get install -y --force-yes --no-install-recommends --allow-unauthenticated ragel szn-libfileserver-dev libz-dev python3-dev szn-libprefetch-dev libcfgparser-dev szn-libprimitives-dev libjsoncpp-dev libfastrpc-dev libmurmurhash-dev libboost-thread-dev libboost-python-dev libboost-system-dev szn-fulltext-urlnorm-dev libpcre++-dev libprotobuf-dev szn-uri-dev szn-libutf-dev libboost-iostreams-dev libboost-dev libboost-program-options-dev libboost-filesystem-dev libcurl4-nss-dev python-protobuf szn-hbase-genkonst szn-liblemmatizer-dev libboost-locale-dev libboost-regex-dev szn-fulltext-libdetectcity-dev szn-libbarrel-dev szn-libtrie-dev libgtest-dev libdbglog-dev szn-fulltext-classifications-proto libgmock-dev szn-fulltext-librdforest-dev protobuf-compiler

completed
Setting up szn-fulltext-urlnorm-dev (0.6.30) ...
Setting up libboost-python-dev (1.67.0.1) ...
Processing triggers for man-db (2.8.5-2) ...
Processing triggers for libc-bin (2.28-10) ...
W: --force-yes is deprecated, use one of the options starting with --allow instead.

sudo apt-get install -y --no-install-recommends --allow-unauthenticated --allow-downgrades --allow-remove-essential --allow-change-held-packages ragel szn-libfileserver-dev libz-dev python3-dev szn-libprefetch-dev libcfgparser-dev szn-libprimitives-dev libjsoncpp-dev libfastrpc-dev libmurmurhash-dev libboost-thread-dev libboost-python-dev libboost-system-dev szn-fulltext-urlnorm-dev libpcre++-dev libprotobuf-dev szn-uri-dev szn-libutf-dev libboost-iostreams-dev libboost-dev libboost-program-options-dev libboost-filesystem-dev libcurl4-nss-dev python-protobuf szn-hbase-genkonst szn-liblemmatizer-dev libboost-locale-dev libboost-regex-dev szn-fulltext-libdetectcity-dev szn-libbarrel-dev szn-libtrie-dev libgtest-dev libdbglog-dev szn-fulltext-classifications-proto libgmock-dev szn-fulltext-librdforest-dev protobuf-compiler




New server strted here
/*===============================================================================================*/


sudo add-apt-repository "deb http://repo/mirror/docker-buster docker-buster stable"
sudo add-apt-repository "deb http://repo/repo/buster-dev buster-dev main"
sudo apt update
sudo apt upgrade
/*===============================================================================================*/

sudo apt-get install docker-ce=5:20.10.3~3-0~debian-buster docker-ce-cli=5:20.10.3~3-0~debian-buster containerd.io


/home/debian/ $ docker --version
Docker version 20.10.3, build 48d30b5
/home/debian/ $

stared https://gitlab.seznam.net/srch/k8s-infra
k8s-infra docker to fill in my k8s-infra on my localee


opes sluha recipe installation
https://gitlab.seznam.net/opes/build/recipe/blob/master/README.md



opes sluha recipe
Repository with opes specific sluha commands.

Installation:
# add XY-dev mirror to source list
$ echo "deb http://repo/repo/stretch-dev stretch-dev main" >> /etc/apt/sources.list
$ apt-get install python-jinja2 python-pkg-resources debhelper szn-debhelper cdbs pkg-config szn-gn ninja-build build-essential
Note: on Debian Wheezy you need to compile ninja from source as there is
no official package.

Commands:


init - prepares for building the target, installing 3rd party deb packages, generates ninja build files using gn


build - runs build using ninja


package - debian packaging

symupload - upload crashreporting symbols for target and its dependencies

test - running unittests

docker - create docker image (not finished)

coverage - code coverage report using clang (WIP)

cmake2gn - semiautomatic conversion from opes-cmake to GN

mega2manifest - convert mega-package to sluha manifest


Migration from opes-cmake

There are two commands for semiautomatic migration.
The mega2manifest command helps with transition of mega-packages to sluha. It grabs all add_project() calls and converts them to manifest yaml.
The cmake2gn attempts to convert most of the opes-cmake macros to their gn equivalents.
Trivial projects are usually straightforward to convert, but there are caveats and things that usually requires additional work:

no user defined variable expansion
nested python (protobuf) modules
protobuf include paths and dependecies
wrong public/private include dirs or libraries
no support for install/packacking macros
/*===============================================================================================*/

Imported
ssh://git@gitlab.seznam.net/indexer-fulltext/mega-indexer-fulltext.git/manifest/manifest to /home/debian/sluha/.slh_manifest
/home/debian/sluha/.slh_manifest


/*===============================================================================================*/
debian@miko-debian-dev:~/test$ cat /home/debian/sluha/.slh_manifest
imports:
- import: mega-indexer-fulltext
  remote: ssh://git@gitlab.seznam.net/indexer-fulltext/mega-indexer-fulltext.git
  manifests:
  - manifest/manifest
projects:
- project: mega-indexer-fulltext
  path: mega-indexer-fulltext
  remote: ssh://git@gitlab.seznam.net/indexer-fulltext/mega-indexer-fulltext.git
/*===============================================================================================*/

ccls
https://github.com/MaskRay/ccls/wiki/Build
https://sarcasm.github.io/notes/dev/compilation-database.html


cmake install
sudo apt-get install cmake

clnag9 install
sudo apt-get install build-essential xz-utils curl
curl -SL http://releases.llvm.org/9.0.0/clang+llvm-9.0.0-x86_64-pc-linux-gnu.tar.xz | tar -xJ

michal-kocanrdle@kocandrle-m:~$ mv clang+llvm-9.0.0-x86_64-pc-linux-gnu clang_9.0.0
michal-kocanrdle@kocandrle-m:~$ sudo mv clang_9.0.0 /usr/local
michal-kocanrdle@kocandrle-m:~$ export PATH=/usr/local/clang_9.0.0/bin:$PATH
michal-kocanrdle@kocandrle-m:~$ export LD_LIBRARY_PATH=/usr/local/clang_9.0.0/lib:$LD_LIBRARY_PATH
michal-kocanrdle@kocandrle-m:~$ clang++ -stdlib=libc++ -std=c++2a -Wall example.cpp -o example




git clone --depth=1 --recursive https://github.com/MaskRay/ccls
cd ~/ccls
sudo apt install libclang-9-dev
cmake -H. -BRelease -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=/path/to/clang+llvm-xxx




https://ianding.io/2019/07/29/configure-coc-nvim-for-c-c++-development/

https://github.com/prabirshrestha/vim-lsp

/*===============================================================================================*/
ALE
mkdir -p ~/.vim/autoload ~/.vim/bundle && \
> curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim


vim ~/.vimrc and paste in the following super-minimal example:

execute pathogen#infect()
syntax on
filetype plugin indent on




michal-kocanrdle@kocandrle-m:~$ cd ~/.vim/bundle && \
> git clone https://github.com/tpope/vim-sensible.git
Cloning into 'vim-sensible'...
remote: Enumerating objects: 348, done.
remote: Total 348 (delta 0), reused 0 (delta 0), pack-reused 348
Receiving objects: 100% (348/348), 50.08 KiB | 712.00 KiB/s, done.
Resolving deltas: 100% (88/88), done.




mkdir -p ~/.vim/autoload ~/.vim/bundle && \
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim


ALE acts as a "language client" to support a variety of Language Server Protocol features, including:

    Diagnostics (via Language Server Protocol linters)
    Go To Definition (:ALEGoToDefinition)
    Completion (Built in completion support, or with Deoplete)
    Finding references (:ALEFindReferences)
    Hover information (:ALEHover)
    Symbol search (:ALESymbolSearch)


/*===============================================================================================*/

[plugin-mergedocattributes]
Symbol = mergeTitles
BarrelDirname = barrel_da

[plugin-ftxtdownload-daily]
Symbol = fulltextdownloadbarrels
DownloadPath = barrel_da/

==============================================================================

[plugin-create-qu]
Symbol = pruneTermUrlBarrel
DaBarrelDir = ${BARREL_ROOT}/barrel_da/
DocBarrelPath = barrel_d/documents.5

[plugin-create-qs]
Symbol = pruneTermSiteBarrel
DaBarrelDir = ${BARREL_ROOT}/barrel_da/


[plugin-create-qds-ftxt]
Symbol = createQDSBarrelFtxt
DocAttributesBarrelPath = ${BARREL_ROOT}/barrel_da
DocAttributesBarrelPath = /home/debian/ftxt-indexer/out_linux/Debug/cache/${CLUSTER_ID}/barrel_da


[plugin-create-qds-generic]
Symbol = createQDSBarrel

DocAttributesBarrelPath = ${BARREL_ROOT}/barrel_da
DocAttributesBarrelPath = /home/debian/ftxt-indexer/out_linux/Debug/cache/${CLUSTER_ID}/barrel_da


[plugin-create-qds-ftxt-complete]
Symbol = createQDSBarrelFtxt
DocAttributesBarrelPath = ${BARREL_ROOT}/barrel_da


[plugin-create-qds-generic-complete]
Symbol = createQDSBarrel
DocAttributesBarrelPath = ${BARREL_ROOT}/barrel_da







debian@miko-debian-dev:~/ftxt-indexer/merge/merge/src/plugins$ rg -i pruneTermSiteBarrel
prune_termurlbarrel.cc
45:int pruneTermSiteBarrel(
322:int pruneTermSiteBarrel(
329:    LOG(INFO3, "running pruneTermSiteBarrel in plugin '%s'", pluginName.c_str());
debian@miko-debian-dev:~/ftxt-indexer/merge/merge/src/plugins$ rg -i pruneTermUrlBarrel
Makefile.am
17:             libprunetermurlbarrel.la libcreateqdsbarrel.la libfilteranchors.la \
45:libprunetermurlbarrel_la_SOURCES = prune_termurlbarrel.cc
46:libprunetermurlbarrel_la_LIBADD = $(top_builddir)/libbarrel/libbarrel.la \

prune_termurlbarrel.cc
40:int pruneTermUrlBarrel(
263:int pruneTermUrlBarrel(
270:    LOG(INFO3, "running pruneTermUrlBarrel in plugin '%s'", pluginName.c_str());

==============================================================================








/*===============================================================================================*/
