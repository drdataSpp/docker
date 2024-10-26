# Docker Beginner Challenges

This document contains a series of beginner challenges to help you learn Docker. For each challenge, follow the task and fill in your expected output.

Code Challenges Credits: https://www.perplexity.ai/
Input: "I am starting to learn Docker and I am an absolute beginner. Can you give me some beginner coding challenges, such as pulling an image, running a container, and deleting both a container and an image? The challenges should only provide the code challenges and expected output, without revealing the answers."

## Challenge 1: Pulling an Image

**Task:** Pull the official Python image from Docker Hub.

**Expected output:**
```
Using default tag: latest
latest: Pulling from library/python
...
Status: Downloaded newer image for python:latest
docker.io/library/python:latest
```

**Your Output:**
```
PS C:\Users\username> docker pull python

Using default tag: latest
latest: Pulling from library/python
7d98d813d54f: Pull complete
da802df85c96: Pull complete
7aadc5092c3b: Pull complete
ad1c7cfc347f: Pull complete
3cb0c7824817: Pull complete
6d4976a28162: Pull complete
7fd1c94ea9ec: Pull complete
Digest: sha256:a31cbb4db18c6f09e3300fa85b77f6d56702501fcb9bdb8792ec702a39ba6200
Status: Downloaded newer image for python:latest
docker.io/library/python:latest
```

---

## Challenge 2: Running a Container

**Task:** Run a container using the Python image you just pulled. Make it print "Hello, Docker!" and then exit.

**Expected output:**
```
Hello, Docker!
```

**Your Output:**
```
##Terminal 1:
PS C:\Users\username> docker run python sleep 100

##Termminal 2:
PS C:\Users\username> docker exec 5518e python -c "print('Hello, Docker!')"
Hello, Docker!
```

---

## Challenge 3: Listing Running Containers

**Task:** List all currently running containers.

**Expected output:**
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

**Your Output:**
```
PS C:\Users\username> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Users\username>
```

---

## Challenge 4: Listing All Containers

**Task:** List all containers, including stopped ones.

**Expected output:**
```
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                     PORTS     NAMES
abcdef123456   python    ...       2 minutes ago   Exited (0) 2 minutes ago             ...
```

**Your Output:**
```
PS C:\Users\username> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS                          PORTS     NAMES
5518e4327517   python    "sleep 100"   3 minutes ago   Exited (0) About a minute ago             ecstatic_moore
PS C:\Users\username>
```

---

## Challenge 5: Removing a Container

**Task:** Remove the Python container you created earlier.

**Expected output:**
```
abcdef123456
```

**Your Output:**
```
PS C:\Users\username> docker rm 5518e
5518e
PS C:\Users\username> docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Users\username>
```

---

## Challenge 6: Listing Images

**Task:** List all Docker images on your system.

**Expected output:**
```
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
python       latest    a5d7930b4e0f   2 weeks ago    917MB
```

**Your Output:**
```
PS C:\Users\username> docker images
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
python       latest    a4cb00e84832   7 days ago   1.02GB
PS C:\Users\username>
```

---

## Challenge 7: Removing an Image

**Task:** Remove the Python image you pulled earlier.

**Expected output:**
```
Untagged: python:latest
Untagged: python@sha256:...
Deleted: sha256:...
...
```

**Your Output:**
```
PS C:\Users\username> docker rmi python
Untagged: python:latest
Untagged: python@sha256:a31cbb4db18c6f09e3300fa85b77f6d56702501fcb9bdb8792ec702a39ba6200
Deleted: sha256:a4cb00e84832fc88a38893b00b15826ac0dc444e9874fe0353e2d73674477d1c
Deleted: sha256:3c14067a926376fab08075d0c12d2bfc44051f3047edafcd49f58e6c804634e6
Deleted: sha256:97419548464a5c18a39bafdb46b71e22ecb0b7988214f3a12974ee4415375fd6
Deleted: sha256:41e27bf88c6b820c28ef01b7a02317825453c1245661901e3d589329ee916922
Deleted: sha256:0dc99f3ce3bae9e0787aa2fec1bf44c5c482d244fc083585b4a60394218a1f17
Deleted: sha256:9d4eafd5fa9f85c5ab2a5ad25ff003d89abe0ff507be49a485ff887ad0ba1dcc
Deleted: sha256:022dfb72daa3a2542468d8f16f93eaed6eb84ab3df056804278fb781c85cd86d
Deleted: sha256:ef5f5ddeb0a6492f959cfdcfc6b0a3518e0a120db92e53ccb8225ee481e7a4a1
PS C:\Users\username>
```

---

## Challenge 8: Running a Container in Interactive Mode

**Task:** Run an Ubuntu container in interactive mode with a bash shell.

**Expected output:**
```
root@abcdef123456:/#
```

**Your Output:**
```
PS C:\Users\username> docker run -it ubuntu 
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
ff65ddf9395b: Pull complete
Digest: sha256:99c35190e22d294cdace2783ac55effc69d32896daaa265f0bbedbcde4fbe3e5
Status: Downloaded newer image for ubuntu:latest
root@75b08cd4e587:/#
```