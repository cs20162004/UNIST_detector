# UNIST Logo Detector

## Description
This is a yolov3-tiny object detection model that can identify UNIST (Ulsan National Institute of Science and Technology) logo withing the given image with 84.13% mean average precision. The model was trained using darknet yolov3-tiny. 
### Result
![Darknet Logo](https://raw.githubusercontent.com/cs20162004/UNIST_detector/main/images/output2.jpg)

### Dependencies
Install the Tkinter package
```sh
$ apt-get install python3-tk
```

### How to run the model on your own image:
Clone to your local repository 
```sh
$ git clone https://github.com/cs20162004/UNIST_detector.git
$ cd UNIST_detector
```
Run the detector.py
```sh
$ python3 detector.py
```
Then, choose your image
