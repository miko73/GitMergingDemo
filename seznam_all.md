Ahoj,
/*========================================================================*/
miko settings

root@1923fc09e643:/ws/gn/examples/simple_build# apt update
root@1923fc09e643:/ws/gn/examples/simple_build# apt-get install tree
export PATH=/ws/gn/out:.:$PATH

Enable Copy on Select in Windows Terminal
https://www.jackofalladmins.com/knowledge%20bombs/dev%20dungeon/windows-terminal-copy-selection/
Copy on select
https://packagecontrol.io/packages/Copy%20on%20Select


/ws/gn/ninjatracing

/
/*========================================================================*/


ja bych k tomu dovolil doplnit par veci na ktere se zamerit, protoze je toho mozna vic nez dost :)

V Dockeru je dulezite krome samotneho
# vytvareni image (tj. syntax Dockerfile) jeste
# umet namountit volume,
# vystavit sitovy port containeru, (docker run -d -p 8080:80 httpd)
# jak funguje a jak vytvorit image s entrypointem.



V Kubernetes porozumet co je
# Deployment, Pod,
# jak funguje volume a mounteni v podech (ConfigMap, Secret, PersistentVolumes).

U protobufu staci imho projet zakladni tutorial na syntax a
vedet jak vypada vygenerovany c++ kod.

Gitlab-CI asi v tuhle chvili asi neres, jelikoz jde vlastne jen o
pousteni commandu v Docker containeru.
A nema moc cenu to ted studovat,
kdyz jeste nemas pristup do firemniho Gitlabu.

Aby toho ale nebylo malo, tak jeste neco prihodim :)

Jako build system pouzivame GN (https://gn.googlesource.com/gn/), ktery pouziva Chromium.

Takze projit si prezentaci (
https://docs.google.com/presentation/d/15Zwb53JcncHfEwHpnG_PoIbbzQ3GQi_cpujYwbpcbZo/edit?usp=sharing) a
Quick Start Guide (https://gn.googlesource.com/gn/+/master/docs/quick_start.md)
te urcite take nemine.
https://www.youtube.com/watch?v=QVZa7QbMix8
https://www.chromium.org/developers/gn-build-configuration
https://gn.googlesource.com/gn/+/HEAD/docs/quick_start.md#Setting-up-a-build #build tutorial






https://www.youtube.com/watch?v=bmxr75CV36A
https://bugs.chromium.org/p/chromium/issues/detail?id=611087




V posledni rade, nevim jak si na tom se znalosti aktualnich standardu C++,
takze se pripadne koukni co se od dob kdy jsi pouzival C++ zmenilo
(momentalne pouzivame C++11 a prechod na C++17 je na spadnuti).
Neni treba znat vsechny nove featury, protoze stejne vetsinu z nich nepouzivame,
ale urcite je dobre mit o nich prehled.




/*========================================================================*/
intsll python on ubuntu

add-apt-repository
apt-get install ppa:deadsnakes/ppa


/*========================================================================*/
https://www.youtube.com/watch?v=EpNpGI2f1_I&feature=youtu.be


/*========================================================================*/
miko typs

https://www.youtube.com/watch?v=kuIxFzrRBZw
Moderní nástroje pro příkazovou řádku (Jakub Vokoun)

linux desktop on windows
https://medium.com/@japheth.yates/the-complete-wsl2-gui-setup-2582828f4577

Microsoft PowerToys
https://github.com/microsoft/PowerToys



fzf --preview 'head -100 {}'

tabulkové formáty na příkazovou
www.fisidata.org

nice code
https://www.youtube.com/watch?v=PySLIy7Klts

docker videa
https://www.youtube.com/watch?v

/*========================================================================*/



/*====================================================================*/
root@1923fc09e643:/ws/gn/examples/simple_build/out/default# ./hello
Hello, world


/*========================================================================*/
michal-kocanrdle@kocandrle-m:~$ tmux new -s vim -d
michal-kocanrdle@kocandrle-m:~$ tmux send-keys -t vim 'vim' C-m
michal-kocanrdle@kocandrle-m:~$ tmux attach -t vim



==============================================================================
miko dump
dump -vvv -D ./documents.5 -u sites -W ./words.hash2word -d -t wb ./words > words_out.txt

dump -t qsb 2 > site_data.txt


dump -D documents.5 -W words.hash2word -t wb words > ../words.txt
dump -D documents.5 -W words.hash2word -t wb words
dump -h
dump -D ./data/documents.5 -W ./data/words.hash2word -d -t wb ./data/words
dump -D ./barrel_d/documents.5 -u 4549914e08c954c0 -W ./data/words.hash2word -d -t wb ./data/words
dump -D ./barrel_d/documents.5 -u 1ed4493194f51334 -W ./data/words.hash2word -d -t wb ./data/words > words_out.txt
dump -t qub /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/1 >> qub.txt
dump -t qut /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/url_total.idx > qub.txt
dump -D ../barrel_d/documents.5 -t qsb /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qs/1
dump -D ../barrel_d/documents.5 -t qsbt /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qs/site_total.idx
dump -t qsb /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qs/1 >> qsb.txt
dump -t qsbt /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qs/site_total.idx > qsb.txt
dump -t qub /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/1 > qub.txt
dump -t qsb /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qs/1 > qsb.txt
dump -t qsb /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qs/1
dump -t qut /home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/url_total.idx

==============================================================================
http://harelba.github.io/q/

==============================================================================
https://www.ceskatelevize.cz/ivysilani/10430569360-gottland/213562269910004-misto-stalina/titulky
==============================================================================
miko sqlite

-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_ent rename COLUMN field1 to token_hash;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_ent rename COLUMN field2 to enb_hash;
-- Result: query executed successfully. Took 2ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_ent rename COLUMN enb_hash to ent_hash;
-- Result: query executed successfully. Took 0ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_ent rename COLUMN field3 to frequency;
-- Result: query executed successfully. Took 0ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_ent rename COLUMN field4 to entity;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_ent rename COLUMN field5 to avro_file_id;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_token rename COLUMN field1 to token_hash;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_token rename COLUMN field2 to token_hash_int;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_token rename COLUMN field3 to token_key_count;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_token rename COLUMN field4 to token;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_token rename COLUMN field5 to avro_file_id;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_url_tal rename COLUMN field1 to entity_hash;
-- Result: no such table: csv_url_tal
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_total rename COLUMN field1 to entity_hash;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_total rename COLUMN field2 to clicks;
-- Result: query executed successfully. Took 1ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_total rename COLUMN field3 to entity;
-- Result: query executed successfully. Took 2ms
-- EXECUTING ALL IN 'SQL 1'
--
-- At line 1:
alter table csv_total rename COLUMN field4 to avro_file_id;
-- Result: query executed successfully. Took 0ms


==============================================================================
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/csv_url_doc5.csv ./
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/csv_url_doc5.csv ./

/home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/csv_url_doc5.csv



docker hub

==============================================================================
nastarovat

oddel
install clangd
https://github.com/prabirshrestha/vim-lsp
https://github.com/mattn/vim-lsp-settings



!/home/michal-kocanrdle/.vim/plugged/vim-lsp-settings/installer/install-clangd.sh [running]

./clangd: error while loading shared libraries: libz3.so.4.8: cannot open shared object file: No such file or directory

sudo apt install -y libz3-4
sudo update-alternatives --install /lib/x86_64-linux-gnu/libz3.so.4.8 libz3.4.8 /lib/x86_64-linux-gnu/libz3.so.4 100
sudo aptitude install clang
sudo apt update
sudo apt install clang





1 /usr/bin/lsb_release
  2 Downloading clangd and LLVM...
  3   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
  4                                  Dload  Upload   Total   Spent    Left  Speed
  5   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  6 100  383M  100  383M    0     0  3337k      0  0:01:57  0:01:57 --:--:-- 5689k
!/home/michal-kocanrdle/.vim/plugged/vim-lsp-settings/installer/install-clangd.sh [finished]                                                                                               7,1            All
Installed clangd

start here
https://github.com/m-pilia/vim-ccls

continue here with project
https://github.com/MaskRay/ccls/wiki/Project-Setup






Tmux
Neovim
https://gitlab.seznam.net/opes/build/opes-gnbuild a
https://gitlab.seznam.net/opes/build/sluha
oddel

ipconfig /all.
V Linuxu použijte příkaz
ifconfig.
sudo apt install net-tools

miko linux dokumentace

http://mech.fd.cvut.cz/noticeboard/linux/ldp3.pdf

oddel
