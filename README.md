# ReSpeaker Audio Extractor Demo

This is a demo implementing a use case for Speech Emotion Recognition, using a `Raspberry Pi 3 Model B+` and `ReSpeaker Mic Array v2.0`. The demo is a Python script that can be loaded in to continuously read audio incoming from the ReSpeaker and send API requests to SERaaS which then outputs emotions back.

SERaaS is a Final Year Project for [Waterford Institute of Technology](https://www.wit.ie/) developed by Wei Kit Wong, which aims to provide a Speech Emotion Recognition as a Web API service. This is achieved by Machine Learning to build the SER classification model; the [User Management Service](https://github.com/SERaaS/SERaaS-User-Management-Service) to provide authentication features, and the [API Service](https://github.com/SERaaS/SERaaS-API-Service) to deploy it all as a service.

## General

## Technologies Used

* *pyaudio* - Perform audio operations

## Usage

You can use the following commands in the terminal to run the demo;

1) `git clone https://github.com/SERaaS/ReSpeaker-Audio-Extractor-Demo.git` - Download the repository to your computer.

2) `cd respeaker-audio-extractor-demo` - Move to the demo folder.

3) `pip install -r requirements.txt` - Ensure you have all necessary dependencies installed (requires Python).

4) Create the missing files as defined below.

5) `python main.py` - Run the program.

### Missing Files

A `./seraasURLHandler.py` file is missing from the repo that you must create before running the program.

`./seraasURLHandler.py`
```python
# This is your own SERaaS API endpoint URL
endpoint = "http://????/analyse/????"
```
