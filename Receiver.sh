#!/bin/bash

sudo apt -y install python-pip 
pip install azure
pip install azure-servicebus==0.20.2
python Receiver.py
