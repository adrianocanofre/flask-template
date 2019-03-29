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
$ docker run -d -p 5000:80 --env-file=/path/file <Project-name>
```

## Built With

* [Flask](http://flask.pocoo.org/)  
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)  
* [Flasgger](https://github.com/rochacbruno/flasgger)

## Release History  
**0.0.1**  
* Initial version(beta)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
