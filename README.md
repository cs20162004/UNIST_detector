# UNIST Logo Detector

## Description
This is a yolov3-tiny object detection model that can identify UNIST (Ulsan National Institute of Science and Technology) logo withing the given image with 84.13% mean average precision. The model was trained using darknet yolov3-tiny. 
### Result
![Darknet Logo](https://raw.githubusercontent.com/cs20162004/UNIST_detector/main/images/output2.jpg)

## Dependencies
Install the Tkinter package
```sh
$ apt-get install python3-tk
```
Clone to your local repository 
```sh
$ git clone https://github.com/cs20162004/UNIST_detector.git
$ cd UNIST_detector
```
### Run detector on Ubuntu:

Run the detector_ubuntu.py
```sh
$ python3 detector_ubuntu.py
```
Then, choose your image

### Run detector on Mac:

Run the detector_mac.py
```sh
$ python3 detector_mac.py
```
Then, choose your image

## References

- [You only look once: Unified, real‐time object detection.](https://arxiv.org/abs/1506.02640)
Redmon, J.; Divvala, S.; Girshick, R.; Farhadi, A. You only look once: Unified, real‐time object detection. In
Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, Las Vegas, NV, USA,
26 June–1 July 2016; pp. 779–788

- [TF-YOLO: An Improved Incremental Network for Real-Time Object Detection.](https://www.mdpi.com/2076-3417/9/16/3225/htm)
He, & Huang, Chang-Wei & Wei, Liqing & Li, Lingling & Anfu, Guo. (2019). TF-YOLO: An Improved Incremental Network for Real-Time Object Detection. Applied Sciences. 9. 3225. 10.3390/app9163225.

- J. Redmon. Darknet: Open source neural networks in c.
http://pjreddie.com/darknet/, 2013–2016.

- [Yolo9000: Better, faster, stronger.](https://arxiv.org/abs/1612.08242)
J. Redmon and A. Farhadi. Yolo9000: Better, faster, stronger.
In Computer Vision and Pattern Recognition (CVPR), 2017
IEEE Conference on, pages 6517–6525. IEEE, 2017.

- [Yolov3: An incremental improvement.](https://arxiv.org/abs/1804.02767)
J. Redmon and A. Farhadi. Yolov3: An incremental improvement. arXiv, 2018.
