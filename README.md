# mileapp BACKEND DEVELOPER TEST

##Installation
```bash
cd untitled
pip install -r requirements.txt 
```
##Create Database
```bash
sudo -u postgres psql
CREATE DATABASE mileapp;
CREATE USER mileapp with encrypted password 'mileapp123';
GRANT ALL PRIVILEGES ON DATABASE mileapp to mileapp;
```
##Run Django server
if you don't have Virtual Environment, please install it first.
To activate virtual environment:
```bash
source venv/bin/activate
./manage.py migrate
./manage.py runserver
```
Then the server will run.

##CRUD
Follow this link
```bash
http://localhost:8000/api/package
http://localhost:8000/api/package/:uri
```

##CRUD SAMPLE
I recommend to try with Postman <br/><br/>
To get all data: <br/>
METHOD: GET<br/>
http://localhost:8000/api/package <br/>
http://localhost:8000/api/package/:uri <br/><br/>

To create new record: <br/>
METHOD: POST<br/>
http://localhost:8000/api/package <br/>
body: https://pastebin.pl/view/b7ad42cb <br/><br/>

To update record: <br/>
METHOD: PUT<br/>
http://localhost:8000/api/package/:uri <br/>
body: https://pastebin.pl/view/660d03ce <br/><br/>

To update single or more record column: <br/>
METHOD: PUT (because django supported partial update i'm not gonna use PATCH)<br/> 
http://localhost:8000/api/package/:uri <br/>
body: <br/>
```bash
{
    "customer_name": "PT.COBACOBA INDONESIA",
    "transaction_amount": 1000000
}
```



##SQL to mock data
Just run it on your dbms tool
https://pastebin.pl/view/c68921f8

#Unit Test

##Installation
```bash
cd rest-api-test
npm-install
```

##Usage
Open the ```api-test.js```, adjust the ```order id``` variable then open your terminal and type ```mocha api-test.js --timeout 100000```
