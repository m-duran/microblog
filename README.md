# Microblog
A micro blog application. Based on the [Flask Megatutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

## Configuration Variables
Set these environment variables:  
SECRET_KEY  : Application's secret key  
SQLALCHEMY_DATABASE_URI : URI for the database for the application to use  

<hr>

#### Email Notifications  

To use mail notifications, set up a mail service and provide these environment variables as appropriate:  

MAIL_SERVER  
MAIL_PORT  
MAIL_USE_TLS  
MAIL_USERNAME  
MAIL_PASSWORD  
<hr>

#### Post Translation  
To use post translation service, set up a [MS Translator API](https://azure.microsoft.com/en-us/services/cognitive-services/translator-text-api/) and provide the following variable:  

MS_TRANSLATOR_KEY : API key for your translation service on Azure

#### Elasticsearch  
To use [Elasticsearch](https://www.elastic.co/products/elasticsearch) to search post content, set up Elasticsearch and provide the URI in the following variable:  

ELASTICSEARCH_URL : The url of the Elasticsearch service to use


## Manual Installation
Manual: Use pip and your preferred environment manager to install dependencies

    pip install -r requirements.txt
    
Install or run an email service, Elasticsearch instance, and MS translator service if using them.

## Docker  
To run the application as a docker image, build and run the provided dockerfile, passing any needed environment variables:  

    docker build -t microblog .
    docker run
        -p 5000:5000
        --env FLASK_ENV=development
        --env MAIL_SERVER={your email server url}
        --env MAIL_PORT={your email server port}
        --env MAIL_USE_TLS={your email server TLS setting}
        --env MAIL_USERNAME={your email server username}
        --env MAIL_PASSWORD={your email server password}
        --env MS_TRANSLATOR_KEY={your MS translator key}
        --env ELASTICSEARCH_URL={your elasticsearch url}
        --name microblog
        microblog 
        
There is also a script that starts Elasticsearch as a container, located under the elasticsearch directory. 
        
## Docker-Compose
You can start both the application and elasticsearch with the provided docker-compose file. Provide your environment variabled and run:  

    docker-compose up
