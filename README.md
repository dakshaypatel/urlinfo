# **URL Lookup Service** - Malware or  No Malware

This is a microservice written using Python, Flask and MySql to achieve a simple functionality- to check weather a URL is Malware or Not. 
The decision is based on a database that contains a list of URLs and their informations.

## DB Design
We are using MySQL server for data storage.

**Table Name:** *url_infos*

| Field        | Type         | Null     | Key         | Default | Extra           |
|--------------|--------------|----------|-------------|---------|-----------------|
| url          | varchar(512) | NOT NULL | Primary Key |         |                 |
| malware_info | varchar(64)  | NOT NULL |             |         |                 |
| created_at   | timestamp    |          |             | NOW()   |                 |
| udated_at    | timestamp    |          |             | NOW()   | ON UPDATE NOW() |

**Create Table Command:**
```
CREATE TABLE url_infos(
    url VARCHAR(512) PRIMARY KEY, 
    malware_info VARCHAR(64) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW()
);
```
## Instructions to build and run:- 
### Requirements:-
- Python 3+
- pip3
- click
- Flask
- itsdangerous 
- Jinja2 
- MarkupSafe 
- mysqlclient 
- Werkzeug

### Instructions:-
1. Clone the project- 'https://github.com/dakshaypatel/urlinfo.git'
2. Go into the project folder- 'cd  urlinfo'
3. Install Dependent python modules - 'pip3 install click Flask itsdangerous Jinja2 MarkupSafe mysqlclient Werkzeug'
4. Run the app- 'python3 run.py'

## API Documentation:- 
You can also refer to the [Postman Collection here](https://www.getpostman.com/collections/7029f8e8d0cc426201ef).

1. **Get Url Info:** 

*GET* :  '/urlinfo/1/<hostname_and_port>/<original_path_and_query_string>'

**Response**: 
```
MALWARE/NOT_MALWARE
```
<img width="1790" alt="GET Request" src="https://user-images.githubusercontent.com/32039107/183448602-a10954fa-bad7-49bd-ad56-ebc1970b2b23.png">


2. **Update Url Details** 

*POST* : '/urlinfo'

**Header**:
```
-H 'content-type: application/x-www-form-urlencoded' \
```

**Body** : 
``
-d 'url=facebook.com&malware_info=NOT_MALWARE'
``

**Response**
```
SUCCESS
```

![POST Request](https://user-images.githubusercontent.com/32039107/183448705-98b06db7-c7be-48a4-b8ed-0d423b3ec0dd.png)

