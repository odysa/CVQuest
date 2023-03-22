#!/bin/bash

uvicorn main:app --port 8989 & 
uvicorn main:static --host 0.0.0.0 --port 8080 &
sleep infinity