# **FLAT** **RENTAL**
****

### *This is an application to make advertisement of apartment for rent. User can submit form of advertisement with all detail of a flat (e.g. Location, Price, Area). To every advertisement users can contact publisher and he/she will get notified.* ###

****

## **GETTING** **STARTED**

1. Download
   * You need to clone repository to your local destination
       ~~~python
            $ cd path\to\your\workspace
            $ git clone https://github.com/Spikey21/Flat-Rental.git

   * if you have established ssh connection to github you can use this link to clone repo:
       ~~~python
            git@github.com:Spikey21/Flat-Rental.git
     
2. To run this application you need to have installed docker and docker-compose, if you don't have it already, please visit this sites for further instruction:
   *  [docker](https://docs.docker.com/ee/supported-platforms/)
   *  [docker-compose](https://github.com/Yelp/docker-compose/blob/master/docs/install.md)
3. If you have docker applications installed type this commands to build docker container:

   `make build`

   `make dev`
4. After that populate database with command below:

   `docker-compose run app sh -c "python manage.py runserver"`
 
5. If you want to create superuser:

   `make createsuperuser`

## **USAGE**

When project will be up, go to: http://localhost:8000/
