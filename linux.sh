/scp
==============================================================================
in ubuntu I switched the mapping of keyboard using tweaks
https://askubuntu.com/questions/1029588/18-04-ctrlshift-to-change-language
==============================================================================
sudo nano /etc/systemd/logind.conf

In the file above, I changed only this line:

#HandleLidSwitch=suspend

to this:

HandleLidSwitch=ignore

After saving the file, I ran:

sudo systemctl restart systemd-logind


#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.
#
# Entries in this file show the compile time defaults.
# You can change settings by editing this file.
# Defaults can be restored by simply deleting this file.
#
# See logind.conf(5) for details.

[Login]
#NAutoVTs=6
#ReserveVT=6
#KillUserProcesses=no
#KillOnlyUsers=
#KillExcludeUsers=root
#InhibitDelayMaxSec=5
#HandlePowerKey=poweroff
#HandleSuspendKey=suspend
#HandleHibernateKey=hibernate
#HandleLidSwitch=suspend
#HandleLidSwitchExternalPower=suspend
HandleLidSwitchDocked=ignore
#PowerKeyIgnoreInhibited=no
#SuspendKeyIgnoreInhibited=no
#HibernateKeyIgnoreInhibited=no
#LidSwitchIgnoreInhibited=yes
#HoldoffTimeoutSec=30s
#IdleAction=ignore
#IdleActionSec=30min
#RuntimeDirectorySize=10%
#RuntimeDirectoryInodes=400k
#RemoveIPC=yes
#InhibitorsMax=8192
#SessionsMax=8192


sudo apt install gconf2
michal-kocanrdle@kocandrle-m:~$ gconftool-2 -t string -s /apps/gnome-power-manager/buttons/lid_ac nothing
michal-kocanrdle@kocandrle-m:~$ gconftool-2 -t string -s /apps/gnome-power-manager/buttons/lid_battery nothing







/*===============================================================================================*/
when setting up the ssh key for Virtual Env
On virtual env it is necessary to add the private certificate pared with the public certificate stored on gitlab

sluha update
in ~/.ssh

chmod 600 miko_rsa

eval $(ssh-agent -s)
ssh-add ./miko_rsa
/*===============================================================================================*/
miko ide
https://github.com/dense-analysis/ale
https://github.com/MaskRay/ccls
/*===============================================================================================*/
ubuntu version
michal-kocanrdle@kocandrle-m:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.10
Release:	20.10
Codename:	groovy
/*===============================================================================================*/
vim documentation
http://vimdoc.sourceforge.net/htmldoc/quickfix.html#quickfix
/*===============================================================================================*/
ninja documentation
https://ninja-build.org/manual.html
/*===============================================================================================*/


less compile_command.json
{
  "directory": "/home/prj/build/src/adam",
  "command": "/opt/sdk/sysroots/x86_64-ocpsdk-linux/usr/bin/arm-poky-linux-gnueabi/arm-poky-linux-gnueabi-g++   -march=armv7ve -mthumb -mfpu=neon -mfloat-abi=hard -mcpu=cortex-a7 --s
ysroot=/opt/sdk/sysroots/cortexa7t2hf-neon-poky-linux-gnueabi --sysroot=/opt/sdk/sysroots/cortexa7t2hf-neon-poky-linux-gnueabi  -DBOOST_ENABLE_ASSERT_HANDLER -I/home/ocp/src/c
pp1/eden/include -I/home/prj/src/adam/include -I/home/prj/src/serpent/include -I/home/ocp/user_sysroots/11.0.4/usr/include -I/home/prj/gen_files -I
/home/prj/src/adam/../include   -O2 -pipe -g -feliminate-unused-debug-types  -Wno-psabi -Wno-maybe-uninitialized -DBOOST_ASIO_ENABLE_SEQUENTIAL_STRAND_ALLOCATION   -Wall -Wext
ra -pedantic -funsigned-char -std=gnu++17 -o CMakeFiles/adam_app.dir/src/main.cpp.o -c /home/prj/src/adam/src/main.cpp",
  "file": "/home/prj/src/adam/src/main.cpp"


debian@miko-debian-dev:~/sluha/indexer/worker/src$ sudo apt-get upgrade
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
The following packages have been kept back:
  libmurmurhash-dev szn-libsslwrapper-dev
0 upgraded, 0 newly installed, 0 to remove and 2 not upgraded.
debian@miko-debian-dev:~/sluha/indexer/worker/src$ sudo apt-get install szn-libsslwrapper-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 szn-libsslwrapper-dev : Depends: szn-libsslwrapper8 (= 5.0.4) but 5.0.0 is to be installed
E: Unable to correct problems, you have held broken packages.

debian@miko-debian-dev:~/sluha/indexer/worker/src$ sudo apt-get remove szn-libsslwrapper8
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  szn-libhttpstorage-dev szn-libhttpstorage4 uuid-dev
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  szn-libfileserver-dev szn-libsslwrapper-dev szn-libsslwrapper8 szn-metaserver szn-metaserver-dev
0 upgraded, 0 newly installed, 5 to remove and 1 not upgraded.
After this operation, 16.2 MB disk space will be freed.
Do you want to continue? [Y/n] Y
(Reading database ... 61059 files and directories currently installed.)
Removing szn-libfileserver-dev (5.0.3) ...
Removing szn-metaserver-dev (2.8.29) ...
Removing szn-libsslwrapper-dev (5.0.0) ...
Removing szn-metaserver:amd64 (2.8.29) ...
Removing szn-libsslwrapper8 (5.0.0) ...
Processing triggers for libc-bin (2.28-10) ...

debian@miko-debian-dev:~/sluha/indexer/worker/src$ sudo apt-get upgrade
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
The following packages were automatically installed and are no longer required:
  szn-libhttpstorage-dev szn-libhttpstorage4 uuid-dev
Use 'sudo apt autoremove' to remove them.
The following packages have been kept back:
  libmurmurhash-dev
0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.
==============================================================================
debian@miko-debian-dev:~/sluha/indexer/worker/src$ sudo apt-get remove libmurmurhash-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libmurmurhash1 szn-libhttpstorage-dev szn-libhttpstorage4 uuid-dev
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  libmurmurhash-dev
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 53.2 kB disk space will be freed.
Do you want to continue? [Y/n] n
Abort.
==============================================================================
debian@miko-debian-dev:~/sluha/indexer/worker/src$ sudo apt-cache show libmurmurhash1
Package: libmurmurhash1
Priority: optional
Section: libs
Installed-Size: 28
Maintainer: Debian Med Packaging Team <debian-med-packaging@lists.alioth.debian.org>
Architecture: amd64
Source: libmurmurhash
Version: 1.3-2
Depends: libc6 (>= 2.4)
Filename: pool/main/libm/libmurmurhash/libmurmurhash1_1.3-2_amd64.deb
Size: 5556
MD5sum: b682b3055333589e12b5abe0e4124971
SHA1: 972bdbd20246d49fa6ed83cde1a65e6eb53caa39
SHA256: 905aad518eb4d48504c99dd4a0a1375b9ec09db8977303db4bc8678307d0b3d4
SHA512: 63a8c85da673cb40eed7add0e1bb93a32a427e593643cc7c89c3921ea57621561a002e12119c662e04dd2f0c4d2e2d733695a8f341aa8c92cca8e56af89e1c6b
Description: Portable MurmurHash Implementation
Description-md5: de92456beacfaf0ff9af9eb35eb0a6f2
Homepage: https://github.com/kloetzl/libmurmurhash
Tag: role::shared-lib


==============================================================================
ssh copyo

scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/out_linux/Debug/cache/q_avro/2021-02-22-07-57/entity/part-0049.avro ./entity.avro
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/out_linux/Debug/cache/q_avro/2021-02-22-07-57/token/part-0049.avro ./token.avro
scp logs.tar debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/test
scp * debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/test_data/barrel_da

scp /home/michal-kocanrdle/Python/fastavro/tests/my_test.py debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/projects/fastavro/tests

scp /home/michal-kocanrdle/Downloads/1 debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/test_data

cd ~/projects/data
scp * debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/local-storage/1/complete/2021-02-15-17-00-00-000000/barrels/current/barrel_qu

cd /home/michal-kocanrdle/Downloads/barrel_qs/
scp * debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/test_data/barrel_qs

scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/csv.tar.gz ./


cd /home/michal-kocanrdle/projects/code_backup/
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/data.tar.gz ./

scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/merge/merge/src/plugins/avro_termulbarrel.cc ./

scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/indexer/worker/doc/DOC.md ./
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/indexer/worker/tools/download-url-job.py  ./
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/merge/merge/BUILD.gn ./
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/merge/merge/CMakeLists.txt ./
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/merge/merge/src/plugins/Makefile.am ./
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/fulltext/dump/conf/randomUrl.conf ./

scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/storage/avro-schema/BUILD.gn ./
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/out_linux/Debug/conf/miko_worker.conf ./
scp ./test_miko.cc debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/code_back
scp * debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/test_data/



==============================================================================
clipboard
https://www.seanh.cc/2020/12/27/copy-and-paste-in-tmux/

how to bin vim copy buffer to xserver clipboard,
from tmux to desktop

bind -t vi-copy y copy-pipe "xclip -sel clip -i"
==============================================================================
miko debian
https://www.debian.org/doc/manuals/debian-reference/index.en.html
==============================================================================
seznam packages pro debian

repo-web.dev.dszn.cz


==============================================================================



