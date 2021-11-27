# Smart Refrigerator

A smart way to keep eye on your daily needs. What would you do when you are out and need to peep into your refrigerator?

## Prerequisites

* [Python 3.8](https://www.python.org/downloads/release/python-380/) 
* [Node.js & NPM](https://www.npmjs.com/package/download) latest version should be installed
* [Cuda](https://towardsdatascience.com/installing-tensorflow-with-cuda-cudnn-and-gpu-support-on-windows-10-60693e46e781) installation for Fast Performance


## Hardware Requirements

* Refrigerator with good white lighting
* IP WebCam preferably 8 MP or above
* Nvidia 1050 or above graphics card
* Browsers like Chrome / Mozilla

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

![Main Screen](https://github.com/mukulbindal/imagesForReadme/blob/main/SRF-home.png?raw=true)

### Steps to use

#### Register:

The Refrigerator already has a webcam connected to a server. All refrigerator come with a unique ID associated with their IP Webcams. For demo, we can use (RF-100#) as the ID format.

![Register](https://github.com/mukulbindal/imagesForReadme/blob/main/Register.png?raw=true)

![Register](https://github.com/mukulbindal/imagesForReadme/blob/main/register-success.png?raw=true)
#### Login:
Upon successful registration, you need to collect the User ID to login and connect to your refrigerator from anywhere.

![Login](https://github.com/mukulbindal/imagesForReadme/blob/main/loginsuccess.png?raw=true)
#### My Refrigerator:
A live report of the food items present in your refrigerator can be accessed from your laptop, PC, mobile anywhere. The simple and flexible design makes the process smooth.

![Live Detection](https://github.com/mukulbindal/imagesForReadme/blob/main/smart-ref-live.png?raw=true)

<img src="https://github.com/mukulbindal/imagesForReadme/blob/main/localhost_4200_myref(Moto%20G4).png" width=100/>

### Full Demo Here:
(Coming soon)
### Future Improvements

* Detect the rotten/expired food items (based on how long they are in the box).
* Recommendation of healthier diet.
* Your daily consumption report for healthy/unhealthy food.

Any contributions are welcome!