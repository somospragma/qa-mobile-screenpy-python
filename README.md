

<h1 align="center">
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://f.hubspotusercontent20.net/hubfs/2829524/Copia%20de%20LOGOTIPO_original-2.png"></a>
  <br>
  Pragma
  <br>
</h1>

<h4 align="center">Proyecto base de <a href="https://github.com/karatelabs/karate" target="_blank">Pragma</a>.</h4>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

Breve descripción del proyecto
<p align="center">
  <a href="#topicos">Topicos</a> •
  <a href="#instalación-y-ejecución">Instalación y ejecución</a> •
    <a href="#descarga">Descarga</a> •
  <a href="#download">Descripción</a> •
  <a href="#download">Consideraciones</a> •
  <a href="#download">Tecnologias</a> •
  <a href="#credits">Autores</a> •
  <a href="#related">Relacionados</a> •
  <a href="#roadmap">Roadmap</a>
</p>

![screenshot](https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.gif)

## Topicos

* Karate
* Java
* Rest
* Gherkin
* Cucumber

## Instalación y ejecución

Para clonar y ejecutar está aplicación, necesitas [Git](https://git-scm.com) and [Java JDK](https://nodejs.org/en/download/) instalados en tu equipo. Desde la linea de comando:

```bash
# Clone this repository
$ git clone https://github.com/amitmerchant1990/electron-markdownify

# Go into the repository
$ cd electron-markdownify

# Install dependencies
$ npm install

# Run the app
$ npm start
```

### Run con java jar
```
java -jar karate-1.4.0.jar <ruta_del_archivo.feature>

java -jar karate-1.4.0.jar -Dkarate.options="--config karate-config.js" -DbaseUrl=https://miotraurl.com ruta_del_archivo.feature

java -jar karate-1.4.0.jar -Dkarate.options="--config karate-config.js" ruta_del_archivo.feature
```

#### ejemplo run con java jar

```
 java -jar karate-1.4.0.jar src/test/java/users/get/user-get.feature
 
```

### Run con gradle

```

 test --tests <nombre_de_clase>.<nombre_del_método> -D<propiedades_del_sistema>
 
 test --tests SampleTesClassRunner -DbaseUrl=https://reqres.in 
 
 test --tests SampleTesClassRunner.testTagsMethod -DbaseUrl=https://reqres.in 
 
 test -Dtest=SampleTesClassRunner#testTagsMethod
 
```

#### ejemplo run con gradle

```
 gradle test --tests ManagementUserTest.testParallel -DbaseUrl=https://reqres.in 
 
 gradle test --tests UserGetRunner -DbaseUrl=https://reqres.in 
 gradle test --tests UserGetRunner.userGet -DbaseUrl=https://reqres.in 
 
 gradle test -Dtest=UserGetRunner#userGet -DbaseUrl=https://reqres.in 
 
```


## Descarga

Puedes descargar el proyecto en el enlace [download](https://github.com/amitmerchant1990/electron-markdownify/releases/tag/v1.2.0) 

## Consideraciones
El proyecto usa como servicio base el servicio demo Reqres, el correcto funcionamiento de los casos de uso dependeran de la disponibilidad del servicio demo en cuestion

## Tecnologias
-   [JDK java]
-   [Karate]
-   [Gradle]


## Autores

- Mauro L. Ibarra P.
- Johan E. Agudelo

## Relacionados

- [Proyecto Karate Base](https://github.com/amitmerchant1990/markdownify-web)


## Roadmap

- [Guia QA](https://github.com/amitmerchant1990/pomolectron) - (En construcción) Una guia de proyectos Orientados a la Calidad de Software
