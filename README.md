https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli


Tested this on ubuntu:

`apt-get update -y && apt-get upgrade -y`

`apt-get install python3 -y && apt-get install python3-pip -y`

`git clone -b 5-webapp-flask-azureapp https://github.com/DIGITALAPPLICATION/python3-webapps.git`
`cd python3-webapps`

`pip install -r requirements.txt`

`output: Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.2 click-8.1.3 flask-2.2.2 importlib-metadata-4.12.0 itsdangerous-2.1.2`

`python3 app.py`

```
 * Serving Flask app 'sam'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.0.4:5000
Press CTRL+C to quit
49.37.130.119 - - [25/Sep/2022 08:00:45] "GET / HTTP/1.1" 200 -
49.37.130.119 - - [25/Sep/2022 08:00:46] "GET / HTTP/1.1" 200 -
49.37.130.119 - - [25/Sep/2022 08:00:47] "GET / HTTP/1.1" 200 -
49.37.130.119 - - [25/Sep/2022 08:00:47] "GET / HTTP/1.1" 200 -
49.37.130.119 - - [25/Sep/2022 08:00:48] "GET / HTTP/1.1" 200 -
```

open browser and check http://localhost:5000 or http://{publicIp}:5000

Ctrl+c = stop the lcoally runnign app at the same port 5000

once local testing completed, try deploy to azure

https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

`curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`

```
az login

//this will create a default webapp azure service, defaulr service plan, defaukt resource grouo with sku B1 plan
//also, code will be deployed from current directory to azure webapp service
az webapp up --runtime PYTHON:3.9 --sku B1 --logs --location "North Europe"

output:
The webapp 'ambitious-dune-b61b498b8be7402cbb5cba66ae358d69' doesn't exist
Creating Resource group 'narayanas87_rg_0073' ...
Resource group creation complete
Creating AppServicePlan 'narayanas87_asp_9165' ...
Creating webapp 'ambitious-dune-b61b498b8be7402cbb5cba66ae358d69' ...
Configuring default logging for the app, if not already enabled
Creating zip with contents of dir /root/msdocs-python-django-webapp-quickstart ...
Getting scm site credentials for zip deployment
Starting zip deployment. This operation can take a while to complete ...
Deployment endpoint responded with status code 202
BuildRequestReceived...          Success!
BuildPending...                  Success!
BuildInProgress...               Success!

Your application is running.

You can launch the app at http://ambitious-dune-b61b498b8be7402cbb5cba66ae358d69.azurewebsites.net

------------------------------------------

If you already have webpp, rg, service plan, etc, then zip the code and deploy (there are many approaches apart from zip menthod)

zip -r azure-python-webapp.zip . -x '.??*'

az webapp config appsettings set \
    --resource-group webapp_rg_0073 \
    --name my-python-webap \
    --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true
	

az webapp deploy --type zip \
    --name my-python-webap \
    --resource-group webapp_rg_0073 \
    --src-path azure-python-webapp.zip 


```

open browser and check http://my-python-webap.azurewebsites.net




