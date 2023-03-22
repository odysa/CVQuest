#!/bin/bash

<<<<<<< HEAD
uvicorn main:app --port 8989 & 
uvicorn main:static --host 0.0.0.0 --port 8080 &
sleep infinity
=======
uvicorn main:little_nginx --host "0.0.0.0" --port 8080
>>>>>>> 903a89335b7e9bd2cdffaf6079ba881c13ffa5b9
