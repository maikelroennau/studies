#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
sudo apt-get install libgtkglext1 libgtkglext1-dev
mkdir OpenCV
cd OpenCV
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout 3.2.0
mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_EXAMPLES=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D WITH_TBB=ON  -D WITH_OPENCL=ON -D WITH_OPENGL=ON -D WITH_TBB=ON -D WITH_IPP=ON -D WITH_V4L=ON ..
make -j8
sudo make install
pkg-config --modversion opencv
