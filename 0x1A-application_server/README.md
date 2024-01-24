# Airbnb Application Server Configuration

## Introduction
This repository contains the configuration files and instructions for setting up the Airbnb application on a web server. The configuration is organized based on different tasks and services.

## Task 1: Setting up Development Environment
### Requirements
1. Ensure that task #3 of your SSH project is completed for web-01.
2. Install the net-tools package on your server: `sudo apt install -y net-tools`
3. Git clone your AirBnB_clone_v2 on your web-01 server.
4. Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.
   - Your Flask application object must be named `app`.

### Example
Window 1:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
```
Window 2:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```

## Task 2: Set up Production with Gunicorn
### Requirements
1. Install Gunicorn and any other libraries required by your application.
2. The Flask application object should be called `app`.
3. Serve the content from the same route as in the previous task.
4. Verify that it's working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.
5. Ensure that nothing is listening on port 6000.

### Example
Terminal 1:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
[2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
[2019-05-03 20:47:20 +0000] [3595] [INFO] Using worker: sync
[2019-05-03 20:47:20 +0000] [3598] [INFO] Booting worker with pid: 3598
```
Terminal 2:
```bash
ubuntu@229-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~$
```

## Task 3: Serve a Page with Nginx
### Requirements
1. Nginx must serve the page both locally and on its public IP on port 80.
2. Nginx should proxy requests to the process listening on port 5000.
3. Include your Nginx config file as `2-app_server-nginx_config`.
4. Spin up your production or development application server (listening on port 5000) to test.

### Example
On my server:
Window 1:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-06 20:43:57 +0000] [14026] [INFO] Starting gunicorn 19.9.0
[2019-05-06 20:43:57 +0000] [14026] [INFO] Listening at: http://0.0.0.0:5000 (14026)
[2019-05-06 20:43:57 +0000] [14026] [INFO] Using worker: sync
[2019-05-06 20:43:57 +0000] [14029] [INFO] Booting worker with pid: 14029
```
Window 2:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```
On my local terminal:
```bash
vagrant@ubuntu-xenial:~$ curl -sI 35.231.193.217/airbnb-onepage/
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 06 May 2019 20:44:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: keep-alive
X-Served-By: 229-web-01

vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-onepage/
Hello HBNB!vagrant@ubuntu-xenial:~$
```

## Task 4: Add a Route with Query Parameters
### Requirements
1. Nginx must serve this page both locally and on its public IP on port 80.
2. Nginx should proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to the process listening on port 5001.
3. Include your Nginx config file as `3-app_server-nginx_config`.
4. Spin up Gunicorn instances for both routes (port 5000 and port

 5001) to test.

### Example
Terminal 1:
```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app'
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
1684
1688

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5001/number_odd_or_even/6
<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 6 is even</H1></BODY>
</HTML>ubuntu@229-web-01:~/AirBnB_clone_v2
ubuntu@229-web-01:~$ 
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-dynamic/number_odd_or_even/5
<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 5 is odd</H1></BODY>
</HTML>ubuntu@229-web-01:~/AirBnB_clone_v2$
Local machine:
```bash
vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-dynamic/number_odd_or_even/6<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 6 is even</H1></BODY>
</HTML>vagrant@ubuntu-xenial:~$
```

## Task 5: Serve Your AirBnB Clone
### Requirements
1. Git clone your AirBnB_clone_v4.
2. Gunicorn should serve content from `web_dynamic/2-hbnb.py` on port 5003.
3. Setup Nginx so that the route `/` points to your Gunicorn instance.
4. Setup Nginx so that it properly serves the static assets found in `web_dynamic/static/`.
5. Reconfigure `web_dynamic/static/scripts/2-hbnb.js` to the correct IP.
6. Nginx must serve this page both locally and on its public IP on port 5003.

### Example
```bash
# Placeholder for the example
```
