#!/usr/bin/env bash
cd
git clone --branch picamera2 https://github.com/raspberrypi/libcamera.git
cd libcamera
pip install ply
pip install pyyaml
meson build
ninja -C build install
cd
git clone https://github.com/tomba/kmsxx.git
cd kmsxx
git submodule update --init
sudo apt install -y libfmt-dev libdrm-dev
meson build
ninja -C build
cd
git clone https://github.com/RaspberryPiFoundation/python-v4l2.git
cd
sudo pip3 install pyopengl
sudo apt install -y python3-pyqt5
git clone https://github.com/raspberrypi/picamera2.git
cd
sudo apt install -y python3-opencv
sudo apt install -y opencv-data
