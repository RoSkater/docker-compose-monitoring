# DOCKER-COMPOSE MONITORING

The aim of this project is to play around with Docker-Compose, Dockerfiles (Flask app), Grafana and Prometheus

<br>

## TOOLS

[![My Skills](https://skillicons.dev/icons?i=docker,flask,prometheus,grafana)](https://skillicons.dev)

<br>

## WORKFLOW
The Prometheus Instance makes requests to the Flask App */metrics* endpoint so the data then can be displayed in the Grafana container UI:

**Flask APP** -- (GET http://flask-app/metrics) --> **Prometheus** --> **Grafana**

<br>

## LAUNCH DOCKER COMPOSE
Make sure you are in the same directory as the *docker-compose.yml* and use the following command to launch the containers compose:

```
sudo docker-compose up
```