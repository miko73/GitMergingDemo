
==============================================================================
7.MikiPesto.3
You have exceeded the maximum login attempts. Please contact administrator.
==============================================================================
miko docházka
miko projekt

IINT001-002-047

## ==============================================================================


Pokud se připraví tunnely, tak lze služby dohledat:
miko api
miko restapi
miko adoki

local
  http://localhost:4200/admin/process-list


Front-End: http://localhost:28088/admin/process-list
Swagger: http://localhost:28080/swagger

Kibana: http://localhost:25601/kibana/app/kibana_overview

miko Cloudera
management.hadoop.local:7183



miko SQL
miko links
[16:14] Bem, Martin
    https://ls3dxfdqcdc8rsp-db202105221926.adb.eu-frankfurt-1.oraclecloudapps.com/ords/demo/_sdw/?nav=worksheet
​[16:14] Bem, Martin
    demo/AdastraAdastra123
         AdastraAdastra123

​[16:14] Bem, Martin
    demo1
​[16:14] Bem, Martin
    demo2
video

https://adastrabiz-my.sharepoint.com/personal/martin_bem_adastragrp_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmartin%5Fbem%5Fadastragrp%5Fcom%2FDocuments%2FRecordings%2F%C5%A0koleni%20SQL2%20%28Oracle%20SQL%29%20%2D%201%2D20210524%5F160139%2DMeeting%20Recording%2Emp4&parent=%2Fpersonal%2Fmartin%5Fbem%5Fadastragrp%5Fcom%2FDocuments%2FRecordings&originalPath=aHR0cHM6Ly9hZGFzdHJhYml6LW15LnNoYXJlcG9pbnQuY29tLzp2Oi9nL3BlcnNvbmFsL21hcnRpbl9iZW1fYWRhc3RyYWdycF9jb20vRVNRd0o1Qy16enBGaWxoYkozTlVselVCeDZfVEh0azJoaGhlR2tTajBjRFRNdz9ydGltZT0tV0NsY0dJZzJVZw

https://adastrabiz-my.sharepoint.com/:v:/r/personal/david_vavruska_adastragrp_com/Documents/Recordings/%C5%A0koleni%20SQL2%20(Oracle%20SQL)%20-%202-20210526_155338-Meeting%20Recording.mp4?csf=1&web=1&e=8Cgi05


miko impala
https://edge1.hadoop.local:8888/hue/editor/?type=impala

miko hive
https://edge1.hadoop.local:8888/hue/editor/?type=hive

==============================================================================
miko adalab_sftp
adoki_sftp / toJe1Prdel*

miko adalab_hdfs

hdfs:///user/hive/warehouse/

==============================================================================
URL
jdbc:hive2://edge1.hadoop.local:10000/offloader_mirror;AuthMech=1;KrbServiceName=hive;KrbHostFQDN=edge1.hadoop.local;KrbAuthType=1;


(base) PS C:\Users\michal.kocandrle> klist                                                                                                                                                         Ticket cache: API:krb5cc
Default principal: Michal.Kocandrle@DATALAB.ADASTRA.CZ

Valid starting       Expires              Service principal

15.06.2021 18:32:16  16.06.2021 18:32:16  krbtgt/DATALAB.ADASTRA.CZ@DATALAB.ADASTRA.CZ

kinit -t hdfs.keytab user/
kinit -kt Michal.Kocandrle.keytab Michal.Kocandrle/_HOST@ADASTRA.CZ



beeline -u 'jdbc:hive2://localhost:10000/offloader_mirror;principal=Michal.Kocandrle/DATALAB.ADASTRA.CZ@DATALAB.ADASTRA.CZ;auth=kerberos;kerberosAuthType=fromSubject' admin admin
beeline -u 'jdbc:hive2://edge1.hadoop.local:10000/offloader_mirror;principal=Michal.Kocandrle@DATALAB.ADASTRA.CZ' admin admin


beeline -u jdbc:hive2://localhost:10000 admin admin
beeline -u 'jdbc:hive2://localhost:10000/default;principal=hive/_HOST@COMPANY.COM'

jdbc:hive2://server:21050/default;principal=impala/server@REALM.COM;
auth=kerberos;kerberosAuthType=fromSubject

sudo kinit -kt /etc/security/keytabs/hive.service.keytab hive/host1.xxx.local@EXAMPLE:COM

sudo beeline -u "jdbc:hive2://host1.xxx.local:2181,host2.xxx.local:2181,host3.xxx.local:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2"

krbtgt/DATALAB.ADASTRA.CZ@DATALAB.ADASTRA.CZ


beeline -u 'jdbc:hive2://edge1.hadoop.local:10000/offloader_mirror;AuthMech=1;KrbHostFQDN=edge1.hadoop.local;KrbServiceName=hive;KrbAuthType=1;principal=hive/edge1.hadoop.local@DATALAB.ADASTRA.CZ' admin admin
beeline -u 'jdbc:hive2://edge1.hadoop.local:10000/offloader_mirror;principal=hive/DATALAB.ADASTRA.CZ@DATALAB.ADASTRA.CZ;auth=kerberos;kerberosAuthType=fromSubject' admin admin

jdbc:hive2://myhost.example.com:21050/;principal=impala/myhost.example.com@H2.EXAMPLE.COMMENT


principal=hive/_HOST@ADASTRA.CZ' admin admin

-Djava.security.krb5.debug=true
-Djava.security.krb5.conf="C:\Users\michal.kocandrle\krb5.conf"
-Djavax.security.auth.useSubjectCredsOnly=false

beeline -u 'jdbc:hive2://<HiveServer2Host>:10000/default;principal=hive/<HiveServer2Host>@<‌​KDC_Realm>' -f query.sql


beeline -u jdbc:hive2://edge1.hadoop.local:10000/offloader_mirror admin admin


beeline -n barney -p bedrock -u "jdbc:hive2://m1.hdp.local:10010/<db>"


jdbc:hive2://hivehost:10000/{database};AuthMech=1;KrbServiceName=hive;KrbHostFQDN=hivehost.region.sample.com;KrbAuthType=1;
jdbc:hive2://{host}:{port}/{database};AuthMech=1;KrbRealm=FOO.BAR;KrbHostFQDN={server}; KrbServiceName=hive;KrbAuthType=2

impala
jdbc:impala://worker1.hadoop.local:21050;AuthMech=1;KrbHostFQDN=worker1.hadoop.local;KrbServiceName=impala;KrbAuthType=1

jdbc:impala://worker1.hadoop.local:21050;AuthMech=1;KrbHostFQDN=worker1.hadoop.local;KrbServiceName=impala;KrbAuthType=1

miko DB

https://edge1.hadoop.local:8888/hue/editor/?type=impala


Testovaci databáze
DB type	URL	port	database	Username	Password	deployment

MariaDB 10.1.38	10.254.134.12	3306	offloader	offloader	majsikl	standalone

Oracle Express 11g	                  10.254.134.12	49161	xe	system	oracle	docker
system/oracle



Microsoft SQL Server 2017 14.00.3048	10.254.134.12	1433	master	sa	M4jkr0s0ft	docker

PostgreSQL 9.6	10.254.134.12	5432	offloader	offloader	oFFloader	standalone
DBMS: PostgreSQL (ver. 9.6.12)
Case sensitivity: plain=lower, delimited=exact
Driver: PostgreSQL JDBC Driver (ver. 42.2.5, JDBC4.2)
Ping: 16 ms
SSL: no



Teradata Express 15.10.00.07	10.254.134.164	1025	dbc	dbc	dbc	vbox

Sap Hana Express	10.254.134.12	39013	system	SYSTEM	S4P_HANICKA	docker
mysql
jdbc:mysql://10.254.134.12:3306/offloader?allowMultiQueries=true&useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC
offloader/majsikl


mssql sqlserver
sa/M4jkr0s0ft
jdbc:sqlserver://10.254.134.12:1433;databaseName=master
==============================================================================

miko python in adastra

https://adastrabiz-my.sharepoint.com/personal/dagmar_binova_adastragrp_com/_layouts/15/onedrive.aspx?originalPath=aHR0cHM6Ly9hZGFzdHJhYml6LW15LnNoYXJlcG9pbnQuY29tLzp2Oi9nL3BlcnNvbmFsL2RhZ21hcl9iaW5vdmFfYWRhc3RyYWdycF9jb20vRWFaMEZFbjFBOGhOdThMSG1pVXlUNkVCQzgwQVlZMkhNSkNUbnY5X25OM3FiZz9ydGltZT05bV9yemNnMzJVZw&id=%2Fpersonal%2Fdagmar%5Fbinova%5Fadastragrp%5Fcom%2FDocuments%2FRecordings



==============================================================================


Ada lab prostředí in Wiki

miko oreily
https://www.oreilly.com
Login: Jan.sichrovsky@adastragrp.com
PW: Adastra_CZ_0064

Python for DevOps: Learn Ruthlessly Effective Automation


https://teams.microsoft.com/l/entity/com.microsoft.teamspace.tab.wiki/tab::df4566af-ef07-4bd1-a36d-c4b1e6e344d4?context=%7B%22subEntityId%22%3A%22%7B%5C%22pageId%5C%22%3A2%2C%5C%22sectionId%5C%22%3A9%2C%5C%22origin%5C%22%3A2%7D%22%2C%22channelId%22%3A%2219%3A148e091a54d74b40b9744fd8ee625d91%40thread.skype%22%7D&tenantId=dd92f8ec-83fc-44c4-b277-1c4120fae21c

Uživatel: admin
Heslo: admin

Vše běží na Edge serveru: edge1.hadoop.local

miko hadoop

==============================================================================
F12 na frontendu ukazuje spojení a případně

adoky priorita mezi loady = určuje
adoky priorita mezi objekty = 0 njvět
==============================================================================
miko oracle
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
AdastrA.GrouP89

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

hadoop fs

hadoop fs -mkdir bdps/sample_files



\\
https://edge1.hadoop.local:7980/hue/filebrowser/view=/user/Michal.Kocandrle
na SQL ikonu tam je databaze impala
offloader_mirror

======================
install mysql-phpmyadmin.yml for the MySQL and phpMyAdmin
mkdir ~/DockerContain
vim mysql-phpmyadmin.mysql
version: '3.2'

services:
   db:
      image: mysql:8.0
      container_name: appsDB
      restart: always
      ports:
       - '6603:3306'
      environment:
        MYSQL_ROOT_PASSWORD: helloworld

   app:
      depends_on:
       - db
      image: phpmyadmin/phpmyadmin
      container_name: phpmyadmin
      restart: always
      ports:
       - '8080:80'
      environment:
        PMA_HOST: db

docker-compose -f mysql-phpmyadmin.yml up -d
docker ps

in explorer localhost:8080 root/helloworld

You can also access the Mysql from your MySQLWorkbench.
Hostname:localhost Port:6603 Username:root Password:helloworld
==============================================================================
ALTER USER 'root'@'localhost' IDENTIFIED BY 'helloworld';

==============================================================================
nefuguje
hadoop dfs -copyFromLocal C:\adastra\tut\hive\C.txt hdfs://edge1.hadoop.local:/user/Michal.Kocandrle/data

hadoop fs -ls -R hdfs://edge1.hadoop.local://home/Michal.Kocandrle


scp edge1.hadoop.local:

nefuguje
scp Michal.Kocandrle@edge1.hadoop.local:/home/Michal.Kocandrle/test.txt ./
scp -i C:\install\Michal.Kocandrle.ppk Michal.Kocandrle@edge1.hadoop.local:/home/Michal.Kocandrle/sftp_measurements.csv ./
scp -i C:\install\Michal.Kocandrle.ppk Michal.Kocandrle@edge1.hadoop.local:/home/Michal.Kocandrle/test.txt ./

<!-- scp  debian@miko-debian-dev.fulltext-dev.ko1.os.scif.cz:/home/debian/ftxt-indexer/out_linux/Debug/data/barrels/miko/barrel_qu/csv_url_doc5.csv ./ -->



http://localhost:28080/#/settings_user/login
response authnetication Bearer copy it to Authorize section button
=========================
miko adoki
master databáze mangeru na dastacku

mysql --host=127.0.0.1 --port=23306 -u root -p offloader_manager
Password admin
on local clinet configuration
127.0.0.1 Port 23306
 local Port 23306
 SSH -> use SSH tunel
 host edge1.hadoop.local
 port 22
 Local prot 23306
 Authentication : Key Payr Putty
 User Michal.Kocadnrle
 Private key C:\install\Michal.Kocandrle.ppk

Get-PSProvider -PSProvider Environment
Get-ChildItem -Path Env:\

$env:MYSQL_ROOT_PASSWORD='admin'
$env:MYSQL_USER='root'
$env:MYSQL_PASSWORD='admin'
$env:PMA_HOST='127.0.0.1'
$env:PMA_VERBOSE='adoki'
$env:PMA_PORT='23306'
$env:PMA_USER='root'
$env:PMA_PASSWORD='admin'



docker run --name phpmyadmin -d --link 127.0.0.1:offloader_manager -p 23306:23306
docker run --name root -d -e PMA_HOST=127.0.0.1 -p 23306:23306 phpmyadmin/phpmyadmin
docker run --name root -d --link "127.0.0.1:23306/offloader_manager" -p 8080:80 phpmyadmin/phpmyadmin


10.254.134.12




==============================================================================


jiné instance DB běží na jiných portech




tabulky popis
  etl_ přípravná verze metadata
  met_ metadata po deloy
  cnf_ configurace
    column property (specifická data mimo relační model.)
    object property (specifická data mimo relační model.)
      obcně jsou to vlastnosti specifické pro jednotlivá řešení, které jiná řešení nemají
      slouží také pro uložení nějakých specifických parameterů.
        group a name poisné evidenční sloupčky
prioiry je použitá v mysql_hive_basic_scenario.json
priorita procesu je něco jiného.

master DB ADKOI manageru mysql --host=127.0.0.1 --port=23306 -u root -p offloader_manager
petr hrabec nasatzuje

Marcel dělá migrační skripty.

source condition (nastavení subselektu)

v met_ tabulkách se drží i historické struktury loadovaných tabulek, dají se tam vysledovat i změny.
valid_to NULL znamená platnou verzi tabulky

v cnf se nasmí mazat aby byla zachována

metadata_sync_version (záznamy)
sys_log (logy ze synchronizace)

sys_property nastavení adoki
sys_system claoudera connections.
sys_system_connections definice připojení
sys_connection_property vlastnosti užívané v připojeních.
sys_predicata_settings definice incrementů
  u incrementů se přidávají data podle value v nějkém sloupečků.
  operator je where podmínka pro definici incrementu
  v KB 20 predikátů většinou podle data typů
  použití v definici sloupce ve scénáři přidáme predicate a "podmínků"
  increment se dá udělat i jinak, třeba se fixně generuje
  etl_job_controler
    external_lock
    incremental_lock
    last_runtime
  když se job zapne
    run 9009
class manager
  dokud se job nespustí, manager se snaží o spuštění
  offloader.manager.reading.JobLoader
  worker process se dá spustit i na claoudu, aby to bylo blízko datům
etl_action
  ve chvíli kdy se nastartuje je vyplněn started_at
  estimat_size

check point je místo kam až se došlo, v historii akcí je možné hledat, jak se v akcích posunuly checkopinty.
action set (popis prováděné akce)
  create
  offload
  statistics

etl_statistics
  statistiky o průběhu loadu.


MariaDB
  database
    job service

docker ps na edge1
docker log


  postman api metody do jsonů


    etl_job_proprty
==============================================================================










Platformy Big Data
Hadoop (HDFS, Hive, Impala), ElasticSearch


Datové zdroje
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
miko adoki process definition

described in  mysql_hive_address_8.json

      {
        "group":"target:object:rdbms",
        "name":"session_end_statement",
        "value": "insert into offloader_mirror.miko_test_target values($ROW_COUNT$, '$TARGET_SCHEMA$.$TARGET_NAME$', '$SOURCE_SCHEMA$.$SOURCE_NAME$', date_format(current_timestamp(), 'yyyy-MM-dd HH:mm:ss') );"
      }

miko adoki scenare

archive stage core
C:/adastra/resources/mysql_hive_metadata/mysql_hive_basic_scenario.json
   "properties": [
      {
        "group": "object:cnf",
        "name": "target_name",
        "value": "mysql_offload_rental"
      },
      {
        "group": "object:cnf",
        "name": "archive_name",
        "value": "mysql_offload_rental_snapshot"
      },{
        "group": "object:cnf",
        "name": "stage_name",
        "value": "mysql_stage_rental_snapshot"
      }
    ]

==============================================================================
,
      {
        "group": "object:cnf",
        "name": "target_load_time",
        "value": "adoki_load_date"
      }
==============================================================================


{
  "name": "postgresql_int_with_forward",
  "dataType": "int",
  "operator": "$predicate_column$ >= $predicate_value_min$",
  "minValue": "0",
  "description": "Int value where condition to use in Postgresql. Searches for equal and higher."
}
==============================================================================

Offload detail
From:system: adalab_mysqlschema: offloadername: address
To:system: adalab_cdhschema: offloader_mirrorname: mysql_offload_address



==============================================================================
miko git link
git clone --recurse-submodules https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/KB-Offloader%20Team/_git/Ada-Offloader-Stack
git clone https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/_git/Offloader-Manager



==============================================================================
miko spark
https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.3.4/bk_spark-guide/content/calling-udfs.html

https://spark.apache.org/docs/latest/configuration.html#dynamically-loading-spark-properties





tsf
definice miko git

https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/KB-Offloader%20Team/_git/Ada-Offloader-Stack

definice loadu ktere se pouzivaji k pouziti ve swagru
https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/KB-Offloader%20Team/_git/Offloader-Worker

Ada-Offloader-Service

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
miko clumn properties
C:\adastra\resources\03_teradata_hive_metadata\teradata_hive_basic_scenario.json
{
   58          "name": "address",
   59          "dataType": "varchar(50)",
   60          "ordinalPosition": 2,
   61:         "properties": [{
   62            "group": "column:rdbms",
   63            "name": "salt2",
   ..
   68          "dataType": "varchar(50)",
   69          "ordinalPosition": 3,
   70:         "properties": []
   71        }


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

miko hadoop
distributed filesystem
hdfs dfs -ls /user/hive/warehouse/offloader_mirror.db/




hdfs dfs -ls /user/Michal.Kocandrle
bash-4.2$ hdfs dfs -ls /user/Michal.Kocandrle
21/05/24 16:28:51 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Found 6 items
drwxr-x---+  - Michal.Kocandrle michal_kocandrle          0 2021-05-22 02:00 /user/Michal.Kocandrle/.Trash
drwxr-xr-x+  - Michal.Kocandrle michal_kocandrle          0 2021-05-18 10:27 /user/Michal.Kocandrle/.scratchdir
drwxr-x---+  - Michal.Kocandrle michal_kocandrle          0 2021-05-22 14:17 /user/Michal.Kocandrle/.sparkStaging
-rw-r--r--+  3 Michal.Kocandrle michal_kocandrle         79 2021-05-17 16:12 /user/Michal.Kocandrle/Michal.Kocandrle.keytab
-rw-r--r--+  3 Michal.Kocandrle michal_kocandrle       1438 2021-05-17 16:12 /user/Michal.Kocandrle/Michal.Kocandrle.ppk
drwxr-x---+  - Michal.Kocandrle michal_kocandrle          0 2021-05-24 15:49 /user/Michal.Kocandrle/data


hdfs dfs -copyFromLocal arrayfile.txt /user/Michal.Kocandrle/data
hdfs dfs -ls /user/Michal.Kocandrle/data
==============================================================================
[16:49] Bem, Martin
https://ls3dxfdqcdc8rsp-db202105221926.adb.eu-frankfurt-1.oraclecloudapps.com/ords/sql-developer

demo/AdastraAdastra123

==============================================================================


scp Michal.Kocandrle@edge1.hadoop.local:/home/Michal.Kocandrle/test.txt ./

scp -i C:\install\id_rsa.pub Michal.Kocandrle@edge1.hadoop.local:/home/Michal.Kocandrle/test.txt ./
scp -i C:\install\Michal.Kocandrle.ppk Michal.Kocandrle@edge1.hadoop.local:/home/Michal.Kocandrle/test.txt ./


ne
hadoop dfs -copyFromLocal C:\adastra\tut\hive\C.txt hdfs://edge1.hadoop.local://Michal.Kocandrle/data




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

miko external
tabulky s externimi daty se zakladají jako EXTRENAL, po dropu data zůstávají v BIGDATECH.
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
==============================================================================
miko spark-shell local
local spark is connected to
http://acz-c9vr8d3.adastracorp.net:4042/jobs/


spark batch processing Hadoop MapReduce
Structured data analysis spark
Machine Learning Analysis MLLib can be used for clustering
Interactive SLQ anslisis Impala
RealTime streaming data analysis : Storm library

scala> val hex=0x6;output - hex:Int =6
<console>:1: error: ';' expected but '=' found.
       val hex=0x6;output - hex:Int =6
                                    ^

scala> val hex=0x6;
hex: Int = 6

scala> val big=1.234
big: Double = 1.234

scala> val a='A'
a: Char = A
                             ^
scala> val hello="Hello world"
hello: String = Hello world

scala> println(""" Tady uvozovky "vole" tady """);
 Tady uvozovky "vole" tady

scala> object Test {
def main (args: Array [String]){
val it = Iterator("a", "b", "c", "d")
while(it.hasNext){
println(it.next())
}
}
}



====================================================
show create table `offloader_mirror`.`miko_test_target_4`;


CREATE TABLE `offloader_mirror.miko_test_target_4`(
`c1` smallint,
`s2` string,
`gen_targ_name` string,
`adoki_load_datetime` string)
ROW FORMAT SERDE
'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
'hdfs://nameservice1/user/hive/warehouse/offloader_mirror.db/miko_test_target_4'
TBLPROPERTIES (
'parquet.compress'='snappy',
'transient_lastDdlTime'='1623056463')

==============================================================================
hive> describe offloader_mirror.miko_test_target_4;
OK
c1                      smallint
s2                      string
gen_targ_name           string
adoki_load_datetime     string
Time taken: 0.576 seconds, Fetched: 4 row(s)
hive> describe formated offloader_mirror.miko_test_target_4;
FAILED: SemanticException [Error 10001]: Table not found formated
hive> describe formatted offloader_mirror.miko_test_target_4;
OK
# col_name              data_type               comment

c1                      smallint
s2                      string
gen_targ_name           string
adoki_load_datetime     string

# Detailed Table Information
Database:               offloader_mirror
OwnerType:              USER
Owner:                  Petr.Hrabec
CreateTime:             Mon Jun 07 11:01:03 CEST 2021
LastAccessTime:         UNKNOWN
Retention:              0
Location:               hdfs://nameservice1/user/hive/warehouse/offloader_mirror.db/miko_test_target_4
Table Type:             MANAGED_TABLE
Table Parameters:
        parquet.compress        snappy
        transient_lastDdlTime   1623056463

# Storage Information
SerDe Library:          org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe
InputFormat:            org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat
OutputFormat:           org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat
Compressed:             No
Num Buckets:            0
Bucket Columns:         []
Sort Columns:           []
Time taken: 0.141 seconds, Fetched: 28 row(s)


alter table offloader_mirror.miko_test_target_4 rename to michal_kocandrle.miko_test_target_4;

alter table michal_kocandrle.miko_test_target_4
change column s2 s2 STRING
comment 'druhy sloupec string'
AFTER gen_targ_name;

hive> alter table michal_kocandrle.miko_test_target_4
    > change column s2 s2 STRING
    > comment 'druhy sloupec string'
    > AFTER gen_targ_name;
OK
Time taken: 0.168 seconds
hive> describe michal_kocandrle.miko_test_target_4;
OK
c1                      smallint
gen_targ_name           string
s2                      string                  druhy sloupec string
adoki_load_datetime     string
Time taken: 0.106 seconds, Fetched: 4 row(s)

set hive.enforce.bucketing
==============================================================================
miko doc

miko teradata documentation
https://www.tutorialspoint.com/teradata/teradata_quick_guide.htm

adastra documentation
https://adastrabiz.sharepoint.com/sites/BigDatateam/Shared%20Documents/Forms/AllItems.aspx


bigdata
https://adastrabiz.sharepoint.com/sites/BigDatateam/Shared%20Documents/Forms/AllItems.aspx?viewid=cce868a5%2D6395%2D4b64%2Dbd23%2D794662b4fecf&id=%2Fsites%2FBigDatateam%2FShared%20Documents%2FVzd%C4%9Bl%C3%A1v%C3%A1n%C3%AD%2Fbig%5Fdata%5Fprednasky%5Fbelgie
https://bigdataprogrammers.com/join-in-spark-using-scala-with-example/
https://bigdataprogrammers.com/read-csv-file-spark-scala/


hadoop

https://adastrabiz.sharepoint.com/sites/BigDatateam/Shared%20Documents/Forms/AllItems.aspx?viewid=cce868a5%2D6395%2D4b64%2Dbd23%2D794662b4fecf&id=%2Fsites%2FBigDatateam%2FShared%20Documents%2FVzd%C4%9Bl%C3%A1v%C3%A1n%C3%AD%2Fbig%5Fdata%5Fprednasky%5Fbelgie%2F7%20%2D%20Hadoop%20and%20mapreduce%2Epdf&parent=%2Fsites%2FBigDatateam%2FShared%20Documents%2FVzd%C4%9Bl%C3%A1v%C3%A1n%C3%AD%2Fbig%5Fdata%5Fprednasky%5Fbelgie

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

r5EYm74N

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

cloudera top doc
https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.3.4/index.html

  DATA GOVERNANCE AND INTEGRATION
  Data Governance Guide
  Apache Flume User Guide
  Kafka Guide
  Hortonworks Connector for Teradata

spark guide
https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.3.4/bk_spark-guide/content/ch_spark-examples.html

hive performance tuning
https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.3.4/bk_performance_tuning/content/ch_hive_architectural_overview.html


miko hive
https://cwiki.apache.org/confluence/collector/pages.action?key=Hive

http://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html

https://cwiki.apache.org/confluence/display/Hive/Tutorial

miko hdfs
HDFS Administration
https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.3.4/bk_hdfs_admin_tools/content/ch01.html


sousta scriptů
miko hive
http://svn.apache.org/viewvc/hive/trunk/ql/src/test/queries/clientpositive/

==============================================================================



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
miko hadoop
hadoop dfs -copyFromLocal c:/file_name.txt htfs:/user/Michal.Kocandrle/data
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
setfacl: Permission denied. user=Michal.Kocandrle is not the owner of
inode=/user/hive/warehouse/michal_kocandrle.db/company_miko/age=25
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
miko video

interní videa s Marcelem
https://web.microsoftstream.com/video/e09e66ba-2aaf-4627-adfa-7668a0f52c63
https://web.microsoftstream.com/video/381c9024-7adb-4828-a93b-02868bbb69c8

mentor synchro
https://web.microsoftstream.com/video/fb93fddc-0b0b-44e1-86da-6bb2b3adaab8

targetExpression
https://web.microsoftstream.com/video/2c8a6479-3a1e-4cf7-8f90-1ce782de4687



Jakub Augustýn
https://web.microsoftstream.com/video/7119ab7d-0dfc-4318-b0f0-037f33d5c228

miko markdown
MD - documentation format
  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code
  more in
    https://github.com/search?q=adam-p%2Fmarkdown-here


DEMO_House_Prices


Adastra Klub: Úvod do Scaly
https://web.microsoftstream.com/video/c85e197f-2426-4ed3-b517-bf221f77472b?list=user&userId=beee7cb1-62f0-4261-8476-71a7c44a5d3e
Adastra Klub: Úvod do Scaly 2
https://web.microsoftstream.com/video/2bcb815c-d627-4d94-a97c-7a356df7f3e2?list=user&userId=beee7cb1-62f0-4261-8476-71a7c44a5d3e


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

=============================================================================

==============================================================================

how to install scala on windows
miko scala
pokročilé
scala packages
==============================================================================
file:///C:/Users/michal.kocandrle/OneDrive%20-%20Adastra,%20s.r.o/Documents/adastra/scala_tutorial.pdf
==============================================================================
how to install packages to scala environment

scala packaging
https://learning.oreilly.com/library/view/scala-cookbook/9781449340292/

==============================================================================


https://github.com/winitzki/talks/blob/master/scala-sbt/begin-sbt.md

==============================================================================
https://github.com/winitzki/talks/blob/master/scala-sbt/begin-sbt.md
https://www.youtube.com/watch?v=PDhOv4NMK-Y

==============================================================================

https://www.tutorialspoint.com/scala/scala_file_io.htm

https://docs.scala-lang.org/cheatsheets/index.html



https://www.scala-sbt.org/1.x/docs/offline/Combined+Pages.html#Build+definition

https://stackoverflow.com/questions/51895267/how-to-setup-spark-on-windows-10-step-by-step


cala doc
https://docs.scala-lang.org/tour/tour-of-scala.html



====================================================

miko spark-shell
miko spark

bash-4.2$ kinit -kt Michal.Kocandrle.keytab Michal.Kocandrle
bash-4.2$ spark-shell

scala> spark.sql("show databases").collect().foreach(println)



:paste
  spark.sql("use offloader_mirror")
  spark.sql("show tables").collect().foreach(println)

  spark.sql("use adoki")

spark.sql("insert into offloader_mirror.miko_test_target_1 values(3,'text 3', 'gen string 3', '08.06.2021' )")
val table=spark.sql("select * from offloader_mirror.miko_test_target_1")
table.collect().foreach(println)

scala> val table=spark.sql("select * from offloader_mirror.customer")
scala> table.show()

https://github.com/deanwampler/spark-scala-tutorial/blob/master/src/main/scala/sparktutorial/Intro1-script.scala

==============================================================================
miko sparks video https://web.microsoftstream.com/video/3dce546c-839f-4cd7-a4e9-94dfb517d58f
RDD resilient distributed dataset

akce
  count
  take
Transformace
  filter
  map
  reduce



==============================================================================
https://docs.oracle.com/javase/8/docs
==============================================================================
miko sublime
https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/index.html
https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/extensibility/snippets.html
==============================================================================
miko which
(base) (venv) PS C:\adastra\projects\gs>
function which {get-command $args[0]| format-list }

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
ssh -R 1025:localhost:1025 root@10.254.134.164
ssh -R 1025:localhost:22 root@10.254.134.164

ssh -R 10000:localhost:22 root@10.254.134.164


add ssh tunnel in putty
source port 1025 destination 10.254.134.164:1025
in connection string config
jdbc:teradata://localhost/DATABASE=dbc,DBS_PORT=1025
dbc/dbc

root/root
jdbc:teradata://10.254.134.164/DATABASE=dbc,DBS_PORT=1025,TYPE=FASTEXPORT

==============================================================================

miko SSH
C:\Users\michal.kocandrle>ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\michal.kocandrle/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\michal.kocandrle/.ssh/id_rsa.
Your public key has been saved in C:\Users\michal.kocandrle/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:8cDtFK+pW4oW8xFlOBcRl3T6CJ38CSr6Dy3y1nQ57EU adastracorpnet\michal.kocandrle@ACZ-C9VR8D3
The key's randomart image is:
+---[RSA 3072]----+
|         .==o..  |
|       .o.+*.+   |
|        +=+ B    |
|        .* = =E. |
|        S.*..o+  |
|      o..+. = .  |
|      o+++oo o   |
|      .=o*. .    |
|     ...=..      |
+----[SHA256]-----+

C:\Users\michal.kocandrle>cd .ssh

C:\Users\michal.kocandrle\.ssh>ls
==============================================================================

https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DyVnjMDq1Hy8%26t%3D14203s%26fbclid%3DIwAR3_fxdgWevB0aYog89eODKX6pUTZmOrKVnwZz87evK_ao4AodHg0gd0KGc&h=AT0y_K_ju-eLssHZwOxjYxx3gzy4MFKMRF-wZBIi9oowrGXNIX_csL3ZZGXRLiFyztI4uJ7uT1tttm8fFg8vgK4QJae90RZp4coFkv9FvaUt8lPI8v2KOue3WT_pSfgErUgPoB84goEEiIfa&__tn__=R]-R&c[0]=AT3rE1KzubqgL5mK5YWdnODP_mPO1W53nL4u98eG-GvKMnCe7ytQI-uv7-vrL5zGaRs8gktiqEOYbnfnpb8ydwlrwu1XIeRmElAmncauD-08qnR-z3gyubeidnUImNeIOzKK0X4ewSncUYLIDRxmxoMgMA8BFOmr1c4UBax3sJwnMUM
==============================================================================

==============================================================================

Google cloud

==============================================================================
AWS Jiří Zelenka
  denominátor = jmenná konvence
    access-control-model
  cloud formation infrastructure provisioning.
==============================================================================
ps -ef in windows
(base) PS C:\install> tasklist | findstr odp
odp.exe                      23684 Console                    1     16?532 K
==============================================================================
vaše přístupové údaje do vzdělávacího systému INSTRUCTOR jsou:
Uživatelské jméno: ACkocandrle
Heslo: mkoc35
==============================================================================


adoki_load_date string
co dělá kafka
jak monitorovat běžící joby?
statistics_flag ?
synchronizace hive a impaly ?
docker ps? nemám práva

dovolenou řešit s Petrem

==============================================================================
https://www.apachefriends.org/index.html

DBver
vmver pro teradata
retence dat
i
==============================================================================
miko retence

když má tabulka datumový sloupec udělelj retenci na 30 dní.
retence podle klíče = udržuj záznamy podle klíče
na jakých typech sloupců dává smysl nastavovat retenci?
jaká retenční pravidla by se dala aplikovat
  posledních n dnů
  posledních n hodin


udělat příklad provedení na nějaké datové tabulce;
zkontroluj retence a odmaž data



při retenci zvážit jestli jsou tam nějaká návazná data
  retenci bych udělal na základě souvisejícího loadu.
  Data v tabulkách bych neznačkoval jen datumem jako dnes,
  ale přidal bych vazbu na load, kterým data vstoupila do systému.
  Výmaz dat bych potom nabízel pomocí jednotlivých jobů,
  tam by se daly nastavit filtry podle vlastností jobu a řeklo by se smaž všechna data,
  která vstoupila do systému s tímhle loadem, nebo seznamem loadů.
  vlastně by se tam asi nemuselo nic extra přidávat

## jak nadefinovat seznam tabulek nad kterými se budou provádět retence
## jat na vazbu do stávajících struktur, asi podobně jako incrementy něco bude třeba doplnit.
## začít tím že udělám selekty řádků které by se měly mazat



## kdo to bude sledovat v adoki ?
## začnu na na nejjednodušší databázi sqlite a postupně přidávat funkcionalitu.

## zkusit nakonec zapracovat myšlenku s load_id, tabulku jednotlivých loadů a mazat to po celých loadech.


SELECT CONCAT('delete from ' , mps.path_schema ,'.', moo_target.name , ' where ' ,  sps.operator)
from etl_checkpoint ec
inner join sys_predicate_setting sps on sps.id = ec.sys_predicate_setting_id
inner join cnf_column_transformation cct on cct.id = ec.cnf_column_transformation_id
inner join meta_column_transformation mct on mct.cnf_column_transformation_id = cct.id
inner join meta_column mc_source on mc_source.id = mct.source_column_id
inner join meta_column mc_target on mc_target.id = mct.target_column_id
inner join meta_object_offload moo_source on moo_source.id = mc_source.object_offload_id
inner join meta_object_offload moo_target on moo_target.id = mc_target.object_offload_id
inner join meta_path_schema mps on moo_target.path_schema_id = mps.id;


-- SELECT ec.cnf_column_transformation_id, ec.sys_predicate_setting_id , sps.operator, sps.name, sps.data_type,
-- ec.sys_predicate_setting_id, ec.cnf_column_transformation_id, mct.cnf_column_transformation_id, mct.target_column_id,
-- mc_target.object_offload_id
-- SELECT *

SELECT CONCAT('delete from ' , mps.path_schema ,'.', moo_target.name , ' where ' ,  sps.operator)
from etl_checkpoint ec
inner join sys_predicate_setting sps on sps.id = ec.sys_predicate_setting_id
inner join cnf_column_transformation cct on cct.id = ec.cnf_column_transformation_id
inner join meta_column_transformation mct on mct.cnf_column_transformation_id = cct.id
inner join meta_column mc_source on mc_source.id = mct.source_column_id
inner join meta_column mc_target on mc_target.id = mct.target_column_id
inner join meta_object_offload moo_source on moo_source.id = mc_source.object_offload_id
inner join meta_object_offload moo_target on moo_target.id = mc_target.object_offload_id
inner join meta_path_schema mps on moo_target.path_schema_id = mps.id;


==============================================================================
miko adoki code notes
miko code notes
C:\adastra\Offloader-Worker\src\main\scala\com\adastragrp\offloader\worker\renderer


C:\adastra\Offloader-Worker\src\main\scala\com\adastragrp\offloader\worker\spark\dialect

C:\adastra\Offloader-Worker\src\test\scala\com\adastragrp\offloader\worker\
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        09.06.2021     15:24          11438 ActionTest.scala
-a----        09.06.2021     15:24           2223 ApiTest.scala
-a----        09.06.2021     15:24          19904 IntegrationTest.scala
-a----        09.06.2021     15:24           1389 MetadataTest.scala
-a----        09.06.2021     15:24          22841 RendererTest.scala
-a----        09.06.2021     15:24           2517 ScalaUtilsTest.scala
==============================================================================

==============================================================================
miko adoki data model

cnf_column_transformation obsahuje konfiguraci o převodech sloupců

==============================================================================
miko kafka
https://www.root.cz/clanky/pouziti-nastroje-apache-kafka-v-aplikacich-zalozenych-na-mikrosluzbach/#k02

https://www.root.cz/clanky/prace-s-kafkou-z-prikazove-radky-nastroje-kafkacat-a-kcli/#k01

přednáška BigData
https://cw.fel.cvut.cz/b201/courses/b0m33bdt/start

miko hadoop doc
https://cw.fel.cvut.cz/b201/_media/courses/b0m33bdt/b0m33bdt-3p.pdf

miko machine learning
https://docs.microsoft.com/en-us/azure/architecture/data-science-process/python-data-access

Vědecké zkoumání dat pomocí Scala a Spark v azure
https://docs.microsoft.com/cs-cz/azure/architecture/data-science-process/scala-walkthrough

Azure Architecture Center
https://docs.microsoft.com/cs-cz/azure/architecture/



==============================================================================
defnice tříd
C:\adastra\Offloader-API\src\main\scala\com\adastragrp\offloader\api\manager\dto\package.scala

/**
   * Shadow Column (Artifical Column Based on Expression)
   *
   * @param name            : column name
   * @param dataType        : column dataType
   * @param ordinalPosition : column position
   * @param layers          : shadow column layers list, where column is created example layers: [stage, target, archive]
   * @param expression      : column expression
   * @param predicate       : column is used in incrementing via predicate settings
   * @param properties      : column properties
   */
 /**
   * Column
   *
   * @param id              : column identificator
   * @param name            : column name
   * @param dataType        : column dataType
   * @param ordinalPosition : column position
   * @param predicate       : column is used in incrementing via predicate settings
   * @param properties      : column properties
   */
    /**
   * Offload Object Relation
   *
   * @param groupId               : relation groups id (equals the source object id on root)
   * @param groupScenarioName     : relations group scenario name
   * @param source                : source object
   * @param target                : target object
   * @param sourceConnectionName  : relation connection name for source
   * @param targetConnectionName  : relation connection name for target
   * @param sourceCustomConnectorName : custom connector name used as a reader/offloader
   * @param targetCustomConnectorName : custom connector name used as a writer/offloader
   * @param priority              : relation order when execution, starting from 0, default is 1
   * @param expectedSize          : relation expected size, options: small, medium, large, default is medium
   * @param sourceCondition       : where condition SQL to apply on source
   * @param overwriteFlag         : target overwrite
   * @param columnTransformations : sequence of column transformations
   */
 /**
   * Column Transformation
   *
   * @param source           : optional source column name
   * @param target           : target column name
   * @param targetExpression : column sql transformation
   */
   /**
   * Offload Schema List
   *
   * @param systemId       : system id
   * @param connectionId   : connection id
   * @param pathSchema     : schema name
   * @param pathSchemaType schema type options: "dir", "db", "topic", "other"
   */
    /**
   * System
   *
   * @param id                  : system id
   * @param name                : system name
   * @param system              : system type (platform type: cloudera, teradata, oracle, ... )
   * @param connections         : default maximal number of connections
   * @param memory              : default maximum memory
   * @param startAt             : default start time
   * @param endAt               : default end time

   * @param systemConnections   : SystemConnections class
   * @param systemResourcePools : SystemResourcePools class
   */
    /**
   * System connections
   *
   * @param id         : connection id (optional if not exists yet)
   * @param systemId   : system id
   * @param name       : system connection name
   * @param system     : system connection type (impala, hive, mysql, teradata, oracle, ...)
   * @param url        : connection url
   * @param hostname   : hostname if url is empty
   * @param port       : port if url is empty
   * @param username   : username to use
   * @param password   : password to use
   * @param properties : connection properties
   */

==============================================================================

miko kb



KB Stránky:
https://egate.kb.cz/
accounts in ODP

Jira - jira.kb.cz
Confluence (Wiki) - wiki.kb.cz
Feak (vykazování hodin) - feak.kb.cz
Itim (změna hesla) - itim.kb.cz
Service Manager (zde se žádá o it požadavky) - sm.kb.cz


https://jira.kb.cz/jira/secure/Dashboard.jspa
==============================================================================
LDAP (Lightweight Directory Access Protocol)




https://itim.kb.cz/itim/self/ChangeAccount.do
Kam jsem jezdil na tábor
Matka za svobodna
První adresa a čp
První auto ?
První dovolená s Evou?
BDP wiki

https://wiki.kb.cz
Hledej offloader
taky
https://wiki.kb.cz/confluence/display/DAMT/Data+Transport+documentation
https://wiki.kb.cz/confluence/display/BDPA/Access+Rights+Management#AccessRightsManagement-Typologierol%C3%AD
==============================================================================

https://jupyterhub.bdpp.kb.cz

najít si na wiki.kb.cz
P001_apim_dwh_wso2.txt ??
==============================================================================

podat podnět na prošetření nadměrného předepiosvání subsitučních preparátů.
revizní komise p5 tůmova
prověřit množství předepisované

"offloaderObjects": [
"id"
"systemName"
"pathSchema"
"name"
"locFlag"
"properties":[
{
  "group":"object:rdbms",
  "name":"deply_flag",
  "value": "false"
},
{
  "group":"object:rdbms",
  "name":"SALT2",
  "value": "cikbaseu"
},

{
  "group":"object:rdbms",
  "name":"SALT1",
  "value": "d213423423"
},
{
  "group":"object:rdbms",
  "name":"session_end_statement",
  "value": "update.[OLEG].[METADATA].[CIE_INT_DI_BATCH_CONTROL_IN] set record_count=$ROW_COUNT$, available_flag='Y' where table_name='DBD_CUSTOMER' and batch_code=(select max(batch_code) from [OLEG].[METADATA].[CIE_INT_DI_BATCH_CONTROL_IN] where Batch_Name='rads_to_oleg');"
},
]
]

dají se takto definovat
source
  session_init_statement
  session_end_statement
target
  session_init_statement
  session_end_statement





spark sql
"target_expresion":"sha2(concat(sha2(concat(party_id,'d234323k324234'), 384), 'cikbaseu', 384)"

==============================================================================
"scenario":{
  "scenarioName":"basic",
  "mapping":{
    "varchar\\((.+)\\)":[
      "navarchar($1)"
    ],
    "char\\((.+)\\)":[
      "nchar($1)"
    ]
  },
  "properties":[
    {
      "group":"object:cnf",
      "name":"target_connection_name",
      "value":"connectionstring"
    },
    {
      "group":"object:cnf",
      "name":"",
  ]
},
"sourceOffloadObjects":[
"connectionName":"val",
"pathSchema":"val",
"name":"v_name",
"dataType":"view",
"properties":[
{
  "group":"object:cnf",
  "name":"taget_path_schema",
  "value":"ksdlf.dbo"
},
{
  "group": "object:cnf",
  "name":"session_end_statement",
  "value":"insert into [MDWH_LO].[dbo].[IM_Log] ([process_id], [therad_id], [time_stamp], [..]) values ($PROCESS_ID$, NULL, current_timestamp, 'BDPP', $ROW_COUNT$, $SOURCE_SCHEMA$.$SOURCE_NAME$, $TARGET_SCHEMA$.$TARGET_NAME$, 0, DATEDIFF(SECOND, cast('$STARTED_AT$' as DateTiem2), 'service_offloader@SOS.KB.CZ', NULL, NULL))"
},
{}
]
]

==============================================================================
"column":[
  {
    "name":"payment_id",
    "dataType": "smallint",
    "ordinalPosition":1,
    "properties":[
      "target_expresion": "'$target_name$'"
      ]
  },
  {
    "name":"customer_id",
    "dataType": "smallint",
    "ordinalPosition":1,
    "properties":[
      "target_expresion": "'$process_id$'"
      ]
   }
    ]
  }
]
==============================================================================
"result": {
        "message": "Worker_18:-e-2021-06-07T14:31:38.648+02:00: due to truncated message [Cloudera][
        HiveJDBCDriver](500051) ERROR processing query/statement.
        Error Code: 40000, SQL state: TStatus(statusCode:ERROR_STATUS,
        infoMessages:[*org.apache.hive.service.cli.HiveSQLException:
        Error while compiling statement: FAILED:
        SemanticException No valid privileges\n User Petr.Hrabec does not have privileges for CREATETABLE\n The required privileges:
        Server=server1->Db=michal_kocandrle->action=create->grantOption=false;:17:16, org.apache.hive.service.cli.operation.Operation:toSQLException:Ope",
        "startTime": "2021-06-07T12:31:38.632Z",
        "endTime": "2021-06-07T12:31:39.421Z",
        "exitCode": 1,
        "applicationId": "application_1622800553462_40572"

==============================================================================
miko data_ananl
select ea.status, ea.started_at, ea.finished_at , ej.id, ej.external_id, ej.internal_id , ea.etl_action_id, eas.name, moo_target.name , mps_target.path_schema
from
etl_action ea
inner join etl_job ej on  ej.id = ea.etl_job_id
inner join etl_action_set eas on eas.id = ea.etl_action_set_id
inner join meta_object_offload_rel moor on ea.meta_object_offload_rel_id = moor.id
inner join etl_job_controller ejc on ej.etl_job_controller_id  = ejc.id
inner join meta_process mp on ejc.meta_process_id = mp.id
inner join meta_object_offload moo_target on moor.target_object_offload_id = moo_target.id
inner join meta_path_schema mps_target on moo_target.path_schema_id = mps_target.id
WHERE
mp.name = 'adalab_mysql_miko_4';
ORDER BY ID DESC;

select ea.status, ea.started_at, ea.finished_at , ej.id, ej.external_id, ej.internal_id , ea.etl_action_id, eas.name, moo_target.name , mps_target.path_schema
from
etl_action ea, etl_job ej, etl_action_set eas, meta_object_offload_rel moor, etl_job_controller ejc,
meta_process mp, meta_object_offload moo_target, meta_path_schema mps_target WHERE
ej.id = ea.etl_job_id
and eas.id = ea.etl_action_set_id
and ea.meta_object_offload_rel_id = moor.id
and ej.id = ea.etl_job_id
and ej.etl_job_controller_id  = ejc.id
and ejc.meta_process_id = mp.id
and moor.target_object_offload_id = moo_target.id
and moo_target.path_schema_id = mps_target.id
and mp.name = 'adalab_mysql_miko_4';

==============================================================================
select * from etl_action ea, etl_job ej , etl_job_controller ejc, meta_process mp where
ea.etl_job_id = ej.id
and ej.etl_job_controller_id  = ejc.id
and ejc.meta_process_id = mp.id
and mp.name like '%miko%';


==============================================================================
select mc_source.name, mc_target.name from
meta_column_transformation mct
, meta_column mc_source
, meta_column mc_target
, meta_object_offload moo_source
, meta_object_offload moo_tartget
WHERE
    mc_source.id = mct.source_column_id
and mc_target.id = mct.target_column_id
and moo_source.id  = mc_source.object_offload_id
and moo_tartget.id = mc_target.object_offload_id
and moo_tartget.name like '%sap_offload_film%';

==============================================================================
select moo_source.id, moo_source.name , mc_source.name, moo_tartget.id , moo_tartget.name , mc_target.name, mct.target_expression from
cnf_column_transformation mct
LEFT JOIN cnf_column mc_source on mc_source.id = mct.source_column_id
LEFT JOIN cnf_column mc_target on mc_target.id = mct.target_column_id
LEFT JOIN cnf_object_offload moo_source on moo_source.id  = mc_source.object_offload_id
LEFT JOIN cnf_object_offload moo_tartget on moo_tartget.id = mc_target.object_offload_id
WHERE
moo_tartget.name like '%mysql_miko_address_3%';
==============================================================================
select moo_source.id, moo_source.name , mc_source.name, moo_tartget.id , moo_tartget.name , mc_target.name, mct.target_expression from
meta_column_transformation mct
LEFT JOIN meta_column mc_source on mc_source.id = mct.source_column_id
LEFT JOIN meta_column mc_target on mc_target.id = mct.target_column_id
LEFT JOIN meta_object_offload moo_source on moo_source.id  = mc_source.object_offload_id
LEFT JOIN meta_object_offload moo_tartget on moo_tartget.id = mc_target.object_offload_id
WHERE
moo_tartget.name like '%mysql_miko_address_4%';
==============================================================================
select moo_target.name, mp.name from
meta_object_offload moo_target
inner join meta_object_offload_rel moor on moor.id = moo_target.id
inner join meta_process mp on mp.id = moor.process_id
where
moo_target.name like '%increment%';

==============================================================================
SELECT sp.`group` , sp.name , mop.value, sp.description from
sys_property sp
inner join meta_object_property mop on sp.id = mop.sys_property_id
where
sp.name != 'statistics_flag' ;
==============================================================================
miko predicate
miko checkpoint

SELECT * from etl_checkpoint ec
inner join sys_predicate_setting sps on sps.id = ec.sys_predicate_setting_id
inner join cnf_column_transformation cct on cct.id = ec.cnf_column_transformation_id
inner join meta_column_transformation mct on mct.cnf_column_transformation_id = cct.id
inner join meta_column mc_source on mc_source.id = mct.source_column_id
inner join meta_column mc_target on mc_target.id = mct.target_column_id
inner join meta_object_offload moo_source on moo_source.id = mc_source.object_offload_id
inner join meta_object_offload moo_target on moo_target.id = mc_target.object_offload_id
WHERE
moo_source.name like '%miko%' or moo_target.name  like '%miko%';

==============================================================================
==============================================================================
SELECT * from etl_checkpoint ec
inner join sys_predicate_setting sps on sps.id = ec.sys_predicate_setting_id
inner join cnf_column_transformation cct on cct.id = ec.cnf_column_transformation_id
inner join meta_column_transformation mct on mct.cnf_column_transformation_id = cct.id
inner join meta_column mc_source on mc_source.id = mct.source_column_id
inner join meta_column mc_target on mc_target.id = mct.target_column_id
inner join meta_object_offload moo_source on moo_source.id = mc_source.object_offload_id
inner join meta_object_offload moo_target on moo_target.id = mc_target.object_offload_id
WHERE
moo_source.name like '%miko%' or moo_target.name  like '%miko%';
==============================================================================
miko cnf_process
miko analyza
??? co dělá metadata_sync_version
??? co dělá sys_custom_connector

select count(*), ssc_target.name from
cnf_process cp
inner join cnf_object_offload_rel coor on cp.id = coor.process_id
inner join meta_process mp on mp.cnf_process_id = cp.id
inner join sys_system_connection ssc_source on coor.source_object_sys_system_connection_id = ssc_source.id
inner join sys_system_connection ssc_target on coor.target_object_sys_system_connection_id = ssc_target.id
inner join cnf_object_offload coo_source on coor.source_object_offload_id = coo_source.id
inner join cnf_object_offload coo_target on coor.target_object_offload_id = coo_target.id
group by ssc_target.name;

where cp.name='adalab_mysql_to_hive_basic';

<!-- where cp.name='adalab_mysql_to_hive_basic'; -->

select * from
meta_process mp
inner join cnf_process cp on mp.cnf_process_id = cp.id and mp.priority = cp.priority
inner join cnf_object_offload_rel coor on cp.id = coor.process_id
inner join sys_system_connection ssc_source on coor.source_object_sys_system_connection_id = ssc_source.id
inner join sys_system_connection ssc_target on coor.target_object_sys_system_connection_id = ssc_target.id
inner join cnf_object_offload coo_source on coor.source_object_offload_id = coo_source.id
inner join cnf_object_offload coo_target on coor.target_object_offload_id = coo_target.id
where mp.name='adalab_mysql_to_hive_basic';

==============================================================================






==============================================================================
CASE WHEN EXTRACT(MONTH FROM '$predicate_value_min$') = 1
AND EXTRACT(DAY FROM '$predicate_value_min$') = 1
THEN CASE WHEN EXTRACT (YEAR FROM $predicate_column$) = EXTRACT(YEAR FROM '$predicate_value_min$') -1
OR EXTRACT(YEAR FROM $predicate_column$) = 2999
THEN 1 ELSE 0 END ELSE CASE WHEN MONTHS_BETWEEN($predicate_column$,'$predicate_value_min$') <= 2
OR EXTRACT(YEAR FROM END_DATE) = 2999 THEN 1 ELSE 0 END END = 1





==============================================================================
##### Local SBT (non-docker) based development


==============================================================================
miko git
git clone --recurse-submodules https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/_git/Offloader-Service
==============================================================================
miko predicate
predicat se dfinuje na source tabulce

From:system: adalab_mysqlschema: offloadername: address
To:system: adalab_cdhschema: offloader_mirrorname: mysql_stage_address

==============================================================================
proč je
etl_checkpoint napojen pres cnf_column_transformation_id na cnf_column_transformation místo na meta_column_transformation

==============================================================================
miko db analýza
https://ceskepodcasty.cz/episode/EPTdKii6hFCLB7DGtis2


==============================================================================
miko Sbt

https://www.jetbrains.com/help/idea/sbt-support.html#sbt_structure

https://www.scala-sbt.org/1.x/docs/Getting-Started.html

[warn] Neither build.sbt nor a 'project' directory in the current directory: "C:\adastra\tut\scala"
c) continue
q) quit
?continue
c) continue
q) quit
?c
[info] [launcher] getting org.scala-sbt sbt 1.5.2  (this may take some time)...
[warn] No sbt.version set in project/build.properties, base directory: C:\adastra\tut\scala
[info] welcome to sbt 1.5.2 (Oracle Corporation Java 1.8.0_201-1-ojdkbuild)
[info] loading global plugins from C:\Users\michal.kocandrle\.sbt\1.0\plugins


==============================================================================
requester
https://docs.python-requests.org/en/master/

==============================================================================
miko teradata

CREATE SET TABLE offloader.film ,NO FALLBACK ,
     NO BEFORE JOURNAL,
     NO AFTER JOURNAL,
     CHECKSUM = DEFAULT,
     DEFAULT MERGEBLOCKRATIO
     (
      film_id DECIMAL(10,0) NOT NULL GENERATED ALWAYS AS IDENTITY
           (START WITH 1
            INCREMENT BY 1
            MINVALUE 1
            MAXVALUE 2147483647
            NO CYCLE),
      titul VARCHAR(255) CHARACTER SET LATIN NOT CASESPECIFIC NOT NULL,
      description VARCHAR(500) CHARACTER SET LATIN NOT CASESPECIFIC,
      release_year INTEGER DEFAULT NULL ,
      language_id SMALLINT NOT NULL,
      original_language_id SMALLINT DEFAULT NULL ,
      rental_duration SMALLINT NOT NULL,
      rental_rate DECIMAL(4,2) NOT NULL,
      delka SMALLINT DEFAULT NULL ,
      replacement_cost DECIMAL(5,2) NOT NULL,
      rating VARCHAR(10) CHARACTER SET LATIN NOT CASESPECIFIC,
      special_features VARCHAR(400) CHARACTER SET LATIN NOT CASESPECIFIC,
      last_update TIMESTAMP(6) NOT NULL,
      random_bigint BIGINT DEFAULT NULL ,
      random_float FLOAT DEFAULT NULL ,
      random_blob BLOB(2097088000))
PRIMARY INDEX ( film_id );






==============================================================================
miko lidi
Dagmar Binová
Jakub Augustýn
  Marcel Vrábel adoki lead

  Petr Hrabec Docker/devops
    od nás devops

  Jan Kodet KB admin
    Jirkovský Marek prcuje s Kodetem

  Miroslav Mráz KB koordinator
  Mark Litoš
  Jan Hřivna MT

teradata hash row buckety podle primárního indexu

row_id v teradatě
jak rozdělit obří tabulku
di_profit_item_bigdata
==============================================================================
miko kb lidi
  Petura Michal
  Korec Petr

==============================================================================
KB jiné týmy
  radek.nevyhosteny@adastragrp.com

  oleg.masajlo@adastragrp.com <oleg.masajlo@adastragrp.com>;

    datajka ??

  Vanda squad ??
  Honza Provaznik

Tomáš Sedloň
  azure
Tomáš Sedloň
  azure

Pavel Stejskal
  adastra guru azure atd.
  samostatný aplikační vývoj pro

POC Proof Of Concept

radek.nevyhosteny@adastragrp.com <radek.nevyhosteny@adastragrp.com>;

Jan Kodet
  adastra internal na

==============================================================================
miko presells

Plichta, Jan ???
  vyadá seniorně pracuje pro ČEZ
  dělá restapi, čte data z elastiku něco málo vyhledává
  caomda ??? engine ukládá do elastiku, přelévání dat
  pak přelejvat do datalake
  psalo se to java springboot ??
  používaání kafka
  openstack kubernetes reviewt
Plichta, Jan.sichrovsky@adastragrp.com

ČEZ interní materiály o dokerizaci to by mě zajímalo.


POC azure pro GŘC ???

==============================================================================
miko moje
  sleduj https://pyvo.cz/ projekt python komunita spousta knowledge

https://github.com/auto-mat

https://imysleni.cz/informaticke-mysleni/inspiromat/inspiromat-videa


==============================================================================

jar tvf hive-beeline-1.2.1000.2.5.4.2-7.jar


==============================================================================
miko powershell
How To Work with Environment Variables in PowerShell
https://mcpmag.com/articles/2019/03/28/environment-variables-in-powershell.aspx

Get-PSProvider -PSProvider Environment
Get-ChildItem -Path Env:\

$env:GOOGLE_APPLICATION_CREDENTIALS='C:\adastra\projects\gs\speech-test-300122-d4f7f5f35fc7.json'
==============================================================================
porada
  metadatova synchronizace v KB
    formou mysql procedury
    zpomaluje se na hledání změn v DB
  běží dlouho (vyhazuje user session po 10min)

  jak se používá kafka ????
    frontovací služba ??
    variantně RabbitMQ

  začít připravovat azure, prostředí
    Db v azure sqlserver
    v první fázi napojit managera na
    využít pro workera
    přenos na azure a cloud není por KB prioritou


==============================================================================
miko printer
miko office printer adastr

CZ_NORWAY_DCA3S
==============================================================================
rozchozeni vyvoje managera

examp

Adastří CA


Java (maven, sbt, atd.)

https://adastrabiz.sharepoint.com/sites/BigDataOffloader/Shared%20Documents/Development/adastraCA.zip - stáhnout a rozbalit. Ve stejném adresáři pustit skript, viz níže.

Aby bylo možné komunikovat se serverem https://repo.adastragrp.com, je potřeba označit certifikační autoritu, která vydala certifikát tomuto serveru (interní self-sign Adastra CA) za duvěryhodnou. Pro import Adastřího CA certifikátu do truststore každého JDK můžeš použít následující příkaz (CMD pustit jako administrátor):

FOR /D %i IN ("c:\Program Files\Java\jdk*") DO (
    "%i\bin\keytool" -importcert -file adastraCA.cer -keystore "%i\jre\lib\security\cacerts" -storepass changeit -alias "AdastraCA"
)
Na otázku Trust this certificate? [no] odpovědět yes.

V JDK 16 (možná i dříve) se adresářová struktura mírně změnila a je třeba příkaz upravit:

 "%i\jre\lib\security\cacerts" -> "%i\lib\security\cacerts"

==============================================================================
C:\adastra\cert\adastraCA>("c:\Program Files\Java\jdk1.8.0_291\bin\keytool" -importcert -file adastraCA.cer -keystore "c:\Program Files\Java\jdk1.8.0_291\jre\lib\security\cacerts" -storepass changeit -alias "AdastraCA" )
Owner: CN=Adastra Corporate Root CA
Issuer: CN=Adastra Corporate Root CA
Serial number: 1f0ae669c07df49f482b600221a0fc13
Valid from: Wed Sep 12 10:37:33 CEST 2007 until: Sat Jun 09 09:13:51 CEST 2035
Certificate fingerprints:
         SHA1: A2:9A:2B:B5:D2:4D:A5:E7:3F:B3:93:B7:5A:51:53:07:01:30:8A:2F
         SHA256: D2:A8:FA:63:31:1B:24:E3:C9:6C:4E:71:75:BD:78:D1:5E:AF:50:2F:FE:21:58:23:57:7B:12:50:80:5A:01:23
Signature algorithm name: SHA256withRSA
Subject Public Key Algorithm: 4096-bit RSA key
Version: 3

Extensions:

#1: ObjectId: 1.3.6.1.4.1.311.21.1 Criticality=false
0000: 02 01 01                                           ...


#2: ObjectId: 1.3.6.1.4.1.311.21.2 Criticality=false
0000: 04 14 5E 1F DA 75 C7 80   CD 60 7F BC 9C C9 83 50  ..^..u...`.....P
0010: 4E 51 24 D9 BB CF                                  NQ$...


#3: ObjectId: 2.5.29.19 Criticality=true
BasicConstraints:[
  CA:true
  PathLen:2147483647
]

#4: ObjectId: 2.5.29.15 Criticality=false
KeyUsage [
  DigitalSignature
  Key_CertSign
  Crl_Sign
]

#5: ObjectId: 2.5.29.14 Criticality=false
SubjectKeyIdentifier [
KeyIdentifier [
0000: 80 A5 49 9B A9 57 51 82   B4 D2 B0 12 E6 02 23 E1  ..I..WQ.......#.
0010: B6 93 B9 3C                                        ...<
]
]

Trust this certificate? [no]:  yes
Certificate was added to keystore
==============================================================================
in C:\adastra\Ada-Offloader-Stack
in APITest.scala

val host: String = sys.env.getOrElse("ADOKI_DOCKER_HOSTNAME", "localhost")

  val port: String = sys.env.getOrElse("ADOKI_MANAGER_UNSECURE_PORT", "9007")
  change to
  val port: String = sys.env.getOrElse("ADOKI_MANAGER_UNSECURE_PORT", "9009")

==============================================================================
in intelliJ
miko api development
Load sbt Changes Ctrl+Shift+O

in sbt-shell start Manager application by
run 9009


error]   not found: C:\Users\michal.kocandrle\.ivy2\localcom.adastragrp.scala.util\sbt-util_2.12\0.2.5\ivys\ivy.xml
[error]   download error: Caught javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target (PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target) while downloading https://repo.adastragrp.com/repository/scala-util/com/adastragrp/scala/util/sbt-util_2.12/0.2.5/sbt-util_2.12-0.2.5.pom
[error]   download error: Caught javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target (PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target) while downloading https://repo.adastragrp.com/repository/adastra-offloader/com/adastragrp/scala/util/sbt-util_2.12/0.2.5/sbt-util_2.12-0.2.5.pom
[error]   not found: C:\Program Files\JetBrains\IntelliJ IDEA Educational Edition 2021.1\plugins\Scala\repo\com.adastragrp.scala.util\sbt-util_2.12\0.2.5\ivys\ivy.xml
[error]   not found: https://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.adastragrp.scala.util/sbt-util_2.12/0.2.5/ivys/ivy.xml
[error]   not found: https://repo.typesafe.com/typesafe/ivy-releases/com.adastragrp.scala.util/sbt-util_2.12/0.2.5/ivys/ivy.xml
[warn] Project loading failed: (r)etry, (q)uit, (l)ast, or (i)gnore? (default: r)
==============================================================================
Adastří CA


Java (maven, sbt, atd.)

https://adastrabiz.sharepoint.com/sites/BigDataOffloader/Shared%20Documents/Development/adastraCA.zip - stáhnout a rozbalit. Ve stejném adresáři pustit skript, viz níže.

Aby bylo možné komunikovat se serverem https://repo.adastragrp.com, je potřeba označit certifikační autoritu, která vydala certifikát tomuto serveru (interní self-sign Adastra CA) za duvěryhodnou. Pro import Adastřího CA certifikátu do truststore každého JDK můžeš použít následující příkaz (CMD pustit jako administrátor):

FOR /D %i IN ("c:\Program Files\Java\jdk*") DO (
    "%i\bin\keytool" -importcert -file adastraCA.cer -keystore "%i\jre\lib\security\cacerts" -storepass changeit -alias "AdastraCA"
)
Na otázku Trust this certificate? [no] odpovědět yes.
V JDK 16 (možná i dříve) se adresářová struktura mírně změnila a je třeba příkaz upravit:
 "%i\jre\lib\security\cacerts" -> "%i\lib\security\cacerts"
C:\Program Files\Java\jdk-16.0.1\bin\
in
"C:\Program Files\Java\jdk-16.0.1\bin\
keytool -importcert -file "C:\adastra\cert\adastraCA\adastraCA.cer" -keystore "C:\Program Files\Java\jdk-16.0.1\lib\security\cacerts" -storepass changeit -alias "AdastraCA"
==============================================================================
mvn archetype:generate
scala
net.alchim31.maven:scala-archetype-simple
SampleApp
cz.kb.bd.base
==============================================================================
in XAMPP
-- SET Password=PASSWORD('');
-- GRANT ALL PRIVILEGES ON *.* TO `pma`@`localhost` WITH GRANT OPTION
==============================================================================

insert into offloader.miko_test_target values(
$ROW_COUNT$,
'$TARGET_SCHEMA$, $TARGET_NAME$', '$SOURCE_SCHEMA$.$SOURCE_NAME$', current_timestamp());

==============================================================================




9007 se da protunelovat
sipeckou nastartovat test.
P scénáři plní data do manageru
E zapínají load
ProcessServiceTest.scala

musím se vypnout SBT

==============================================================================
added followin local .env file to directory to get proper version to project
.env file added to C:\adastra\Ada-Offloader-Stack
# generated configuration - regenerated as a part of the compilation process. Generated at 2020-06-17T16:06:41.550

# Merged project-config.env and versions from submodules
ADOKI_CLIENT_ID=ada
ADOKI_SPARK_DEPENDENCIES_VERSION=1.0.55
ADOKI_OFFLOADER_DISTRIBUTOR_IMPL_VERSION=1-SNAPSHOT
ADOKI_SPARK_LIBS_VERSION=2.4.0-cdh6.2.0
ADOKI_SPARK_VERSION=2.4.0
ADOKI_OFFLOADER_MANAGER_VERSION=2.0.0.1-SNAPSHOT
ADOKI_OFFLOADER_LOGSTASH_VERSION=1.0.0
ADOKI_OFFLOADER_JOB_IMPL_VERSION=1.0.0.1-SNAPSHOT
ADOKI_OFFLOADER_JOB_API_VERSION=1.0.0
ADOKI_WORKER_VERSION=0.2.28
ADOKI_MANAGER_VERSION=0.1.4
DISTRIBUTOR_SCALA_VERSION=2.11.12
DISTRIBUTOR_BASE_IMAGE=bde2020/spark-base:2.4.0-hadoop2.7

# env-config.env and versions from submodules
# if you are not suer you can use host from ENV variable DOCKER_HOSTNAME
DOCKER_HOSTNAME=192.168.99.100


==============================================================================
error nebezi server na portu 9009

The future returned an exception of type: akka.stream.StreamTcpException, with message:
Tcp command [Connect(localhost:9009,None,List(),Some(10 seconds),true)]
failed because of Connection refused: no further information.
ScalaTestFailureLocation: com.adastragrp.offloader.APITest at (APITest.scala:37)
org.scalatest.exceptions.TestFailedException: The future returned an exception of type:
akka.stream.StreamTcpException, with message: Tcp command
[Connect(localhost:9009,None,List(),Some(10 seconds),true)] failed because of Connection refused:
no further information.


==============================================================================

Zone 40916 Stick FORCE AIR black/red 80cm R-20

==============================================================================
anonimizace, nemaskovaná čísla účtů ??
vead ??, přejmenování tabulek ???
Tom Kozárek (obsah offloadovných dat ??)
staré soubory obsahují prázdné řádky a
pormítají se potom do výslených tabulek v Hive a Impala

manager je přeplněn historickými metadaty ??
smallnewk
checkpointy se mapují na názvy objektů.
Když se nahraje proces bez tabulek, můžou zmizet checkopinty? asi ne, data tam
zůstanou, ale nejsou spojena s objekty,
objekty se musí jmenovat stejně

checkopinty ??

Sváťa a Maixner metadata team spojení Dynamitu
Nahrávání tabulek 3 až 4 dny.

==============================================================================
miko doc
hadop and hive

file:///C:/adastra/projects/BDT

https://learnxinyminutes.com/docs/scala/

create external table pocasi_tmp (
stanice string,
mesic int, den int, hodina int,
teplota double,
flag string,
latitude double, longitude double,
vyska double, stat string, nazev string)
ROW FORMAT
DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION "/user/username/teplota-usa/";

==============================================================================
# BDT
miko doc
CVUT FEL BDT course

## Useful links

* [Hive language manual](https://cwiki.apache.org/confluence/display/Hive/LanguageManual)
* [Apache Spark manual](https://spark.apache.org/docs/1.6.0/)
* [Metacentrum hadoop reference page](https://wiki.metacentrum.cz/wiki/Hadoop)
* [HDFS DFS commands](https://hadoop.apache.org/docs/r2.7.5/hadoop-project-dist/hadoop-common/FileSystemShell.html)
* [CSV files import/export](https://github.com/databricks/spark-csv)

* [PySpark SQL manual](http://spark.apache.org/docs/1.6.0/api/python/pyspark.sql.html)
* [Learn python in Y minutes](https://learnxinyminutes.com/docs/python3/)
* [Official python documentation](https://docs.python.org/3/)
* [Regular expressions at Ryan's tutorials](https://ryanstutorials.net/regular-expressions-tutorial/regular-expressions-basics.php)
==============================================================================

zápis 24.6
oleg?? testovací data
  kontaktní historie ???

INcidenty PDB z offloaderu

Fenix monitoruej provoz včetně provozu
kodet restartoval cluster a kvuli tomu to asi popadalo
nedostali se tam ani se sparkem, nagrantovali prava ?
  jestli je z toho nějaký zápis ??
  Udělat HC offloaderu ?? (Marek)
alka
  NULL pole neměla být NULL
  Michal Hroch ODVH, Dacan,

   ==============================================================================
   www.company.comZdroje:•http://hadoop.apache.org/
   •http://www.linuxexpres.cz/software/kdyz-se-rekne-hadoop
   •http://www.systemonline.cz/clanky/big-data.htm
   •http://www-01.ibm.com/software/data/infosphere/biginsights/
   •http://en.wikipedia.org/wiki/Hadoopa další odkazy zde nalezené
   ==============================================================================
miko partitioning in hive
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;
create temporary table michal_kocandrle.temp_us (txnno INT, txndate STRING, custno INT, amount DOUBLE, category STRING, product STRING, city STRING,state STRING, spendby STRING)
row format delimited fields terminated by ',' lines terminated by '\n' stored as textfile;

--deos not work
--load data local inpath '/user/Michal.Kocandrle/data/txns1.txt' into table temp_us;
-- works fine
load data inpath '/user/Michal.Kocandrle/data/txns1.txt' overwrite into table temp_us;


hdfs dfs -ls /user/Michal.Kocandrle/data

create table txnrecordspar1(txnno INT, txndate STRING, custno INT, amount DOUBLE, category STRING, product STRING, city STRING, spendby STRING)
partitioned by(state STRING) row format delimited fields terminated by ','
lines terminated by '\n' stored as textfile;

insert into table txnrecordspar1 partition(state)
select txnno,txndate,custno,amount,category,product,city,spendby,state from temp_us;

show partitions txnrecordspar1;



hive> show partitions txnrecordspar1;
OK
state=Alabama
state=Arizona
state=California
state=Colorado
state=Connecticut
state=District of Columbia
state=Florida
state=Georgia
state=Hawaii

bash-4.2$ hdfs dfs -ls /user/hive/warehouse/michal_kocandrle.db/txnrecordspar1/
21/06/25 08:51:23 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Found 38 items
drwxrwx--x+  - hive hive          0 2021-06-24 20:13 /user/hive/warehouse/michal_kocandrle.db/txnrecordspar1/state=Alabama
drwxrwx--x+  - hive hive          0 2021-06-24 20:13 /user/hive/warehouse/michal_kocandrle.db/txnrecordspar1/state=Arizona
drwxrwx--x+  - hive hive          0 2021-06-24 20:13 /user/hive/warehouse/michal_kocandrle.db/txnrecordspar1/state=California
drwxrwx--x+  - hive hive          0 2021-06-24 20:13 /user/hive/warehouse/michal_kocandrle.db/txnrecordspar1/state=Colorado
drwxrwx--x+  - hive hive          0 2021-06-24 20:13 /user/hive/warehouse/michal_kocandrle.db/txnrecordspar1/state=Connecticut
==============================================================================
miko azure
miko tutorials
miko azure tutorials
https://docs.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=powershell%2Cclone


start here
https://docs.microsoft.com/cs-cz/azure/

jednotlivé služby
  Azure App Service

tutorial python postgresql on azure
  https://docs.microsoft.com/cs-cz/azure/app-service/tutorial-python-postgresql-app?tabs=bash%2Cclone

1) smluva a účet na azure

2) az client application

3) install DB extension
      az extension add --name db-up

4) vytvoření skupiny prostředků
--resource-group Miko_tutorial_1

5) install posgres DB
      az postgres up --resource-group Miko_tutorial_1 --location westus2 --sku-name B_Gen5_1 --server-name MikoTestPsg1 --database-name pollsdb --admin-user miko --admin-password Loko.Koko.1 --ssl-enforcement Enabled

      (base) (venv) PS C:\adastra\projects\Python\djangoapp> az postgres up --resource-group Miko_tutorial_1 --location westus2 --sku-name B_Gen5_1 --server-name MikoTestPsg1 --database-name pollsdb --admin-user miko --admin-password Loko.Koko.1 --ssl-enforcement Enabled
Creating PostgreSQL Server 'MikoTestPsg1' in group 'Miko_tutorial_1'...
Creating PostgreSQL database 'pollsdb'...
Checking your ip address...
Configuring server firewall rule, 'devbox', to allow for your ip address: 88.100.229.101
If PostgreSQL server declines your IP address, please create a new firewall rule using:
    `az postgres server firewall-rule create -g Miko_tutorial_1 -s MikoTestPsg1 -n {rule_name} --start-ip-address {ip_address} --end-ip-address {ip_address}`
Configuring server firewall rule, 'azure-access', to accept connections from all Azure resources...
Successfully Connected to PostgreSQL.
Ran Database Query: `CREATE USER root WITH ENCRYPTED PASSWORD 'Pollsdb1'`
Ran Database Query: `GRANT ALL PRIVILEGES ON DATABASE pollsdb TO root`
{
  "connectionStrings": {
    "ado.net": "Server=mikotestpsg1.postgres.database.azure.com;Database=pollsdb;Port=5432;User Id=miko@MikoTestPsg1;Password=Loko.Koko.1;",
    "jdbc": "jdbc:postgresql://mikotestpsg1.postgres.database.azure.com:5432/pollsdb?user=miko@MikoTestPsg1&password=Loko.Koko.1",
    "jdbc Spring": "spring.datasource.url=jdbc:postgresql://mikotestpsg1.postgres.database.azure.com:5432/pollsdb  spring.datasource.username=miko@MikoTestPsg1  spring.datasource.password=Loko.Koko.1",
    "node.js": "var client = new pg.Client('postgres://miko@MikoTestPsg1:Loko.Koko.1@mikotestpsg1.postgres.database.azure.com:5432/pollsdb');",
    "php": "host=mikotestpsg1.postgres.database.azure.com port=5432 dbname=pollsdb user=miko@MikoTestPsg1 password=Loko.Koko.1",
    "psql_cmd": "psql --host=mikotestpsg1.postgres.database.azure.com --port=5432 --username=miko@MikoTestPsg1 --dbname=pollsdb",
    "python": "cnx = psycopg2.connect(database='pollsdb', user='miko@MikoTestPsg1', host='mikotestpsg1.postgres.database.azure.com', password='Loko.Koko.1', port='5432')",
    "ruby": "cnx = PG::Connection.new(:host => 'mikotestpsg1.postgres.database.azure.com', :user => 'miko@MikoTestPsg1', :dbname => 'pollsdb', :port => '5432', :password => 'Loko.Koko.1')",
    "webapp": "Database=pollsdb; Data Source=mikotestpsg1.postgres.database.azure.com; User Id=miko@MikoTestPsg1; Password=Loko.Koko.1"
  },
  "host": "mikotestpsg1.postgres.database.azure.com",
  "password": "Loko.Koko.1",
  "username": "miko@MikoTestPsg1"
}

(base) (venv) PS C:\adastra\projects\Python\djangoapp>

6) nasazení aplikace zazipuje aktuální adresář a sám to nasadí
az webapp up --resource-group Miko_tutorial_1 --location westus2 --plan DjangoPostgres-tutorial-plan --sku B1 --name MikoDjangoPGTutorial1

(base) (venv) PS C:\adastra\projects\Python\djangoapp> az webapp up --resource-group Miko_tutorial_1 --location westus2 --plan DjangoPostgres-tutorial-plan --sku B1 --name MikoDjangoPGTutorial1
>>
The webapp 'MikoDjangoPGTutorial1' doesn't exist
Creating AppServicePlan 'DjangoPostgres-tutorial-plan' ...
Resource provider 'Microsoft.Web' used by this operation is not registered. We are registering for you.
Registration succeeded.
Creating webapp 'MikoDjangoPGTutorial1' ...
Configuring default logging for the app, if not already enabled
Creating zip with contents of dir C:\adastra\projects\Python\djangoapp ...
Getting scm site credentials for zip deployment
Starting zip deployment. This operation can take a while to complete ...
Deployment endpoint responded with status code 202
You can launch the app at http://mikodjangopgtutorial1.azurewebsites.net
{
  "URL": "http://mikodjangopgtutorial1.azurewebsites.net",
  "appserviceplan": "DjangoPostgres-tutorial-plan",
  "location": "westus2",
  "name": "MikoDjangoPGTutorial1",
  "os": "Linux",
  "resourcegroup": "Miko_tutorial_1",
  "runtime_version": "python|3.7",
  "runtime_version_detected": "-",
  "sku": "BASIC",
  "src_path": "C:\\adastra\\projects\\Python\\djangoapp"
}
7) Nastavení parameterů pro propojení aplikace a databáze
(base) (venv) PS C:\adastra\projects\Python\djangoapp>
(base) (venv) PS C:\adastra\projects\Python\djangoapp> az webapp config appsettings set --settings DBHOST="MikoTestPsg1" DBNAME="pollsdb" DBUSER="miko" DBPASS="Loko.Koko.1"
[
  {
    "name": "SCM_DO_BUILD_DURING_DEPLOYMENT",
    "slotSetting": false,
    "value": "True"
  },
  {
    "name": "WEBSITE_HTTPLOGGING_RETENTION_DAYS",
    "slotSetting": false,
    "value": "3"
  },
  {
    "name": "DBHOST",
    "slotSetting": false,
    "value": "MikoTestPsg1"
  },
  {
    "name": "DBNAME",
    "slotSetting": false,
    "value": "pollsdb"
  },
  {
    "name": "DBUSER",
    "slotSetting": false,
    "value": "miko"
  },
  {
    "name": "DBPASS",
    "slotSetting": false,
    "value": "Loko.Koko.1"
  }
]

!!! when parameters are aset it's necessary to restart services

<!--
      az postgres up
      --resource-group Miko_tutorial_1
      --location westus2
      --sku-name B_Gen5_1
      --server-name MikoTestPsg1
      --database-name pollsdb
      --admin-user miko
      --admin-password Loko.Koko.1
      --ssl-enforcement Enabled
 -->

When deployed to Azure App Service,
the database connection information is specified
via environment variables
`DBHOST`,
`DBPASS`,
`DBUSER`, and
`DBNAME`.

8) spuštění migrace databáze Django

az webapp ssh
starts terminal session
something like

https://MikoDjangoPGTutorial1.scm.azurewebsites.net/webssh/host
https://mikodjangopgtutorial1.scm.azurewebsites.net/webssh/host
9) migrace tříd djanga v ssh na webu azure

# Run database migrations
python manage.py migrate

# Create the super user (follow prompts)
python manage.py createsuperuser
root/Pollsdb1
Pollsdb1

9) https://mikodjangopgtutorial1.azurewebsites.net
10) http://mikodjangopgtutorial1.azurewebsites.net/admin
11) in admin add vote questions
12) how to run app locally
    # Configure the Python virtual environment
    python3 -m venv venv
    source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt
    # Run Django migrations
    python manage.py migrate
    # Create Django superuser (follow prompts)
    python manage.py createsuperuser
    # Run the dev server
    python manage.py runserver

13) "Starting development server at http://127.0.0.1:8000/
14) Go to http:///localhost:8000/admin add questions
15) Redeploy the code to Azure
   az webapp up
      Webapp 'MikoDjangoPGTutorial1' already exists. The command will deploy contents to the existing app.
      Creating AppServicePlan 'DjangoPostgres-tutorial-plan' ...
      Creating zip with contents of dir C:\adastra\Projects\Python\djangoapp ...
      Getting scm site credentials for zip deployment
      Starting zip deployment. This operation can take a while to complete ...
      Deployment endpoint responded with status code 202
      You can launch the app at http://mikodjangopgtutorial1.azurewebsites.net
      {
        "URL": "http://mikodjangopgtutorial1.azurewebsites.net",
        "appserviceplan": "DjangoPostgres-tutorial-plan",
        "location": "westus2",
        "name": "MikoDjangoPGTutorial1",
        "os": "Linux",
        "resourcegroup": "Miko_tutorial_1",
        "runtime_version": "python|3.7",
        "runtime_version_detected": "-",
        "sku": "BASIC",
        "src_path": "C:\\adastra\\Projects\\Python\\djangoapp"
      }
16) log file diagnostic

      az webapp log tail

      or view it in web browser
      https://mikodjangopgtutorial1.scm.azurewebsites.net/api/logs/docker
      shows log files where you troubleshoot.

      like https://mikodjangopgtutorial1.scm.azurewebsites.net/api/vfs/LogFiles/2021_06_30_lw1sdlwk000016_default_docker.log

17) azure web app config
       az webapp log config --docker-container-logging filesystem
      {
        "applicationLogs": {
          "azureBlobStorage": {
            "level": "Off",
            "retentionInDays": null,
            "sasUrl": null
          },
          "azureTableStorage": {
            "level": "Off",
            "sasUrl": null
          },
          "fileSystem": {
            "level": "Off"
          }
        },
        "detailedErrorMessages": {
          "enabled": false
        },
        "failedRequestsTracing": {
          "enabled": false
        },
        "httpLogs": {
          "azureBlobStorage": {
            "enabled": false,
            "retentionInDays": 3,
            "sasUrl": null
          },
          "fileSystem": {
            "enabled": true,
            "retentionInDays": 3,
            "retentionInMb": 100
          }
        },
        "id": "/subscriptions/4dca53e2-a9ea-4950-9d3c-b30287a01567/resourceGroups/Miko_tutorial_1/providers/Microsoft.Web/sites/MikoDjangoPGTutorial1/config/logs",
        "kind": null,
        "location": "West US 2",
        "name": "logs",
        "resourceGroup": "Miko_tutorial_1",
        "systemData": null,
        "type": "Microsoft.Web/sites/config"
      }

18) how to immediately clean up resource and delete app from azure
    az group delete --no-wait
==============================================================================
miko azure scala spark
miko spark azure
Azure HDInsight
https://docs.microsoft.com/cs-cz/azure/hdinsight/
Azure HDInsight je spravovaná služba Apache Hadoopu, která umožňuje spouštět Apache Spark, Apache Hive, Apache Kafka, Apache HBA a další služby v cloudu.


https://docs.microsoft.com/cs-cz/azure/hdinsight/spark/apache-spark-jupyter-spark-sql
==============================================================================



==============================================================================
Access datasets with Python using the Azure Machine Learning Python client library

https://docs.microsoft.com/en-us/azure/architecture/data-science-process/python-data-access
==============================================================================
(base) PS C:\adastra\AdokiFE> node -v
v14.17.1
(base) PS C:\adastra\AdokiFE> npm -v
6.14.13

==============================================================================
(base) PS C:\adastra> cd angular-cli
(base) PS C:\adastra\angular-cli>
==============================================================================
Offloader-Manager/src/main/resources/log4j2.xml
Offloader-Manager/src/main/resources/application.conf
Offloader-Manager/local-dev.env
    # local dev ENV variables - not used by the docker containers
#kafka ??
    KAFKA_BOOTSTRAP_SERVERS=localhost:9092
    KAFKA_BOOTSTRAP_SERVER_1_HOST=localhost
    KAFKA_BOOTSTRAP_SERVER_1_PORT=9092
    DEV_MODE=true

    # MANAGER
    INTERNAL_MANAGER_HOSTNAME=localhost
    JOB_SERVICE_HOST_URL=http://localhost:9009
    DISTRIBUTOR_SERVICE_HOST_URL=http://localhost:9009
    FRONT_END_HOST=http://localhost:4200

    SLICK_DB_HOST=localhost
    SLICK_DB_PORT=3306
    DB_USER=root
    DB_PASSWORD=helloworld
    MANAGER_ID_PREFIX=kb-manager
# tady je to duležte změnit pro připojení do DB
    TZ=Europe/Prague

    APPLICATION_SECRET=TwqujOJq@v?uzp>E@W4CC^:o1cP;@jyzz@2C6lly_^P<nMlQtcYXxc__UOv0`zME

    adoki_manager_admin_password=admin
    adoki_job_service_manager_password=admin
    adoki_encryption_password=andndnamnmmaiian
    adoki_distributor_service_manager_password=admin

    #http://www.unit-conversion.info/texttools/random-string-generator/
==============================================================================
miko angular
how to start adoki clinet on local angular
local
  http://localhost:4200/admin/process-list

https://angular.io/cli

[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Users\michal.kocandrle\AppData\Roaming\", "User")


C:\Users\michal.kocandrle\AppData\Roaming\npm init -y && npm i mongoose joi express

C:\adastra\AdokiFE>
ng serve --open

ng build

install NPM
  PS C:\adastra> npm install --global yarn
  # zobrazí list použitých modulů, které je třeba naloadovat.
  (base) PS C:\adastra\AdokiFE> npm list -g --depth=0
      C:\Users\michal.kocandrle\AppData\Roaming\npm
      +-- @angular/cli@12.1.0
      -- yarn@1.22.10

  #install all packages / modules to angular project directory
  (base) PS C:\adastra\AdokiFE> npm install


  # Builds the project
    (base) PS C:\adastra\AdokiFE> ng build
    Your global Angular CLI version (12.1.0) is greater than your local version (8.1.3). The local Angular CLI version is used.

    To disable this warning use "ng config -g cli.warnings.versionMismatch false".
    Generating ES5 bundles for differential loading...
    ES5 bundle generation complete.

    chunk {runtime} runtime-es2015.js, runtime-es2015.js.map (runtime) 6.16 kB [entry] [rendered]
    chunk {runtime} runtime-es5.js, runtime-es5.js.map (runtime) 6.16 kB [entry] [rendered]
    chunk {polyfills} polyfills-es2015.js, polyfills-es2015.js.map (polyfills) 269 kB [initial] [rendered]
    chunk {styles} styles-es2015.js, styles-es2015.js.map (styles) 1.44 MB [initial] [rendered]
    chunk {styles} styles-es5.js, styles-es5.js.map (styles) 1.44 MB [initial] [rendered]
    chunk {polyfills-es5} polyfills-es5.js, polyfills-es5.js.map (polyfills-es5) 707 kB [initial] [rendered]
    chunk {main} main-es2015.js, main-es2015.js.map (main) 905 kB [initial] [rendered]
    chunk {main} main-es5.js, main-es5.js.map (main) 1.04 MB [initial] [rendered]
    chunk {vendor} vendor-es2015.js, vendor-es2015.js.map (vendor) 7.28 MB [initial] [rendered]
    chunk {vendor} vendor-es5.js, vendor-es5.js.map (vendor) 8.63 MB [initial] [rendered]
    Date: 2021-06-30T10:26:53.018Z - Hash: f5d156d5d4a4bd745dbf - Time: 101131ms

  # Starts the project in ng server
  (base) PS C:\adastra\AdokiFE> ng serve
    Your global Angular CLI version (12.1.0) is greater than your local version (8.1.3). The local Angular CLI version is used.
    To disable this warning use "ng config -g cli.warnings.versionMismatch false".
    10% building 3/3 modules 0 activei ｢wds｣: Project is running at http://localhost:4200/webpack-dev-server/
    i ｢wds｣: webpack output is served from /
    i ｢wds｣: 404s will fallback to //index.html
    chunk {main} main.js, main.js.map (main) 906 kB [initial] [rendered]
    chunk {polyfills} polyfills.js, polyfills.js.map (polyfills) 269 kB [initial] [rendered]
    chunk {runtime} runtime.js, runtime.js.map (runtime) 6.15 kB [entry] [rendered]
    chunk {styles} styles.js, styles.js.map (styles) 1.44 MB [initial] [rendered]
    chunk {vendor} vendor.js, vendor.js.map (vendor) 7.62 MB [initial] [rendered]
    Date: 2021-06-30T10:29:15.039Z - Hash: 93fc5f8085d7d5948910 - Time: 17468ms
    ** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **
    i ｢wdm｣: Compiled successfully.

==============================================================================
miko postman
installation
https://www.postman.com/downloads/
==============================================================================
simple angular restAPI
mkdir node-projekt
cd node-projekt
npm init --yes
  in package.json se dependencies express a express se nainstaloval do
  node_modules/

==============================================================================

mkdir movie-database
cd movie-database
  # vytvoří adresář client (routing. Zaškrtněme y)
ng n client
cd client
ng serve # spustí clienta

mkdir server
cd server
subl index.js
cd server
npm init -y && npm i mongoose joi express
tím jsme vytvořili soubor package.json
a modifikujeme
######
  {
    "name": "server",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "test": "echo \"Error: no test specified\" && exit 1",
      "start": "node index.js"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
      "express": "^4.17.1",
      "joi": "^14.3.1",
      "mongoose": "^5.7.1"
    }
  }
######
test serverové části
node index.js
cd c:/movie-database
npm init -y && npm i concurrently
modifikjeme package.json
  {
    "name": "movie-databse",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "test": "echo \"Error: no test specified\" && exit 1",
      "start": "concurrently \"cd server && node index.js\" \"cd client && ng serve\""
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
      "concurrently": "^4.1.2"
    }
  }
#####
cd c:/movie-database
miko start
  npm start (nastartuje aplikaci)

in client
  node index.js
in client following error message occurred

          C:\adastra\projects\angular\movie-database\client>ng serve
          ****************************************************************************************
          This is a simple server for use in testing or debugging Angular applications locally.
          It hasn't been reviewed for security issues.

          DON'T USE IT FOR PRODUCTION!
          ****************************************************************************************
          An unhandled exception occurred: The 'buildOptimizer' option cannot be used without 'aot'.
          See "C:\Users\MICHAL~1.KOC\AppData\Local\Temp\ng-m7hzEG\angular-errors.log" for further details.

resolved with

  C:\adastra\projects\angular\movie-database\client>ng serve --prod

Option "--prod" is deprecated: Use "--configuration production" instead.
Warning: 'outputHashing' option is disabled when using the dev-server.
Option "extractCss" is deprecated: Deprecated since version 11.0. No longer required to disable CSS extraction for HMR.
√ Browser application bundle generation complete.

Initial Chunk Files   | Names         |      Size
main.js               | main          |   3.84 MB
polyfills.js          | polyfills     | 623.45 kB
styles.css, styles.js | styles        | 500.10 kB
runtime.js            | runtime       |   6.82 kB

                      | Initial Total |   4.94 MB

Build at: 2021-07-16T14:03:29.376Z - Hash: 575c8e6274d8115bcbea - Time: 8215ms

** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **

miko continue
https://www.itnetwork.cz/javascript/angular/zaklady/databazovy-klient-v-angular-filtrovaci-komponenta


==============================================================================

Bootstrap instalace
cd client/
npm i bootstrap
Upravení angular.json
    "styles": [
    "src/styles.css",
    "node_modules/bootstrap/dist/css/bootstrap.min.css"
    ],
cd client
ng serve

MoviesList komponenta

C:\adastra\projects\angular\movie-database>cd client
C:\adastra\projects\angular\movie-database\client>ng g c movies-list/
  CREATE src/app/movies-list/movies-list.component.html (26 bytes)
  CREATE src/app/movies-list/movies-list.component.spec.ts (655 bytes)
  CREATE src/app/movies-list/movies-list.component.ts (294 bytes)
  CREATE src/app/movies-list/movies-list.component.css (0 bytes)
  UPDATE src/app/app.module.ts (414 bytes)

app/movies-list/movies-list.component.html
modify as
  <div id="movies" class="container tab-pane">
    <div class="row">
      <div class="col-2">
      <!-- Zde bude filtrace -->
      </div>
      <div class="col">
        <h3 class="mt-3">Seznam filmů:</h3>
        <div class="list-group mb-1">
          <button type="button" class="list-group-item list-group-item-action">
            Název 1. Filmu (Rok)
          </button>
          <button type="button" class="list-group-item list-group-item-action">
            Název 2. Filmu (Rok)
          </button>
        </div>
        <div class="btn-group float-right">
          <button type="button" class="btn btn-primary btn-sm">
            Zobrazit
          </button>
          <button type="button" class="btn btn-warning btn-sm">
            Upravit
          </button>
          <button type="button" class="btn btn-danger btn-sm" data-toggle="modal">
            Odebrat
          </button>
        </div>
      </div>
    </div>
  </div>
######

app-routing.module.ts

k vypadá naše nově vytvořená komponenta, musíme ji přidat do routeru
(souboru app-routing.module.ts) a následně upravit kořenovou šablonu
(app.component.html) naší aplikace.
C:\adastra\Projects\angular\movie-database\client\src\app\app-routing.module.ts
    import { NgModule } from '@angular/core';
    import { Routes, RouterModule } from '@angular/router';
    import {MoviesListComponent} from './movies-list/movies-list.component';

    const routes: Routes = [
      {path: 'movies-list', component: MoviesListComponent},
      {path: '', redirectTo: '/movies-list', pathMatch: 'full'},
    ];

    @NgModule({
      imports: [RouterModule.forRoot(routes)],
      exports: [RouterModule]
    })
    export class AppRoutingModule { }






==============================================================================
instalace clienta

ADOKIFE konfigurace na tvrdo v
src/assets/config.dev.json zkopírovat na a rekonfigurovat
src/assets/config.json

==============================================================================
miko how to release adoki
https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/KB-Offloader%20Team/_git/Ada-Offloader-Stack

Compose files
Run
for full-stack run docker-compose up [-d]command in the project directory
alternative is to run the complete stack with logging using command:
  docker-compose -f docker-compose.yml -f docker-compose.overwrite.yml -f docker-compose-log.yml -f docker-compose-log-full-stack.yml up <-d>

for lite run :
  docker-compose -f docker-compose.yml -f docker-compose-lite.yml [-f docker-compose-log.yml -f docker-compose-log-lite.yml] up [-d] command in the project directory.

TFS Deployment
It is possible to set up Continuous Integration using TFS.
The deployment process is bound to the superproject/stack repository.
Make sure a module/service was already pushed before you push a change of
the module/service to the stack repo.

Setup a new git repo
1) https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/_apps/hub/ms.vss-ciworkflow.build-ci-hub?_a=edit-build-definition&id=20

* Triggers -> Add the new branch filter
2) https://tfs.adastragrp.com/tfs/DefaultCollection/KB-Offloader/_release?definitionId=3&_a=releases

* Adoki deploy - Petr H. -> ... -> Clone
* Rename the definition
* Change stack name suffix
* Variables -> update ports and possibly kerberos related vars. You have to use port numbers that are not used
anywhere else. A good approach is to substitute a number in all port variables - eg. 90$8 or $3306 and put the number
to the Release name. If you want to use your own keytab make sure that user tfs-agent has access there (edge1).
* Triggers -> change the git branch
* Save
Service deployment process
1)  Commit our new change in the service (including the changed versions file)
2)  Commit the change in the stack repo.
    If there were any configuration changes update the project-config.env versions appropriately
    (more in the Versions section of the Service documentation).
3) Push the service change to the TFS Git repo
4) Push the stack

Worker deployment
1) Update the ADOKI_WORKER_VERSION and increase the ADOKI_DISTRIBUTOR_IMPL_VERSION in the project-config.env
2) Commit and push the change
==============================================================================
Ada-Offloader-Stack / project-config.env
ADOKI_JOB_IMPL_VERSION=1
ADOKI_DISTRIBUTOR_IMPL_VERSION=33
ADOKI_SPARK_DEPENDENCIES_VERSION=1.0.58
ADOKI_STACK_CONFIG_VERSION=1.1.1

ADOKI_DISTRIBUTOR_SCALA_VERSION=2.11.12
ADOKI_SPARK_VERSION=2.4.0
ADOKI_CDH_VERSION=cdh6.2.0
ADOKI_SPARK_LIBS_VERSION=2.4.0-cdh6.2.0
ADOKI_WORKER_VERSION=0.2.28

ADOKI_DISTRIBUTOR_BASE_IMAGE=alpine:3.8

# the ID is used as a part of a docker image ID
ADOKI_CLIENT_ID=ada

ADOKI_USER_ID=10017
ADOKI_GROUP_ID=10150
==============================================================================
miko tutorials in progress
PS C:\adastra\projects\BDT\cviceni>
jupyter lab


how to start adoki clinet on local angular
C:\adastra\AdokiFE>
ng build

ng serve
==============================================================================
miko skylink
33755991933

==============================================================================
KB dokumentace
C:\Users\michal.kocandrle\OneDrive - Adastra, s.r.o\Documents\KB
==============================================================================
miko code

@param message    com.adastragrp.offloader.api.worker.dto.Message
@param statistics com.adastragrp.offloader.api.worker.dto.Statistics
@param result     com.adastragrp.offloader.api.worker.dto.resultset




GIT
https://git.kb.cz/projects/BDP/repos/dwh-offloader/browse
==============================================================================
miko corka
wiki.kb.cz najít DSSLINE/iNSTALACE Git klienta

https://feak.kb.cz ??

https://wiki.kb.cz/confluence/display/BDPA/DWH+Offloader

https://aslana.kb.cz/offloader/dashboard

https://nsvpxpro.kb.cz/vpn/index.html
https://egate.kb.cz/vpn/index.html
Nexus
https://nexus3.kb.cz/#browse/search=keyword%3Desco

JupyterHub
https://jupyterhub.bdp.kb.cz:8000/tree

Zeppelin

https://zeppelin.bdp.kb.cz
cloudera manager
https://Ifc-edge-001.sos.kb.cz:7183

path to json load devinitions.
/appl/claudera/tech_users/service_offloader/offloader_sync/tmp/json

Local Kafka Docker From https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html
cd examples/cp-all-in-one
docker-compose up -d --build
docker-compose ps
create image for docker
docker-machine create --driver virtualbox --virtualbox-no-vtx-check --virtualbox-memory 6000 confluent

https://docs.confluent.io/3.3.0/installation/docker/docs/quickstart.html
.\kafka-topics.bat --create --topic offloader_input_test --partitions 1 --replication-factor 1 --if-not-exists --zoonkeeper localhost:2181 --delete --topic offloader_test
zkserver
.\bin\windows\gookeeper-server-start.bat .\config\zookeeper.properties


==============================================================================
Já používám openSsh a přes to to jde, když necílím localhost ale 127.0.0.1.
Používám to takto: ssh -nNTL 25601:127.0.0.1:25601 disc
(disc mám nastaveno v openssh konfiguraci) - můžeš to takto rozjet třeba přes git-bash konzoli.
==============================================================================
{
    "name": "TD_MIKO",
    "dataType": "date",
    "operator": "$predicate_column$ >= '$predicate_value_min$'",
    "minValue": "1900-01-01",
    "description": "Date value where condition to use in Teradata. Searches for equal and higher."
 }
  ==============================================================================
miko nagualr dokumentace

https://www.codegrepper.com/code-examples/javascript/ng+build+--prod+--build-optimizer+--aot

==============================================================================
miko connection KB disc put
{
  "id": 1,
  "name": "bdpd",
  "system": "cloudera",
  "connections": 60,
  "memory": 100,
  "startAt": "00:00:00",
  "endAt": "23:59:59",
  "systemConnections": [
    {
      "id": 1,
      "name": "bdpd_impala_kerb",
      "system": "impala",
      "url": "jdbc:impala://cloudera-manager.bdpd.kb.cz:21050;AuthMech=1;KrbAuthType=1;KrbHostFQDN=cloudera-manager.bdpd.kb.cz;KrbServiceName=impala;OptimizedInsert=0;SSL=1",
      "username": "",
      "password": "",
      "properties": []
    },
    {
      "id": 2,
      "name": "bdpd_hive_kerb",
      "system": "hive",
      "url": "jdbc:hive2://cn74x007.sos.kb.cz:10000/default;AuthMech=1;KrbAuthType=1;KrbHostFQDN=cn74x007.sos.kb.cz;KrbServiceName=hive;KrbRealm=SOS.KB.CZ;SSL=1",
      "username": "",
      "password": "",
      "properties": []
    },
    {
      "id": 3,
      "name": "odis_impala_bdpd",
      "system": "impala",
      "url": "cloudera-manager.bdpd.kb.cz",
      "username": "service_offloader_temp",
      "password": "",
      "properties": []
    },
    {
      "id": 8,
      "name": "bdpd_hdfs",
      "system": "hdfs",
      "url": "hdfs://user/e_mkocan/",
      "username": "e_mkocan",
      "password": "4_Plesoun_7",
      "properties": []
    }
  ],
  "systemResourcePools": []
}
==============================================================================

src/app/assests/config.json
{
    "backendServer": "http://localhost:9009",
    "kibanaServer": "http//localhost:25601",
    "swaggerUi": "http://localhost:28080",
    "appVersion": "0.0.0.0"
}
