** How to install this app **

_docker-compose up_ 

The above command will install this app. You will see 4 containers started by this app. 
_shrine_mysql_ - This is the database app running mysql on port 3306
_shrine_fastapi_ - This is the backend fastapi framework, which runs on port 80 but exposes it at port 8000 on the host.
_shrine_react_ - This is yet to be setup. This app exposes port 3000 on the host.
_shrine_test_ - This is the pytest app which currently runs just one test cases. As the app progresses, more tests needs to be added here.

On sucessful deployment you will see the below message on the console. This is if you are running docker-compose in foreground (without -d option). If you used background option with -d, you can check the container logs using docker-compose logs, I think, not tried that yet.

_controlled startup_
The app comes up in a controlled manner. At first the shrine_mysql container comes up, only after sql is up and running on port 3306, does shrine_fastapi start. Once the shrine_react and shrine_test comes up only after uvicorn server in fastapi is up and running n localhost.

shrine_test       | test/test_shrine.py .                                                    [100%]
shrine_test       | 
shrine_test       | ============================== 1 passed in 0.09s ===============================


Once deployed, you will be able to use swagger UI to talk to the backend REST APIs setup on fastapi framework. The swagger UI will run on http://localhost:8000/docs. You will be able to update and view student database from here.

** How to use this app **

After the app is up and running, you can go to localhost:8000/docs to find the supported REST interfaces. Currently only two interfaces work, set and get Students. Rest of the app needs to be built.

For the UI, which is currently not working properly, you can go to localhost:3000. There is not much you can do there as it is not working properly.


** This section is for developers who wish to contribute to this project **
At the root of the source tree, you have two files this README.md and docker-compose.yml files. Rest of the source are organized into directories. The deploymet folder has all the dockerfiles. Currently it has four dockerfiles.

_shrine_app/deployment_
shrine_mysql - This picks the official Oracle's mysql image. The original initialization script has been modified to load initial schema required for shrines fastapi module. The changes are done such that user can specify the sql file to load through environment variable.

shrine_fastapi - This is the backend fastapi framework. This picks a popular public fastapi hello world image, asdkant/fastapi-hello-world and builds on top of that image. It installs the required dependencies for sqlalchemy and the python mysql connector. It also installs the nmap module, which checks for the dependent mysql database before starting the fastapi service.

shrine_react - Some more work needs to be done here. 

shrine_pytest - Pytest is a popular python unit test module, which is used to test the fastapi's REST interfaces. As of now just one test is functional and more tests needs to be added.

_shrine_app/backend_
This folder has the app files needed for the fastapi application.

_shrine_app/frontend_
This folder will have the files needed for the react application. This is still WIP.

_shrine_app/tools_
This folder has the generic tools needed for all the services. As of now we have a tool which checks if a given host has a port open. This is used by the fastapi container to check if mysql is up and running before fastapi starts and similarly, used by the pytest app to check if fastapi is up and running. Similar check will be required by the react app.


_docker-compose.yml_
This is the yaml file which is used for easy deployment at any site. The only requirement is docker and docker-compose installed, an internet connection and a docker hub account. Then just follow the instructions in the beginning of this page.


