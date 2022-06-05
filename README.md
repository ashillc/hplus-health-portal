# hplus-health-portal for awesome-clinic

## Description and Overview
- This is a mock python application that is used for storing patient/client information in a database. 
The application also stores appointment and doctor related information that links to a specific client/patient.

- The app has a RESTFUL interface and can be interacted with using basic GET, POST, PATCH, DELETE actions.

## Cloning this repository
This repo can be cloned using a git client via https : `https://github.com/ashillc/hplus-health-portal.git`
The main branch is `dev` and all changes will be merged to `main` once peer reviewed. 

## Setting up the local development environment
This app can be either run using `Docker` or using python via a virtual environment/system python.
### Docker Approach
- Clone this repository and ensure docker is installed on your machine. Once installed, run ``docker-compose up``.
This will build the app, install dependencies and create the webserver

### Local python/virtual environment approach
To run this program, all you need is python installed on your pc / machine and run using the following commands:
(*ensure you are in the manage.py directory)
- `python manage.py migrate`
- ``python manage.py runserver 8000``

NOTE:
The backend database configured is postgres and can be viewed in the settings.py file. If postgres is not installed 
on your local machine, comment out the Database portion and uncomment the portion that refers to `sqlite`.
This will also work although `sql-lite` is not a production db.

To get python on your machine, you can follow these simple tutorials:

WINDOWS : https://phoenixnap.com/kb/how-to-install-python-3-windows

MAC: https://docs.python-guide.org/starting/install3/osx/

LINUX : https://docs.python-guide.org/starting/install3/linux/

## RESTFUL Endpoints
- `/profile/` supports GET, POST, PATCH, DELETE
- `/appointment/` supports GET, POST, PATCH, DELETE

An example postman collection is included in the repo under `postman_collection`

Example patient payload :
- ``{
        "id": 3,
        "name": "John",
        "phone": "0823083739",
        "email": "ashillc@gmail.com",
        "address": "1 mia drive, waterfall, johannesburg, 2090",
        "member_since": "2022-01-01",
        "picture": "http://localhost:8000/images/samson-idowu-q7WYYWHIACc-unsplash_ruhSfw6.jpg"
    }``

Example Appointment payload :
- ``{
    "id": 1,
    "date": "2022-05-10T00:00:00Z",
    "doctor": "Dr A Smit",
    "medical_speciality": "Urology",
    "branch_address": "1 test avenue, Johannesburg, 1111",
    "viewed": false,
    "name": 1
}``

### Notes, Considerations and Approach

- The only requirement that was provided was to build a python application that could pull information from 
a database and service a frontend. There are many ways this can be done but using DJANGO or FLASK first came to mind.
Flask is lightweight and enables rapid dev as compared to django but a lot of features e.g. database handling and model
creation are better implemented in django (Opinion)
- This app is based on django and does contain a docker file for containerization.
- A database backend was implemented.
- Unit test coverage can be viewed by running ``coverage run manage.py test awesome_clinic.tests
`` and then ``coverage report``