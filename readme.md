# Flask simple rest api

## Table of Content

- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Useful Commands](#useful-commands)
- [Features](#features)
- [Example](#example)

## Requirements

- Python
- Flask library

## Getting started

```bash
git clone https://github.com/JonathanAlex1/flask-simple-restapi flask-simple-restapi
cd flask-simple-restapi
python app.py
```

## Useful Commands

- `python app.py` - starts a dev server and opens browser with running app

## Features

- use of API google maps

## Example
- Test the api Using the URL, with this body:'{"text": "Crazy Burger"}'
   in local: `localhost:4000/find-place`, or 
  prod: `https://eflask-app-rest.herokuapp.com/find-place`
  Will return the following result:
```json
{
  "candidates": [
      {
        "formatted_address": "Av. Capitán Alonso de León, Zaragoza, 67563 Montemorelos, N.L., México",
        "geometry": {
          "location": {
          "lat": 25.1893329,
          "lng": -99.84431470000001
        },
        "viewport": {
          "northeast": {
            "lat": 25.19072037989272,
            "lng": -99.84296292010728
          },
          "southwest": {
            "lat": 25.18802072010727,
            "lng": -99.84566257989273
          }
        }
      },
      "name": "Crazy Burguer",
      "opening_hours": {
        "open_now": true
      },
      "rating": 4.3
    }
  ],
  "status": "OK"
}
```
  test by curl text:
  
```bash
curl --location --request POST 'localhost:4000/find-place' \
--header 'Content-Type: application/json' \
--data-raw '{
  "text": "Crazy Burger"
}'
```

