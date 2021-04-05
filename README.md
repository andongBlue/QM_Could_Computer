# QM_Could_Computer
mini project
## Introduction

**This is the mini project for group 20.**

What our group has done is a student registration system. This system is deployed in the cloud on AWS. This system can retrieve students' information and can be used to store students' information in our database and remove them from the database. In addition to that, the external [numverify API](https://numverify.com/documentation) can be passed to check if the phone number left by the student is correct.

The format of the student information is as follows.：

| student_id | first_name | last_name | phone_number | gender | nationality |
| ---------- | ---------- | --------- | ------------ | ------ | ----------- |
| 123123     | huihui     | liu       | 7529459987   | female | China       |
| 123124     | hehe       | li        | 7529462258   | female | US          |
| 123125     | zhenxiang  | shi       | 7529421102   | female | UK          |
| 123126     | shuaige    | xiao      | 7529316584   | male   | China       |
| 123127     | ming       | Chen      | 7529465582   | female | China       |

## Basic Functions

1. The application provides a dynamically generated REST API. The API must  have a sufficient set of services for the selected application domain.  The REST API responses must conform to REST standards (e.g. response  codes).  **3 Points**

   We provide a dynamic REST API for student information collection system. You can use `GET`, `POST` and `DELETE` to retrieve, add and delete student information from the database. This REST API conforms to the REST standard, for response codes, we have set up common situations. For example: 404 for pages not found, 200 for pages connected successfully.

2. The application makes use of an external REST service to complement its functionality. **3 Points**

   We have used the external REST service ([numverify API](https://numverify.com/documentation)) to improve our system functionality. numverify API can query whether a phone number is a real phone number or not. Here are the details of this external REST service.

   - NumVerify offers a full-featured yet simple RESTful JSON API for national and international phone number validation and information lookup for a total of 232 countries around the world.

   - After signing up, every user is assigned a personal API Access Key - a unique "password" used to make requests to the API. To authenticate with the numverify API, simply attach your `access_key` to the base endpoint URL:`http://apilayer.net/api/validate?access_key=YOUR_ACCESS_KEY `

   - All numverify validation data is returned in universal and lightweight JSON format. Find below a standard API result set: 

     ```json
     {
       "valid": true,
       "number": "14158586273",
       "local_format": "4158586273",
       "international_format": "+14158586273",
       "country_prefix": "+1",
       "country_code": "US",
       "country_name": "United States of America",
       "location": "Novato",
       "carrier": "AT&T Mobility LLC",
       "line_type": "mobile"
     }      
     ```

The meaning of each parameter is as follows.

   |         Object         |                         Description                          |
   | :--------------------: | :----------------------------------------------------------: |
   |        "valid"         |     Returns true if the specified phone number is valid.     |
   |        "number"        | Returns the phone number you specified in a clean format. (stripped of any special characters) |
   |     "local_format"     | Returns the local (national) format of the specified phone number. |
   | "international_format" | Returns the international format of the specified phone number. |
   |    "country_prefix"    | Returns the international country dial prefix for the specified phone number. |
   |     "country_code"     | Returns the 2-letter country code assigned to the specified phone number. |
   |     "country_name"     | Returns the full country name assigned to the specified phone number. |
   |       "location"       | If available, returns the location (city, state, or county) assigned to the specified phone number. |
   |       "carrier"        | Returns the name of the carrier which the specified phone number is registered with. |
   |      "line_type"       | Returns the line type of the specified phone number (See: Line Type Detection) |

3. The application uses a cloud database for accessing persistent information. **3 Points**

   We use Amazon Relational Database Service (Amazon RDS) for MySQL as our cloud database for accessing persistent information. See **config.py** for database configuration.
   
## The information of members

| Name           | Student ID |
| -------------- | ---------- |
| Boshi Zhang    | 200241520  |
| Huixiang Huang | 200258942  |
| Andong Chen    | 200645832  |
| Qiyue Zhang    | 200058205  |
| Yimeng Shao    | 200165880  |
