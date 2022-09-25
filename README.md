https://pythonbasics.org/flask-tutorial-hello-world/

Tested this on ubuntu:

`apt-get update -y && apt-get upgrade -y`

`apt-get install python3 -y && apt-get install python3-pip -y`

`git clone -b webapp-flask https://github.com/DIGITALAPPLICATION/python3-webapps.git`
`cd python3-webapps`

`pip install -r requirements.txt`

`output: Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.2 click-8.1.3 flask-2.2.2 importlib-metadata-4.12.0 itsdangerous-2.1.2`

`python3 sam.py`

```
 * Serving Flask app 'sam'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:81
 * Running on http://10.0.0.4:81
Press CTRL+C to quit
49.37.130.119 - - [25/Sep/2022 08:00:45] "GET / HTTP/1.1" 200 -
49.37.130.119 - - [25/Sep/2022 08:00:46] "GET / HTTP/1.1" 200 -
49.37.130.119 - - [25/Sep/2022 08:00:47] "GET / HTTP/1.1" 200 -
49.37.130.119 - - [25/Sep/2022 08:00:47] "GET / HTTP/1.1" 200 -
49.37.130.119 - - [25/Sep/2022 08:00:48] "GET / HTTP/1.1" 200 -
```

open browser and check http://localhost:81 or http://{publicIp}:81



