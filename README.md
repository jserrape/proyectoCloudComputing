
[![Status](https://img.shields.io/badge/Status-Documenting-yellow.svg)](https://github.com/xenahort/proyectoCloudComputing/blob/master/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/xenahort/proyectoCloudComputing/blob/master/LICENSE)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)
[![Language](https://img.shields.io/badge/language-Flask-green.svg)](http://flask.pocoo.org/)
[![Language](https://img.shields.io/badge/language-MySQL-orange.svg)](https://www.mysql.com/)


# Proyecto de Cloud Computing

Proyecto de la asignatura Cloud Computing del Máster de Ingeniería Informática de Granada.

***

## Descripción de la situación actual

Últimamente estamos oyendo hablar mucho del **procesamiento del lenguaje natural** (PLN) y ahora más en este mundo digital. Sin embargo, el PLN es una disciplina que cuenta con más de 50 años de investigación y desarrollo.

El Procesamiento del Lenguaje Natural es el campo de conocimiento de la **Inteligencia Artificial** que se ocupa de la investigar la manera de comunicar las máquinas con las personas mediante el uso de lenguas naturales, como el español, el inglés o el chino.

Virtualmente, cualquier lengua humana puede ser tratada por los ordenadores. Lógicamente, limitaciones de interés económico o práctico hace que solo las lenguas más habladas o utilizadas en el mundo digital tengan aplicaciones en uso.

***

## Descripción general del proyecto que se va a realizar

El objetivo del proyecto va a consistir en el desarrollo de una plataforma dedicada al procesamiento del lenguaje natural. La plataforma permitirá introducir comentarios para obtener con gran confianza si se tratan de comentarios positivos o negativos, análisis de oraciones, etc.

***

## Arquitectura

Una vez revisadas las distinas arquitecuras software se ha optado por el uso de una arquitecura basada en microservicios para el desarrollo y despliegue de cada funcionalidad de forma independiente.

**¿Qué es un microservicio?**

> Los [microservicios](https://microservices.io/) se caracterizan por poder usar tecnologías subyacentes que van desde la virtualización completa en la nube hasta el uso de contenedores Docker en una sola máquina virtual.

> Lo principal en una arquitectura de microservicios es que se trata de unidades que se van a desplegar de forma independiente, diferentes servicios que trabajarán de forma totalmente independiente unos de otros.

El proyecto inicialmente estará formado por:
1. Microservicio de registro y login
2. Microservicio para el análisis de opiniones.
3. Microservicio para el análisis sintáctico de oraciones.
4. Servicios de gestión de base de datos Mysql.

El desarrollo va a ser realizado en Python utilizando de forma inicial el microframework Flask, la librería nltk con múltiples corpus de texto aún por determinar y el analizardor de texto de Stanford.

***

## Plataforma como servicio: Heroku

Para la elección de un PaaS se ha probado entre zeit.co y Heroku. Se ha optado por Heroku ya que permite gran cantidad de horas de cómputo gratuitas, soporte para multitud de lenguajes y [documentación](https://devcenter.heroku.com/) específica para construir, desplegar y gestionar las aplicaciones.

	Despliegue: https://shielded-scrubland-22143.herokuapp.com/

Ficheros de configuración la aplicación:

	requirements.txt: especifica las dependencias de Python necesarias, así como la versión para la ejecución de la aplicación.
	Procfile: especifica los comandos que son ejecutados por los términos de la aplicación. Hace uso de gunicorn como servicio HTTP WSGI así como especifica el fichero principal de la aplicación.
	nltk.txt: especifica los distintos corpus de texto requeridos por la dependencia nltk que deben ser instalados.
	.travis: especifica datos para el servicio de test como el lenguaje y versión que se va a utilizar, comandos requeridos previos (instalación de librerias y ficheros) y los ficheros que implementan los tests.

**Microservicio desplegado:**

Para el presente hito se ha desarrollado en primer lugar el microservicio de análisis de opiniones destinado a analizar si es positiva o negativa. El microservicio comentado se encuentra en:

	https://shielded-scrubland-22143.herokuapp.com/analize/{comentario}

Para el comentario "I love you." el sistema devolverá:

	{"ruta":"/analize/I%20love%20you","status":"OK","valor":"POSITIVE"}

Mientras que para el comentario "I hate you." el sistema devolverá:

	{"ruta":"/analize/I%20hate%20you","status":"OK","valor":"NEGATIVE"}

En la ruta / del sistema se devolverá:

{"ejemplo":{"ruta":"/analize/I%20love%20you","valor":"{\"ruta\":\"/analize/I%20love%20you\",\"status\":\"OK\",\"valor\":\"POSITIVE\"}"},"ruta":"/","status":"OK"}

En caso de tratar de acceder a una página que no existe el sistema devolverá:

	{"status":404}

Finalmente se ha desarrollado la ruta https://shielded-scrubland-22143.herokuapp.com/about

### Tests

Travis CI es un servicio de integración continua distribuido y alojado que se utiliza para crear y probar proyectos de software alojados en GitHub.

Para el hito 2 se han implementado 11 tests para la comprobación de las distintas funciones del servicio.

### Despliegue

Para el despliegue, se ha realizado de forma que al hacer push a GitHub y tras pasar los tests de Travis-CI se sube de forma automática a Heroku.

Esta configuración se realiza en el menú de la aplicación de Heroku, la opción 'Deploy', y en 'Deployment method'. Se debe enlazar con el proyecto de GitHub y activar el 'Automatic deploys from  master are enabled'.

![Despliegue](img/deploy.png)

### Despliegue en Azure

La aplicación ha sido desplegada en Azure en la dirección:

```
MV: 13.80.105.155
```

La descripción completa correspondiente al provisionamiento mediante Ansible en Azure se encuentra [aquí](https://github.com/xenahort/proyectoCloudComputing/blob/master/provision/ansible/README.md)


***

### Acopio

Para el acopio se ha utilizado una máquina virtual **Ubuntu Server 18.04 LTS**. Se ha escogido dicha imagen debido a que no requerimos de elementos como interfaz gráfica ni navegadores, y sí que se requeriría de un soporte a largo plazo.


La aplicación ha sido desplegada en Azure en la dirección:

```
MV2: 40.127.160.236
```

A través de la línea de comandos "Cloud shell" se ejecutarán los siguientes comandos para la creación de una máquina.

En primer lugar creamos el grupo 'acopioM' correspondiente a la localización Europa occidental.

```
az group create --name acopioM --location uksouth
```

Posteriormente creamos la maquina 'maquinaHito4' asociada al grupo anterior con una imagen UbuntuLTS. La creación de la máquina devolverá un JSON con diferentes parámetros de la máquina como su IP que se extraerá con [jq](https://stedolan.github.io/jq/manual/).
Para extraer el parametro publicIpAddress del JSON se basado en el comentario de [Brian Campbell](https://stackoverflow.com/users/69755/brian-campbell) del post https://stackoverflow.com/questions/1955505/parsing-json-with-unix-tools

```
ip=$(az vm create --resource-group acopioM --name maquinaHito4 --image UbuntuLTS --generate-ssh-keys | jq -r '.publicIpAddress')
```

Abro el puerto ssh de la máquina
```
az network nsg rule create --resource-group acopioM --nsg-name maquinaHito4 --name SSH_rule \
    --protocol tcp \
    --priority 320 \
    --destination-port-range 22 \
    --access allow >/dev/null
```

Abro el puerto http de la máquina
```
az network nsg rule create --resource-group acopioM --nsg-name maquinaHito4 --name HTTP_rule \
    --protocol tcp \
    --priority 300 \
    --destination-port-range 80 \
    --access allow >/dev/null
```

Defino el usuario y añado la clave pública.

```
az vm user update --resource-group acopioM -n maquinaHito4 -u xenahort --ssh-key-value "$(< $HOME/.ssh/id_rsa.pub)"
```

Con lo anterior la máquina está instalada y configurada para iniciar el [provisionamiento](https://github.com/xenahort/proyectoCloudComputing/tree/master/provision/ansible).

Se clona el proyecto y se modifica el fichero hosts con la ip de la máquina.

```
git clone https://github.com/xenahort/proyectoCloudComputing
cd provision/ansible

echo "[ubuntuserver]\nxenahort ansible_ssh_port=22 ansible_ssh_host=**$ip**\n[ubuntuserver:vars]\nansible_ssh_user=xenahort\nansible_ssh_private_key_file=$HOME/.ssh/id_rsa" > hosts
```

Finalmente hay que ejecutar el playbook
```
ansible-playbook playbook.yml
```

### Prueba de velocidad

La localización de la máquina es uksouth ya que como se puede ver en [http://www.azurespeed.com/](http://www.azurespeed.com/) ya que tiene mejores estadísticas que otras localizaciones.

Para la prueba de velocidad se ha utilizado el comando 'httperf' de la forma:
```
httperf --port 80 --num-conns 20 --rate 1 --server 40.127.160.236
```

Obetniendo:
```
httperf --client=0/1 --server=40.127.160.236 --port=80 --uri=/ --rate=1 --send-buffer=4096 --recv-buffer=16384 --num-conns=20 --num-calls=1
httperf: warning: open file limit > FD_SETSIZE; limiting max. # of open files to FD_SETSIZE
Maximum connect burst length: 1

Total: connections 20 requests 20 replies 20 test-duration 19.126 s

Connection rate: 1.0 conn/s (956.3 ms/conn, <=1 concurrent connections)
Connection time [ms]: min 118.3 avg 148.3 max 337.5 median 124.5 stddev 60.3
Connection time [ms]: connect 77.6
Connection length [replies/conn]: 1.000

Request rate: 1.0 req/s (956.3 ms/req)
Request size [B]: 67.0

Reply rate [replies/s]: min 1.0 avg 1.0 max 1.0 stddev 0.0 (3 samples)
Reply time [ms]: response 62.0 transfer 8.6
Reply size [B]: header 152.0 content 162.0 footer 0.0 (total 314.0)
Reply status: 1xx=0 2xx=20 3xx=0 4xx=0 5xx=0

CPU time [s]: user 4.38 system 14.30 (user 22.9% system 74.7% total 97.6%)
Net I/O: 0.4 KB/s (0.0*10^6 bps)
```

Así pues, con un total de 20 conexiones  el 'Reply rate' medio es de 1.0 replies/s y el 'Connection time' medio es de 124.5 ms.
