# **FLAT** **RENTAL**
****

### *This is an application to make advertisement of apartment for rent. User can submit form of advertisement with all detail of a flat (e.g. Location, Price, Area). To every advertisement users can contact publisher and he/she will get notified.* ###

****

## **GETTING** **STARTED**
 
There are two ways to bring this application:

* First option
   1. To run this application you need to have installed docker and docker-compose, if you don't have it already, please visit this sites for further instruction:
        `  docker
           docker-compose`
   2. If you have docker applications installed type this commands to build docker container:
      `  make build
         make dev`
   3. If you want to create superuser:
     `make createsuperuser`
* Second option (old way)
   1. Download
      * You need to clone repository to your local destination
          ~~~python
               $ cd path\to\your\workspace
               https://github.com/Spikey21/Flat-Rental.git

      * if you have established ssh connection to github you can use this link to clone repo:
          ~~~python
                 git@github.com:Spikey21/Flat-Rental.git
    2. Make virtual environment and activate it (optional) 
       ~~~python
             $ python -m venv venv
             $ venv\Scripts\activate
    3. Install requirements
       
       ~~~python
                      $ pip install -r requirements.txt
    4. After this you can create your superuser
   
         `python manage.py createsuperuser`
    5. Finally, you can run application

    `python manage.py runserver 0.0.0.0:8000`