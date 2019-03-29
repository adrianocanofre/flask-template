# Flask Template

This project contains a basic template for using em microservices, apis and other project. This is a RESTFUL service and responds in json.  

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

##### Linux/Mac OS
```
virtualenv
python 3.6
```

##### Installing

```
$ cd flask-template
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip  install -r requirements.txt
```

## Configure

You need to add some variable  to run the project.

```
ENVIRONMENT=NAMEENVIRONMENT
SERVICE_NAME=YOURSERVICENAME
```  
Variables that you can use:  

[config.py](config.py)  
```
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```  

## Running the application


Basic run:

```
$ python app.py
```

Build With Docker without env-file
```
$ docker build -t <Project-name> .
$ docker run -d -p 5000:80 <Project-name>
```
Build With Docker with an env-file (you can build with staging, dev or production)
```
$ docker build -t flask-template  .
$ docker run -d -p 5000:80 <Project-name>
```
Run docker using env file if you don't specified it in build definition
```
$ docker run -d -p 5000:80 --env-file path/your/file <Project-name>
```

**ATTENTION**  
You have to change the ports and edit the file config.py.


## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used


## Release History  
* x.x.x(open version)
  * Install git in gitlab-ci and dockerfile
  * Add endpoint /info

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
