# Getting Started with PyQlik / CDSW

This baseline project shows how to use Python to connect to the Qlik Sense QIX Engine API from within a Cloudera Data Science Workbench environment.

## Files

Modify the default files to get started with your own project.

* `TestPyQlik.py` -- Script to execute example methods against the cloudera.qlik.com Qlik Sense demo server
* `pyqlikengine` -- Folder containing the python module code for interacting with the Qlik Sense QIX engine. It is maintained here: https://github.com/qliknln/pyqlikengine
* `TestPyQlikHelper.py` -- Script which uses helper methods to greatly simplify the code. More to come!

## How to get it going

* `Login` -- Visit http://cdsw.cloudera.qlik.com and if you don't already have an account on this server, click "Sign Up for a New Account". If you already have an account then log in
* Create a New Project -- Click blue button "New Project" on the upper right section of the page after logging in
* Give the project a name, click Git in the "Initial Setup" area, and paste the URL of this GitHub repository (https://github.com/Qlik-PE/CDSW_QlikSense.git) and click Create Project
* You will now see the project workspace. Initially you will see a list of files, some workspace areas on the left, and a button on the top right that reads "Open Workbench". Click that button, "Open Workbench" 
* You will be asked which Engine Kernel you want to use, click "Python 2", leave the rest defaults, and click Launch Session. This will start up a docker instance to do your work in. Once started, click "Open in Workbench"
* When the session has started, it will take you into the workbench interface to run code. On the left, you will see the files imported from GitHub. Click on the file "TestPyQlik.py"
* Upon entering the TestPyQlik.py script in the Workbench, the first thing you will need to do is install the required packages. You can do this by selecting the top portion of the TestPyQlik.py script - "!pip install -r requirements.txt", and right click and choose "Run Line(s)"
* Code will be displayed, and you will have an option to run the code.. On the menu bar just above the code, click on the black play symbol to run all of the code at one time. If you want to simply run sections of the code, you can select a section, right click, and choose "Run Line(s)"

## Roadmap

* More Helper functions to simplify code

* Render Qlik visualizations

* Collaboration / deployment options:

    1. Web page / mashup sharing (similar to Shiny, uses Qlik Sense API’s)
    2. Create/open app & load data results from Impala at end of pipeline
    3. Deploy to AAI
