#!/bin/bash

uvicorn main:app --port 8989 & uvicorn main:static --port 8080