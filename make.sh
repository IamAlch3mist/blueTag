#!/bin/bash

sudo rm -r ./blueTag-RP2040.uf2
sudo docker rm pico-builder-container

sudo docker build -t pico-builder-image .
sudo docker create --rm --name pico-builder-container pico-builder-image

sudo docker cp pico-builder-container:/project/src/build_rp2040/blueTag.uf2 ./blueTag-RP2040.uf2
#sudo docker cp pico-builder-container:/project/src/build_rp2350/blueTag.uf2 ./blueTag-RP2350.uf2

