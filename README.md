# 20261117---DE5M5

Nirosh was here - V2

Task:

1. Clone my repo using the HTTPs link (IN A SEPARATE FOLDER).
2. Download the data files and put them into your repo under a data folder.

# Day 3

AM Task: 
Write unit tests for the date duration function and anything else you may have.
You can use my solution instead of yours if you want.

P.S Best practise is to cover at least 80-90% of functions. 

# Day 4:

Task:
Build and run a docker container that uses our calculator and outputs 247/12.

Stretch 1: 
Try to persist the answers in a docker volume.

Stretch 2: 
Look into how you can create a SQL Lite DB with python. Try and write a simple table using Python.


If done, let me know in the chat. 

## Sol:

1. Create a new folder with a "Dockerfile" and a python app that does what you need.
2. Create the image: ```docker build -t mycontainername .```
3. Create the new vol: ```docker volume create myvolname```
4. Run the container with the image with the vol: ```docker run -v myvolname:/data mycontainername```

P.S You python app should write into a /data folder (this is what binds to our vol)

# TESTING CI PIPELINE.

Nirosh was here.