# Dockerizing a simple python weather app

### What will this app does?
This custom python scripts prompts the user to enter a valid city name and prints out the city's current temperature in Celcius.

## Steps to dockerize the weather app

1. Build the python app as shown in .\dockerizing-simple-python-app\python-weather-app.py
2. Build the Dockerfile as shown in .\dockerizing-simple-python-app\python-weatherapp.Dockerfile
3. Run the docker build command: ``` docker build -f python-weatherapp.Dockerfile -t python-weather-app-docker . ```
4. Run the docker image as a container in an interactive mode: ``` docker run -it python-weather-app-docker ```
5. Output:
```
PS D:\Github\docker\dockerizing-simple-python-app> docker run -it python-weather-app-docker
Enter the city name to fetch its temperature: Wellington
Wellington's current temperature is 14 degree (C).

PS D:\Github\docker\dockerizing-simple-python-app> docker run -it python-weather-app-docker
Enter the city name to fetch its temperature: Chennai
Chennai's current temperature is 29 degree (C).
```
6. Docker Container cleanups:
```
PS D:\Github\docker\dockerizing-simple-python-app> docker ps -a

CONTAINER ID   IMAGE                       COMMAND                  CREATED          STATUS               PORTS     NAMES
84d8dce20c3f   python-weather-app-docker   "python3 python-weat…"   10 minutes ago   Exited (0) 10 minutes ago             condescending_visvesvaraya
183fea94987d   python-weather-app-docker   "python3 python-weat…"   10 minutes ago   Exited (0) 10 minutes ago             cranky_booth

PS D:\Github\docker\dockerizing-simple-python-app> docker rm 84d 183f
84d
183f
```
7. Docker Image cleanups:
```
PS D:\Github\docker\dockerizing-simple-python-app> docker images
REPOSITORY                  TAG       IMAGE ID       CREATED          SIZE
python-weather-app-docker   latest    82416971c36e   12 minutes ago   593MB

PS D:\Github\docker\dockerizing-simple-python-app> docker rmi 824
Untagged: python-weather-app-docker:latest
Deleted: sha256:82416971c36e80091338325dbf1f242fe11897c0a925f8bc93537987821a7a1e
PS D:\Github\docker\dockerizing-simple-python-app>
```
