<p align="center">
  <img width="200" src="https://github.com/Mufumi/Udacity-Optimizing-a-ML-Pipeline-in-Azure-Tutorial/blob/main/Azure%20Ml.jpg" alt="Azure Ml">
</p>

# Operationalizing Machine Learning in Azure

## Overview
This project is part of the Udacity Azure ML Nanodegree.
In this project we initialize, configure and deploy a Machine Learning model in MS Azure. The 

### Authentication

A crucial component of ML Ops is managing authentication of who has access to services in the environment. To ensure authentication can configured, the user has to ensure the Azure CLI is operational in the host machine. The Azure CLI is a cross-platform command-line tool that can be installed locally on Linux computers. The CLI on Linux allows the execution of various commands through a terminal using interactive command-line prompts or a script. Once the Azure CLI is installed and enabled, the user is expected to check the service principal has been activated. For this task, I used the machine provided by the lab and therefore did not go through any authentication process. It is crucial however to understand the fundamentals of authentication in ML Pipelines.  

### Set up Auto ML experiment

Once authentication is complete, the user can proceed to create the Auto ML run with the relevant dataset and initiate an Auto ML experiment. For this excercise we used the Bankmarketing dataset. This dataset contains customer data that is going to be used to find the best strategies to improve for the next marketing campaign. The aim is to deploy a model that will predict the effectiveness of the current marketing campaign. This experiment was conducted on a Standard_DS12_V2 compute cluster.

### Deploy best model

For the deployment of the best performing model, the Azure Container Instance was utilized with authentication enabled. This authentication is critical as a control measure in the ML Ops framework.

### Enable logging

### swagger
### consume endpoints

### Create, publish and consume pipeline
Apache Benchmark (ab): Works with authentication keys to 


## Application architectural diagram

## Future work

## Deploying model in Azure studio

*Screencast goes here*

Using Azure Studio

[![Deploying a model using Azure Studio](Screenshot (240).png)](https://youtu.be/0wKgqIJLtgQ)

## Publish an ML Pipeline

With Python SDK
[![Deploying a model using Azure Python_SDK](Screenshot (240).png)](https://youtu.be/EDPTXV3oGIA)



