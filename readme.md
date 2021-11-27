# Smart Refrigerator

A smart way to keep eye on your daily needs. In this project we propose a new way to TOBEADDED

## Prerequisites

* [Python 3.8](https://www.python.org/downloads/release/python-380/) 
* [Node.js & NPM](https://www.npmjs.com/package/download) latest version should be installed
* [Cuda](https://towardsdatascience.com/installing-tensorflow-with-cuda-cudnn-and-gpu-support-on-windows-10-60693e46e781) installation for Fast Performance


## Hardware Requirements

* Refrigerator with good white lighting
* IP WebCam preferably 8 MP or above
* Nvidia 1050 or above graphics card
* Browsers like Chrome / Mozilla
* TOBEADDED

## Setup

### Backend Setup:

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
$> cd SR-Backend
$> virtualenv venv
$> venv\Scripts\activate
(venv)$> cd SRB
(venv)$> pip install -r requirements.txt
```
Now we can start our backend.

```bash
(venv)$> python manage.py runserver
```
### Frontend Setup:
```bash
$> cd SR-Frontend
$> cd srf
$> npm install -g @angular/cli
$> npm i
```
Now start the Angular UI.
```bash
$> ng serve -o
```
Open port 4200 in your localhost:

![Main Screen](https://i.ibb.co/pzB7LbF/localhost-4200-home-1.png)