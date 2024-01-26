Final Project 

Overview

The primary goal of this project is to develop a Python API application using Flask. The project also incorporates the implementation of a Jenkins pipeline for testing the application, in conjunction with DinD. The codebase is hosted on GitHub to facilitate collaboration and easy access for the instructor.

Repository Information
The code for this project is stored in a GitHub repository. The repository structure includes three main branches:
main/master: This branch is essentially the deployment branch where the application will be published. Changes made and merged into this branch will trigger the deployment process.

develop:The development branch, where planning branches will be merged. Integration tests using the Python Requests library for API testing will be conducted in this branch.

feature: The planning and collaboration branch. In this branch, an environment for unit testing will be created using the unittest library. One test is sufficient to illustrate the functionality of the units.

Jenkins Pipeline

The project utilizes a Jenkins pipeline with automation tools for build, test, and deployment processes.

Testing Environment

Unit Tests:  
-Create an environment for running unit tests.
-Execute unit tests to ensure the functionality of specific features.

Integration Test: 
-Run integration tests using the Python Requests library to test the API.
-Integration tests serve as examples for connecting to the service and testing its functionality.
