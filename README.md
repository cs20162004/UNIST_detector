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

### References

J. Redmon. Darknet: Open source neural networks in c.
http://pjreddie.com/darknet/, 2013–2016.

J. Redmon and A. Farhadi. Yolo9000: Better, faster, stronger.
In Computer Vision and Pattern Recognition (CVPR), 2017
IEEE Conference on, pages 6517–6525. IEEE, 2017.

J. Redmon and A. Farhadi. Yolov3: An incremental improvement. arXiv, 2018.
