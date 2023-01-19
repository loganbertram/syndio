#Employees Endpoint

##Installatiion
To get started, clone this repository and and run `pip3 install -r requirements.txt`.

##Configuation
The port is configuable and may be set by running `export PORT=[port]`. By default, the application will run on port
5050 if no port is provided or if the provided port is invalid. Following TCP port conventions for user server ports,
port should be an integer value between 1024 and 49151, the standard range of ports for user server applications.

##Run
To run, execute `python3 app.py`. You should see something like `Running on http://127.0.0.1:[port]`.

##Testing
To interact with the running application, execute `curl localhost:$PORT/employees`.