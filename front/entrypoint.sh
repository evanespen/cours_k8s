#!/bin/bash

sed -i "s|http:\/\/localhost:8000\/|$API_URL|" /app/main.js;

cd /app;
python -m http.server ${PORT}