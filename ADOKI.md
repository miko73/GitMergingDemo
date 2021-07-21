# Adoki postupy
## Založení systémových připojení

K jednotlivým rozraním adoki přistupujeme loalhost URLs
* Front-End: http://localhost:28088/admin/process-list
* Swagger: http://localhost:28080/swagger
* monitoring Kibana: http://localhost:25601/kibana/app/kibana_overview)

služby zpravidla na běží EDGE serveru a abychom na ně
mohli přistupovat přes local host je třeba nastavit tunelování, 
buď přes síťovou konfiguraci v Putty, nebo přes konfiguraci ssh

###SSH konfigurace
    C:\Users\E_MKOCAN\.ssh\config
    File:
    Host edge
    HostName edge1.hadoop.local
    User Michal.Kocandrle
    Port 22

následující tuneling se spouští v command promptu    
* Front-End: http://localhost:28088/admin/process-list    
    ssh -m hmac-sha2-512 -nNTL 28088:127.0.0.1:28088 edge

- Swagger: http://localhost:28080/swagger
        
    ssh -m hmac-sha2-512 -nNTL 28080:127.0.0.1:28080 edge

* monitoring Kibana: http://localhost:25601/kibana/app/kibana_overview)
  
    ssh -m hmac-sha2-512 -nNTL 25601:127.0.0.1:25601 edge
***
##Swagger
configuraci adoki provádíme přes REST API rozhraní Swagger
Swagger: http://localhost:28080/swagger
***
###Swagger - login
Přihlášení do rozhraní Swagger
>V sekci **login** - **POST /sys/user/login**
Tlačítko **"Try it out"**

otevře formulář pro zápis 
{
    "username": "string",
    "password": "string"
}
kde "string" nahradíme validními hodnotami.
Tlačítkem **Execute** odešleme požadavek na server
v poli 	
    **Response headers**

si zkopírujeme hodnotu v poli
    
**authorization: Bearer** *eyJ0eXAiOiJKV1QiLCJhbG...dkfjsld*

V horní části obrazovky otevřeme tlačítkem **Authorize** 

a vložíme 
zkopírované heslo *eyJ0eXAiOiJKV1QiLCJhbG...dkfjsld*
****
### Swagger - Import systémů ve formátu json
> V sekci **system** - **POST /sys/system**

můžeme vložit v json fromátu konfiguraci připojení
****
###Front-End aplikace
Nahraná připojení si můžeme zkontrolovat 
a doupravit v adoki Front-End apliaci 

>  http://localhost:28088/admin/process-list
> 
>    Settings -> Systems 

po rozkliknutí detailu systému je zobrazen seznam připojení včetně
connect stringu a login informací.

Nové systémy a i připojení je také možné vytvářet a editovat  
manuálně v prostředí frontendu
***
### Swagger - Import scénáře PROCESU datového přenosu
> Swagger: http://localhost:28080/swagger 
>
> V sekci **cnf_scenario** - **POST /cnf/scenario/process**

můžeme vložit v json fromátu zjednodušenou konfiguraci datového přenosu. Na zákadě popisu zdroje a cíle přenosu ve formátu json, bude vygenerován metadatový poips přenosu včetně vztahů 
sloupců zdrojových a cílových tabulek. 

> !!!
>    Tímto způsobem je možné vkládat pouze přenosy využívající 
>    předem připravené přenosové systémy a připojení.

***
<h1 align="center"> Title </h1>
<h1 align="right"> Title </h1>

<a> Title </a>
<p align="center"> Title </p>

<small> small </small>
<br>
<b> bold </b>


<h2 align="center"> Title </h2>










---
___
*kurziva* **bold**.
> blok


***

* asterisks
* next
- Or minuses
- Or minuses
+ Or pluses
+ Or pluses

***


This project was generated with 
link [Angular CLI](https://github.com/angular/angular-cli) version 7.2.3.
### Nadpis 3
Run `ng serve` 



