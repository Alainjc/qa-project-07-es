
## Proyecto sprint 7: Automatización de pruebas de la aplicación web


## Descripción




> El proyecto es un sistema desarrollado mediante el lenguaje de programación "Python" junto con las herramientas que ofrece "Selenium" para automatizar pruebas. Las pruebas permiten verificar la disponibilidad de diversos elementos dentro de la página web de "Urban Routes" con la finalidad comprobar el funcionamiento y disponibilidad de elementos clave que permitan al usuario tener una buena experiencia en el aplicativo.




## Documentación utilizada


- [Python] - https://docs.python.org/3/
- [Pytest] - https://docs.pytest.org/en/7.1.x/contents.html
- [Selenium] - https://selenium-python.readthedocs.io/


## Tecnologías y herramientas utilizadas 

El proyecto hace uso de varias tecnologías y herramientas para optimizar el desarrollo, la ejecución y mantenimiento de las pruebas automatizadas.

                             Tecnologías y herramientas 
    Python: Desarrollo del código
    Pycharm: Editor de código
    Control de versiones: Git
    Selenium WebDriver: Automatización de acciones en navegadores web 
    Chromedriver: Interfaz entre Selenium Webdriver y el navegador Chrome


## Tecnicas utilizadas
    
- Page Object Model (POM): Estructura para organizar el código, reutilizar las pruebas automatizadas, facilitar el mantenimiento de las pruebas y reducir la duplicación del código.

- Esperas explícitas: mediante WebDriverWait para manejar la sincronización en la ejecución de las pruebas automatizadas
    

    

## Instalación y ejecución del proyecto
    Pre-requisitos
- Python 3.12
- Selenium WebDriver
- Navegador Chrome 
- WebDriver compatible con la versión del navegador 
  
 

    Instalación
1. Clonar el repositorio desde Github con el siguiente URL: https://github.com/Alainjc/qa-project-07-es.git
2. Instalar las dependencias del proyecto usando los siguientes comandos desde la línea de comandos: 
    - 'pip install pytest'
    - 'pip install selenium'


    Ejecución
- Abrir la línea de comandos 
- Navegar hasta el directorio donde se encuentra el archivo "qa-project-07-es"
- Usar el comando "pytest" para ejecutar las pruebas

## Descripción del contenido 

El proyecto contiene los siguientes archivos:

    data.py
Se especifican los datos de configuración como la URL de la página web y datos necesarios para desarrolar las pruebas automatizadas.

    main.py
Se especifican los localizadores que serán utilizados para poder realizar las acciones necesarias durante el desarrollo de las pruebas automatizadas, al igual que funciones y métodos que realizan acciones específicas dentro de la pagina web. Dentro de el archivo se desarrollan las pruebas automatizadas mediente el uso de Selenium y referenciando los métodos necesarios para verificar elementos clave dentro de la web.




## Autor/es
>Alain Julián Chan Pat
GITHUB: https://github.com/Alainjc

