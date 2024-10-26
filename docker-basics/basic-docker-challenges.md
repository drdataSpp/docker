# Docker Beginner Challenges

This document contains a series of beginner challenges to help you learn Docker. For each challenge, follow the task and fill in your expected output.

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
[Your answer here]
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
[Your answer here]
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
[Your answer here]
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
[Your answer here]
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
[Your answer here]
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
[Your answer here]
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
[Your answer here]
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
[Your answer here]
```