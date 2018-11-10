
[![Status](https://img.shields.io/badge/Status-Documenting-yellow.svg)](https://github.com/xenahort/proyectoCloudComputing/blob/master/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/xenahort/proyectoCloudComputing/blob/master/LICENSE)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)
[![Language](https://img.shields.io/badge/language-Flask-green.svg)](http://flask.pocoo.org/)
[![Language](https://img.shields.io/badge/language-MySQL-orange.svg)](https://www.mysql.com/)


# Proyecto de Cloud Computing

Proyecto de la asignatura Cloud Computing del Máster de Ingeniería Informática de Granada.

A lo largo del desarrollo del proyecto, se actualizará la web de la aplicación con funcionalidades y especificaciones del propio en el siguiente [enlace](https://xenahort.github.io/).

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

	requirements.txt: especifica las dependencias de Python necesarias para la ejecución de la aplicación.
	Procfile: especifica los comandos ejecutados por la aplicación.
	nltk.txt: especifica los distintos corpus de texto requeridos por la dependencia nltk.
	
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

***

