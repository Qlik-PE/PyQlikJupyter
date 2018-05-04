# Getting Started with PyQlik / Jupyter / Docker

This baseline project shows how to use Python to connect to the Qlik Core Engine API from within a Jupyter notebook environment, leveraging Docker containers.

## Files

Modify the default files to get started with your own project.

* `TestPyQlik.py` -- Script to execute example methods against Qlik Core
* `pyqlikengine` -- Folder containing the python module code for interacting with the Qlik Core engine. 
* `TestPyQlikHelper.py` -- Script which uses helper methods to greatly simplify the code. More to come!

## How to get it going

* In an OS running Docker (tested using Centos on AWS), do a git clone of this repository, Enter the folder you just cloned
* Run `docker-compose up` (NOTE: `-d` is not specified because we want to see the login token that was generated) .. this will fetch the 2 docker images - one for jupyter and one for qlik-core and start them. You will see this inside of a yellow section: "..to login with a token: http://localhost:8888/?token=c29db141690934599c987325d3828f37019c3032258b63e7" (note localhost- this is NOT the hostname you'll use)
* Run `docker ps -a` and you will see the containers and what ports they are running on. Jupyter is set to run on 8889 and qlik core is set to run on 9077 (make sure you open the appropriate firewall ports!)
* Copy the token string above! Log in to the host from the outside (not localhost obviously) and paste in the token string. Set a password, this makes things easier!
* 

## Troubleshooting
* If you want to manually do things in the jupyter container such as setting a new password, you can get to a bash prompt inside the container by running this: `sudo docker exec -it 5a072f8ab67d /bin/bash`
* If you want to stop all containers, do this: `sudo docker stop $(sudo docker ps -q)` .. if you want to remove those containers to start over, run this: `sudo docker rm $(sudo docker ps -aq)`

## Roadmap

* More Helper functions to simplify code

* Render Qlik visualizations

* Collaboration / deployment options:

    1. Web page / mashup sharing (similar to Shiny, uses Qlik Sense API’s)
    2. Create/open app & load data results from Impala at end of pipeline
    3. Deploy to AAI
