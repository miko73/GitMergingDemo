
Ada lab prostředí in Wiki

miko oreily
https://www.oreilly.com
Login: Jan.sichrovsky@adastragrp.com
PW: Adastra_CZ_0064

https://teams.microsoft.com/l/entity/com.microsoft.teamspace.tab.wiki/tab::df4566af-ef07-4bd1-a36d-c4b1e6e344d4?context=%7B%22subEntityId%22%3A%22%7B%5C%22pageId%5C%22%3A2%2C%5C%22sectionId%5C%22%3A9%2C%5C%22origin%5C%22%3A2%7D%22%2C%22channelId%22%3A%2219%3A148e091a54d74b40b9744fd8ee625d91%40thread.skype%22%7D&tenantId=dd92f8ec-83fc-44c4-b277-1c4120fae21c

Uživatel: admin
Heslo: admin

Vše běží na Edge serveru: edge1.hadoop.local

scp edge1.hadoop.local:
scp Michal.Kocandrle@edge1.hadoop.local:/home/Michal.Kocandrle COMPANY.csv
scp debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/csv_url_doc5.csv ./



Pokud se připraví tunnely, tak lze služby dohledat:
miko api
miko restapi
miko adoki
Front-End: http://localhost:28088/admin/process-list
Swagger: http://localhost:28080/swagger

Kibana: http://localhost:25601/kibana/app/kibana_overview



miko DB
miko links

https://edge1.hadoop.local:8888/hue/editor/?type=impala


Testovaci databáze
DB type	URL	port	database	Username	Password	deployment
MariaDB 10.1.38	10.254.134.12	3306	offloader	offloader	majsikl	standalone

Oracle Express 11g	                  10.254.134.12	49161	xe	system	oracle	docker



Microsoft SQL Server 2017 14.00.3048	10.254.134.12	1433	master	sa	M4jkr0s0ft	docker
PostgreSQL 9.6	10.254.134.12	5432	offloader	offloader	oFFloader	standalone
DBMS: PostgreSQL (ver. 9.6.12)
Case sensitivity: plain=lower, delimited=exact
Driver: PostgreSQL JDBC Driver (ver. 42.2.5, JDBC4.2)
Ping: 16 ms
SSL: no



Teradata Express 15.10.00.07	10.254.134.164	1025	dbc	dbc	dbc	vbox

Sap Hana Express	10.254.134.12	39013	system	SYSTEM	S4P_HANICKA	docker


==============================================================================
miko tunelink
in Putty
in SSH -> Auth
   C:\install\Michal.Kocandrle.ppk
   file je ulozen v https://edge1.hadoop.local:7980/ v mem rootu


in SSH -> Tunnels
   Source port = 25601
   Destination  = edge1.hadoop.local:25601
      Add button
in SSH -> Tunnels
   Source port = 28088
   Destination  = edge1.hadoop.local:28088
      Add button
in SSH -> Tunnels
   Source port = 28080
   Destination  = edge1.hadoop.local:28080
      Add button

==============================================================================
miko at adastra WiFi


==============================================================================
in edge only
https://edge1.hadoop.local:8888


https://management.hadoop.local/datalab/#



cloudera datalab
https://management.hadoop.local:7183/cmf/hardware/hosts
https://management.hadoop.local:7183/cmf/login

tady jsem si uolzil vygenerovany
==============================================================================
miko DB
miko links
miko hadoop
miko hue

https://edge1.hadoop.local:7980/hue/filebrowser/view=/user/Michal.Kocandrle
na SQL ikonu tam je databaze impala
offloader_mirror

======================



http://localhost:28080/#/settings_user/login
response authnetication Bearer copy it to Authorize section button
=========================
miko adoki
Platformy Big Data
Hadoop (HDFS, Hive, Impala), ElasticSearch

datové zdroje
Oracle, MySQL, PostgreSQL, Microsoft SQL Server, Teradata, SAP HANA, Sybase

Stream
Kafka, RabbitMQ, ActiveMQ

Cloud
Microsoft Azure, AWS, Google Cloud


ADA
adalab_impala_basic

ETL proces extrakce, transformace a nahrání dat z jednoho či více zdrojů do datového skladu, nebo do datového tržiště.

Enterprise Data Warehouse (EDW)
Big Data Warehouse (BDW)
=============================
Swagger: http://localhost:28080/#/
login

access-control-allow-credentials: true
 access-control-allow-origin: http://localhost:28080
 access-control-expose-headers: *,Authorization,Content-Type
 authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7Im5hbWUiOiJhZG1pbiIsInJvbGVzIjpbImFkbWluIl19fQ.4sf2OeZKiRXABilJYb8xUUVcnEt7pNc4AP1wx5GqA4c
 connection: keep-alive
 content-length: 0
 date: Tue,18 May 2021 06:49:37 GMT
 referrer-policy: origin-when-cross-origin,strict-origin-when-cross-origin
 server: nginx/1.19.4
 vary: Origin
 x-content-type-options: nosniff
 x-frame-options: DENY
 x-permitted-cross-domain-policies: master-only
 x-xss-protection: 1; mode=block
 ==============================================================================
adoki process definition


Offload detail
From:system: adalab_mysqlschema: offloadername: address
To:system: adalab_cdhschema: offloader_mirrorname: mysql_offload_address



==============================================================================
miko git link
https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/KB-Offloader%20Team/_git/Ada-Offloader-Stack



==============================================================================
miko spark
https://spark.apache.org/docs/latest/configuration.html#dynamically-loading-spark-properties


tsf
definice loadu ktere se pouzivaji k pouziti ve swagru
https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/KB-Offloader%20Team/_git/Ada-Offloader-Stack

postman, na provolavani api

platforma
	system typ resource v ramci platformy
	connections
	memory
	time slot
connections
		SystemConnections


repository obsahuje scala zdrojaky k tomu API
offloader-api

cnf_scenario
		(configurace scenaru)
			dryRUN vystup se da nacpat do cnf_process




cnf_process
        (ukládá process)

mapping muze pretizit mapovani datovych typu

"sourceOffloadObjects": [{
    "connectionName": "adalab_mysql",
    "dataType": "table",       (table, file, nebo view.)
    "pathSchema": "offloader", (název databáze)
    "name": "address",         (nuzev tabulky)
    "priority": 1,				(optional pole, může sloužit k nastavení pořadí nahrávání tabulek, muže řešit integritu.)


     "columns": [
      {
        "name": "address_id",
        "dataType": "smallint",
        "ordinalPosition": 1,
        "properties": []     (primarni klic napřiklad)
      },{
        "name": "address",
        "dataType": "varchar(50)",
        "ordinalPosition": 2,
        "properties": []
      },{



properties
		parsovani parametru a specialnich options

"properties": [
      {
        "group": "object:cnf", (podle toho kde se properties vyutzivaj object:cnf jsou properties pro generator)
        "name": "target_connection_name",
        "value": "adalab_hive_kerb"
      },

{
        "group": "target:object:rdbms", (vrstvy, )
        "name": "statistics_flag", (uz to neni )
        "value": "true"
      }

t
Basic
Export
Mirror


empty head, neašla connection.

kibana ukaze více
		Dashboard = Manager Services

etl_controler

ETL_controler
		tady checkujeme jak procesy bezi

external lock
		zamky z venku

internal lock

	external lock
			run, recover

	externaljobname
			vlastni jmeno pro load

	properties
	        name: process_id
	        value
			vlastni parametry
					hodnoty ktere muzu nekam nacpat


	job cotroler state
			lock name stop zastaví

inteligaj od smart brains.
		komunitni edice

cnf_process
		split_by_hash na jdbc

offload objects

v json
		"relations"
source
		definice
target
		definice

source a destination name
priority
overide flag
name
datatype
originalposition

kdyz sloupec nema source jen target
hodnota je dana
		target expresion


cnf process process_name GET
		vytahnout si load


sekce META
		GET a POST
	 nasazuje process do produkce




==============================================================================
zdrojova connection
cilov connection
json na

cnf jsou rozpracovane
meta jsou produkcni

job_service neresit
incrmenty pozdeji






cnf_scenario
		napovedy pro scenare
=================================================================================

adalab_mysql_miko is stored in mysql_cdh_cust_process.json

=================================================================================
dryrun scenaryo

=================================================================================

process adoki monitoring
Job Service -> Adoki - Action Monitoring
=================================================================================
miko scenario
basic
 Scenario to set transfer from source to target.

 It can be used to prepare following scenarios:
 * Load File to File
 * Load Table to File
 * Load File to Table
 * Load Table to Table

 Options:
 General properties: GET /api/sys/property
 In addition to general properties this scenario supports following properties:
",

=================================================================================
mirror
"description": "
 Mirror scenario.

 Source data are saved into target stage from where they are saved to target database
 in defined form.
 This offload can be archived into target archive in form of snapshot.
 Archive table generates automatically snapshot column named pr_load_day or
 based on defined column name.

 Options:
 General properties: GET /api/sys/property
 In addition to general properties this scenario supports following properties:
",
=================================================================================
export

"description": "
 Scenario to safe export data.

 Data are moved from source into stage.
 When all data are collected it will then be moved to target.

 Options:
 General properties: GET /api/sys/property
 In addition to general properties this scenario supports following properties:
",

=================================================================================


adoki properties
      {
        "group": "object:cnf",
        "name": "overwrite_flag",
        "value": "false"
      },

       {
        "group": "target:object:rdbms",
        "name": "statistics_flag",
        "value": "true"
      },{
        "group": "target:object:bd",
        "name": "external_flag",
        "value": "true"
      },
      in
      {
        "group": "target:object:rdbms",
        "name": "session_end_statement",
        "value": "insert into table offloader_mirror.postgresql_offload_increment values ('muhaha', '2021-05-09 23:00:58.932', '2021-38-09 10:38:46', 11)"
      }

     {
        "group": "target:object:file",
        "name": "format",
        "value": "csv"
      },
      {
        "group": "target:object:file",
        "name": "timestamp_format",
        "value": "yyyy/MM/dd HH:mm:ss ZZ"
      }

    "mapping": {
      "time": ["string","timestamp"],
      "custom": ["varchar(5000)"],
      "date": ["string"]},

    "properties": [{
      "group": "source:object:rdbms",
      "name": "split_by_hash",
      "value": "true"


target
          {
            "target": {
              "name": "adoki_load_datetime",
              "dataType": "timestamp",
              "ordinalPosition": 8,
              "properties": []
            },
            "targetExpression": "date_format(current_timestamp(), 'yyyy-MM-dd HH:mm:ss')"
          }


======================================
adalab_mysql_to_hive_mirror

mirror scenario

=====================================
in process config
  scenario
  process
  offloadObjects
  relations
=====================================
in scenario config
  sourceOffloadObjects
    connectionName
    priority
    properties[]
    columns[]

  scenario

miko KB
https://web.microsoftstream.com/video/e09e66ba-2aaf-4627-adfa-7668a0f52c63

miko dokument DBPP_offload

na KB je
BDPP je big data produkční platforma
a Disovery platforma, neprodukční pro analytické využití

BDPP je big data produkční platforma
  z teradata an BDPP
90% loadu, který realizujeme je z Teradata datového skladu do BigData platformy
pomocí ADOKI

  scenář mirror
    5 až 6 k tabulek z TERADATA do stage ze STAGE se
      ukládají do ARCHIVU
      transformují do CORE
    pres STAGE a ARCHIVE do cílové
        CORE (core je mirror produkce)

  automat si bere i změny zdrojových struktur a upravuje si svoje METADATA
    ARCHIVE např při změně sloupce udělá novou tabulku
    na core se udělá tabulka s novu strukturou

  Scénáře a paterny
    PATERNY
      některá data se dají zahodit,
      někde ne a je to složitější.

miko kb
https://web.microsoftstream.com/video/e09e66ba-2aaf-4627-adfa-7668a0f52c63
KB systemy
  Fenix monitoring loadu dat
    ODWH operační datový sklad.
      co se s čím loaduje a co na něm závisí
      popisuje struktury a vztahy v jejich datech.
ADOKI komunikuje s ODWH pres restapi
      DYNAMIT dynamická transformace
        udržuje KB METADATOVY SKLAD
          METADATOVY SKLAD
            popis všech datových struktur
              hlavně Teradata metadat
              ale i všechna další metadata a popis souvislostí
              do budoucna by DYNAMIT měl ukládat do METADATA skladu metadata z ADOKI

        dynamit ovládá adoky a výsledky zapisuje do ODWH

ADOKI ukládá data do HAIV jsou pak přístupná z IMPALY
souborové ukládání dat
  Haiv vezme soubor a promítne ho jako tabulku.
  nejde updatovat řádek
BIGDATA
no hadoopu
hive
v komerčce nastavit JAVU (export java_home)
miko kerberos
kinit -kt Michal.Kocandrle.keytab Michal.Kocandrle
po kinit je ticket uloženej na serveru
  /tmp/krb5cc_1512851902
klist
kdestroy




miko login

kinit -kt Michal.Kocandrle.keytab Michal.Kocandrle
bash-4.2$ kinit -kt Michal.Kocandrle.keytab Michal.Kocandrle
bash-4.2$ hive
WARNING: Use "yarn jar" to launch YARN applications.
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/cloudera/parcels/CDH-6.2.0-1.cdh6.2.0.p0.967373/jars/log4j-slf4j-impl-2.8.2.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/cloudera/parcels/CDH-6.2.0-1.cdh6.2.0.p0.967373/jars/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]

Logging initialized using configuration in jar:file:/opt/cloudera/parcels/CDH-6.2.0-1.cdh6.2.0.p0.967373/jars/hive-common-2.1.1-cdh6.2.0.jar!/hive-log4j2.properties Async: false

WARNING: Hive CLI is deprecated and migration to Beeline is recommended.

quit;


====================================================



kerberos je sprava práv.
dostaneš ticket který ti umožňuje vstupy na platformu.
každý ticket je validní na 24 hodin

kilist vypíše parametry
/tmp/

miko hadup
distributed filesystem
hdfs dfs -ls /user/hive/warehouse/offloader_mirror.db

 hdfs dfs -ls /user/hive/warehouse/offloader_mirror.db/miko_test

hive nejdříve utentikuje
Beeline je nove

map reduce
  http://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
  distribuovaný engine
    map reduce (pripraví platná data ze všeho možnáho)

HIVE spustí javu a ta my ze souborů poskládá odpověď na select.

BIGDATA při ukládání velkých souborů

hdfs hadup distributed file system.
  všechny soubory které jsou používané z HIVE

na bigdata platformě jsou tabulky reprezentované jako directory struktury.
data jsou dále dělená do partitions.
  partitions jsou podsložky.
když se nastaví partitioning vytvořej se pro sloupečky podsložky.
cílem je minimalizovat počet tabulek do kterých se ukládá.


miko impala
in memory engine pro hive
on claudera -> Instances use only (Impala Daemon) hosts

impala-shell --protocol='hs2-http' --ssl -i "tpcds-impala.your_company.com:443"

beeline -n barney -p bedrock -u
"jdbc:hive2://edge1.hadoop.local:10000;AuthMech=1;KrbHostFQDN=edge1.hadoop.local;KrbServiceName=hive;KrbAuthType=1"


jdbc:hive2://m1.hdp.local:10010/<db>"


impala-shell -i worker2.hadoop.local

jmeno server zjistime na CLAUDERA manageru.
hledam impalu
  Impala Demon servery tam to bezi.
use offloader_mirror:




impala je při prvním dotazu pomalá, pak je rychlá, jestliže chceme z

invalidate metadata table_name (synchronizace)
refresh table_name
  refreshuje data z hive v impale

show table table_name;

show create table table_name;

při změně pdkladových dat udělat refresh.
  refresh table_name



 na BIGDATECH external table nemá nic
u external tabulek drop table nezp
[worker2.hadoop.local:21000] michal_kocandrle> show create table offloader_mirror.postgresql_offload_increment;
Query: show create table offloader_mirror.postgresql_offload_increment
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| result                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CREATE EXTERNAL TABLE offloader_mirror.postgresql_offload_increment (

tabulky s externimi daty se zakladají jako EXTRENAL
tabulky které chceme jednoduše dropnout zakládat bez direktivy external.

HIVE a IMPALA mají sdílený metadata store, takže tabulky založené
do impaly se zobrazí i v HIVE a nopak.


impala je in memory engine pro haiv

HIVE je point of truth




V progresu se budou dávat ADOKI struktury do METADATOVÉHO SKLADU
to se teprve bude dělat
Adastra teamu zasahuje do DYnamitu a do Adoky matadat

impala je použitá pro analytická data
  dobrá na analytické funkce
  dotazovací jazyk SQL, je tam méně datových typ.



miko spark shell

spark-shell
   etl framework není to sql dá se dělat v
YARN je moderní kubernet pro BIGDATA,
     obsluhuje
prostudovat


miko Cloudera
management.hadoop.local:7183

sparks -> Instances


python pysparkshell

používat scalu, protože se dá ohýbat

pouštění SQL ve sparku

collect ve sparku vrací výsleky, uživately
frací jako kolekci
!!! nedají se zavolat collect na velká data
CTRL+D se odpojíš.
jak zapnout mutliline
psark paste mode
:paste
napíšu kód
a pak ho spustim na jednou
CTRL+D spustí řádky najednout

metoda show vrací top data.
všechno co
  spark si připravuje postup a pustí až když je to potřeba.
dají se nastavi i checkpointy.
složitější postupy se daj rozdělit do více checkpointů

kinitování

bash.
====================================================
miko doc

lnux tutorial
https://ryanstutorials.net/linuxtutorial/

bigdata
https://bigdataprogrammers.com/how-to-execute-scala-script-in-spark-submit-without-creating-jar/


hive
https://hive.apache.org/

implala
https://docs.cloudera.com/data-warehouse/1.2/querying-data/topics/dw-using-impala-shell.html

impala
https://ondemand.cloudera.com/courses/course-v1:HDP+HDP-ESS+HDP-123/course/

impala
https://www.tutorialspoint.com/impala/index.htm

sparks
https://spark.apache.org/docs/latest/quick-start.html

sparks sql
https://spark.apache.org/docs/latest/sql-programming-guide.html

====================================================
kvalitni Scala resource zdarma
  https://www.scala-exercises.org/

zajimave repo od lidi z Jumpshotu s knihovnami na server development
- vsechno ve scale a funkcnionalni
https://engineering.avast.io/introducing-scala-server-toolkit/


====================================================
Caues, vypada to, ze Elastic uvolnil nejake skoleni zdarma v dobe Covidu.
https://training.elastic.co/learn-from-home

====================================================
Tips & Tricks - How to get ready for AWS certifications - from David Šumský
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html

====================================================
miko hive
https://cwiki.apache.org/confluence/collector/pages.action?key=Hive

http://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html

https://cwiki.apache.org/confluence/display/Hive/Tutorial

sousta scriptů
miko hive
http://svn.apache.org/viewvc/hive/trunk/ql/src/test/queries/clientpositive/




bash-4.2$ kinit -kt Michal.Kocandrle.keytab Michal.Kocandrle
hive


hive> show databases;
OK
adam_macejka
adoki
adoki_mirror
airflow_test
.....
michal_kocandrle

hive> use michal_kocandrle;
OK
Time taken: 0.661 seconds

create table company_miko(id INT, name STRING, age INT, address STRING, salary DOUBLE)
row format delimited
  fields terminated by ','
stored as TEXTFILE;

create table company_miko(id INT, name STRING, address STRING, salary DOUBLE)
PARTITIONED BY(age INT)
row format delimited
  fields terminated by ','
stored as TEXTFILE;


 DESCRIBE EXTENDED company_miko;

ALTER TABLE company_miko RENAME TO firmy;



INSERT OVERWRITE TABLE page_view PARTITION(dt='2008-06-08', country='US')

upload file to hadoop
hadoop dfs -copyFromLocal c:/file_name.txt htfs:/user/Michal.Kocandrle/data


CREATE TABLE page_view(viewTime INT, userid BIGINT,
                page_url STRING, referrer_url STRING,
                ip STRING COMMENT 'IP Address of the User')
COMMENT 'This is the page view table'
PARTITIONED BY(dt STRING, country STRING)
STORED AS SEQUENCEFILE;


PARTITIONED BY(dt STRING, country STRING)
ROW FORMAT DELIMITED
        FIELDS TERMINATED BY '1'
STORED AS SEQUENCEFILE;

SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

LOAD DATA INPATH '/path/to/HDFS/dir/file.csv' OVERWRITE INTO TABLE DB.EXAMPLE_TABLE PARTITION (PARTITION_COL_NAME='PARTITION_VALUE');

INSERT OVERWRITE TABLE t1onhive
SELECT age
FROM company_miko;



set hive.resultset.use.unique.column.names=true;
load data inpath '/user/Michal.Kocandrle/data/COMPANY.csv' overwrite into table company_miko;

load data inpath '/user/Michal.Kocandrle/data/COMPANY.csv' overwrite into table company_miko PARTITION (AGE='25');


hive> load data inpath '/user/Michal.Kocandrle/data/COMPANY.csv' overwrite into table firmy
hive.resultset.use.unique.column.names=false PARTITION (AGE='25');
Loading data to table michal_kocandrle.company_miko partition (age=25)
setfacl: Permission denied. user=Michal.Kocandrle is not the owner of inode=/user/hive/warehouse/michal_kocandrle.db/company_miko/age=25
setfacl: Permission denied. user=Michal.Kocandrle is not the owner of inode=/user/hive/warehouse/michal_kocandrle.db/company_miko/age=25/COMPANY.csv
OK
Time taken: 2.652 seconds


create table tbl_id_part(id int)
partitioned by (year int) row format
delimited fields terminated by ',';

load data inpath '/user/impala/data/id.txt' into table tbl_id_part partition(year=2010);


====================================================
hive -S
--hiveconf hive.cli.print.header=true
--hiveconf hive.resultset.use.unique.column.names=false
--database Mydatabase
-e 'select * from Mytable limit 0;' > /LocalPath/table.csv

====================================================

miko impala
impala-shell -i worker2.hadoop.local


bash-4.2$ impala-shell -i worker1.hadoop.local
Starting Impala Shell without Kerberos authentication
Opened TCP connection to worker1.hadoop.local:21000
Error connecting: TTransportException, TSocket read 0 bytes
Kerberos ticket found in the credentials cache, retrying the connection with a secure transport.
Opened TCP connection to worker1.hadoop.local:21000
Connected to worker1.hadoop.local:21000
Server version: impalad version 3.2.0-cdh6.2.0 RELEASE (build edc19942b4debdbfd485fbd26098eef435003f5d)
***********************************************************************************
Welcome to the Impala shell.
(Impala Shell v3.2.0-cdh6.2.0 (edc1994) built on Thu Mar 14 00:14:35 PDT 2019)

Want to know what version of Impala you're connected to? Run the VERSION command to
find out!
***********************************************************************************

openssl req -config “C:\Program Files\Git\usr\ssl\openssl.cnf” -x509 -nodes -days 365 -newkey rsa:2048 -keyout mykey.key -out mycert.pem
============================================
miko skoleni

Jakub Augustýn
https://web.microsoftstream.com/video/7119ab7d-0dfc-4318-b0f0-037f33d5c228

MD - documentation format
  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code
  more in
    https://github.com/search?q=adam-p%2Fmarkdown-here


DEMO_House_Prices


Introduction to Apache Spark Developer Training
https://web.microsoftstream.com/video/3dce546c-839f-4cd7-a4e9-94dfb517d58f



Adastra BASICS: Datové modelování 101 (Part 1) Bém
https://web.microsoftstream.com/video/95baa4ae-b228-4191-b943-406b7f6fca22
https://web.microsoftstream.com/video/293691b2-11b3-42e7-8a38-9b2b95f652eb

Workshop: PowerDesigner - časť 1.
https://web.microsoftstream.com/video/499563c3-df25-4849-9785-fcfa65f16cae

miko datové modelování
https://web.microsoftstream.com/video/aa04a3c2-249b-4a78-a243-5abecf9fe86f

====================================================
miko jupyter
in conda powershell
in appropriate folder

jupyter lab



====================================================
how to install scala on windows
miko scala

https://stackoverflow.com/questions/51895267/how-to-setup-spark-on-windows-10-step-by-step


====================================================

miko spark-shell
miko spark

bash-4.2$ kinit -kt Michal.Kocandrle.keytab Michal.Kocandrle
bash-4.2$ spark-shell

scala> spark.sql("show databases").collect().foreach(println)

:paste
  spark.sql("use offloader_mirror")
  spark.sql("show tables").collect().foreach(println)

scala> val table=spark.sql("select * from offloader_mirror.customer")
scala> table.show()

https://github.com/deanwampler/spark-scala-tutorial/blob/master/src/main/scala/sparktutorial/Intro1-script.scala

==============================================================================
https://docs.oracle.com/javase/8/docs
==============================================================================
miko sublime
https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/index.html
https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/extensibility/snippets.html
==============================================================================
miko which
(base) (venv) PS C:\adastra\projects\gs>
function which {
get-command $args[0]| format-list
}
(base) (venv) PS C:\adastra\projects\gs> which python


Name            : python.exe
CommandType     : Application
Definition      : C:\adastra\projects\gs\venv/Scripts\python.exe
Extension       : .exe
Path            : C:\adastra\projects\gs\venv/Scripts\python.exe
FileVersionInfo : File:             C:\adastra\projects\gs\venv/Scripts\python.exe
                  InternalName:     Python Console
                  OriginalFilename: python.exe
                  FileVersion:      3.8.8
                  FileDescription:  Python
                  Product:          Python
                  ProductVersion:   3.8.8
                  Debug:            False
                  Patched:          False
                  PreRelease:       False
                  PrivateBuild:     False
                  SpecialBuild:     False
                  Language:         Language Neutral


oddel

(base) (venv) PS C:\adastra\projects\gs>
==============================================================================

miko teradata
jdbc:teradata://10.254.134.164/DATABASE=dbc,DBS_PORT=1025,TYPE=FASTEXPORT

==============================================================================

