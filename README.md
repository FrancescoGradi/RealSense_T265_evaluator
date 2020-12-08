# RealSense_T265_evaluator
In this work we tested the **Intel® RealSense™ Tracking Camera T265** functionality and evaluate data acquisition reliability in different settings. Particularly, the aim is provide a clear and simple report that can be used for future studies or experiments.
The experiments were done indoors and outdoors and were classified as follows: 
- Short range experiments (1m) 
- Medium range experiments (5-15m) 
- Long range experiments (50-100m) 
- Very long range experiments (> 100m) 
- Rotation experiments

![output](https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/RealSense_Fisheye.gif)

## Getting started
To get a local copy up and running follow these simple steps.
### Prerequisites

**Hardware**
- [Intel® RealSense ™ Tracking Camera T265](https://www.intelrealsense.com/tracking-camera-t265/)
- [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/?resellerType=home) (recommended) or [Raspberry Pi 3B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/?resellerType=home)

**Software**
- [Intel RealSense SDK](https://www.intelrealsense.com/developers/)
- pyrealsense2 2.33.1
- numpy 1.16.2
- matplotlib 3.1.1

### Installation
1. Follow [these](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_raspbian.md) instructions for the Raspberry Pi set-up
2. Clone and import the repo in Raspberry Pi
3. Open the `Test` folder and choose the right file to do your experiments (if you have an LCD touchscreen to connect to the Raspberry, you can use the GUI to manage the files, but remember to install PyQt 5.15.1)

## Results
The following table shows a short description of our results, for more details see the [report](https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/relazione.pdf).

For all experiments it is advisable to wait for a camera stabilization time of 5-10 seconds

| Short Range | Medium Range | Long Range | Very Long Range | Rotation
| :---: | :---: | :---: | :---: | :---: |
| <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/miastanza.png" width=" 170" height=auto> | <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/terrazzo_medium.png" width="170" height=auto> | <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/stanzone.png" width=" 170" height=auto> | <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/pista.png" width="370" height=auto> | <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/YawPitchRoll.png" width="170" height=auto> |
| <ul align="left"><li> **indoor**: unstable performance, huge changes at minimal setup variation</li><li> **outdoor**: generally more stable and accurate track</li></ul> <img width=800/> | <ul align="left"><li> path detected very well, very distant references allow the camera to perform better tracking</li><li>visible swaying of the steps</li></ul> <img width=200/> | <ul align="left"><li>the extended environment improves tracking compared to previous cases</li><li>start and end of tracking match</li></ul> <img width=700/> | <ul align="left"><li>path found, but start and end of tracking do not match</li><li>good sensitivity to speed and acceleration changes</li></ul> <img width=700/> | <ul align="left"><li>precise pitch and roll rotation</li><li>a good yaw measurement requires higher rotation speed</li></ul> <img width=600/>|

In conclusion, the results obtained by the camera are highly dependent on the environment used. A broader view brings improvement.
