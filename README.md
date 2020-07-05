# Tableau-Pyton-Dashboard

This repo contains instruction to deploy a Python function to sue it in Tableau throught tabpy and tabpy_client.

The intention is to ilustrate hte use of the tabpymodule for Tableau Python integration.

## Step 1

Download the required files.

* lr_midel.sav
* lr-model.py
* Event Clasifier.twbx

## Step 2

Install all the required modules in Python, you can use pip.

* numpy
* pandas
* sklearn
* pickle
* tabpy
* tabpy_client

## Step 3

Start TabPy, just write tabpy in terminal.

## Step 4

Configure analytics extensions connection in Tableau.

* Go to Help menu.
* Then select Settings and Performance.
* Then manage External Service connection. This will open the External Service Connection dialog box.
* Select TabPy/External API in Select an External Service.
* Select localhost as Server.
* Specify the port 9004 as Port.
* Test hte connection.
* Click OK.

## Step 5

Deploy the model

Just update the lr_model.sav file path and run lr-model.py

## Step 6

Adding the script to the dashboard

Open the workbook.
Go to predictions Sheet.
Describe Model measure.
Copy the script in teh comment.
Edit Model measure.
Replace the current calculation with the copied script.
Clik OK.
Set Cell in Prediction dimension's Compute using property.

## Have fun