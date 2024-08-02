

<h1 align="center">
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://f.hubspotusercontent20.net/hubfs/2829524/Copia%20de%20LOGOTIPO_original-2.png"></a>
  <br>
  Pragma
  <br>
</h1>

<h4 align="center">Proyecto base de <a href="https://github.com/ScreenPyHQ/screenpy_selenium" target="_blank">Pragma</a>.</h4>

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

## Topicos

* Python
* Pytest
* Appium
* Screenpy
* Screenpy-appium

## Instalación y ejecución

Para clonar y ejecutar está aplicación, necesitas [Git](https://git-scm.com) y [Python](https://www.python.org//) instalados en tu equipo y desde la linea de comandos ejecutar lo siguiente:

```bash
# Clone this repository
$ git clone https://github.com/somospragma/qa-web-screenpy-python.git

# Install Python virtual environment for the project 
$ pipenv install
$ pipenv shell

# Install dependencies
pipenv install screenpy-appium
pipenv install screenpy-adapter-allure

# Run tests 
$ pytest features/ --alluredir='<projectpath>\allure-report'

# View report
$ allure serve <allure-report-dir>
```


## Descarga

Puedes descargar el proyecto en el enlace [download](https://github.com/amitmerchant1990/electron-markdownify/releases/tag/v1.2.0) 

## Consideraciones
El proyecto usa como aplicación móvil la app de Demo sauce labs, el correcto funcionamiento de los casos de uso dependeran de la disponibilidad de la aplicación demo en cuestión

## Tecnologias
-   [Python]
-   [Appium]
-   [Screenpy]


## Autores

- Jorge Ardila Camargo

## Relacionados

- [Proyecto screenpy Base](https://github.com/ScreenPyHQ/screenpy_appium)


## Roadmap

- [Guia QA](https://github.com/amitmerchant1990/pomolectron) - (En construcción) Una guia de proyectos Orientados a la Calidad de Software
