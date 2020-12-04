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
The following table shows a short description of our results, for more details see the [report](link)

| Short Range | Medium Range | Long Range | Very Long Range| Rotation
| :---: | :---: | :---: | :---: | :---: |
| <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/miastanza.png" width=" 170" height="170"> | <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/stanzone.png" width="170" height="170"> | <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/giardino.png" width=" 170" height="170"> | <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/pista.png" width="170" height="160"> | <img src="https://github.com/FrancescoGradi/RealSense_T265_evaluator/blob/master/demoImages/YawPitchRoll.png" width="170" height="170"> |
| commento risultati | commento risultati | commento risultati | commento risultati | commento risultati |
