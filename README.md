# rpi-train
Raspberry Pi Model Railway control

## Overview

This is a basic model railway train control application.
Created using Python GPIO Zero and Python Bottle.

## Hardware requirements

This is designed for a analogue model railway with DC motors. It could also be used to control other DC motors.

A H-Bridge motor controller is required. A L298N motor controller is recommended, although other controllers can be used depending upon your model railway power requirements.

You will also need a suitable DC power supply. Note if you have a power supply "wallwart" with your existing train set then it may be AC, in which case you would also need a full-bridge rectifier.
Instead I recommend a 12V DC power supply with sufficient current for all your trains (eg. a 2A should be sufficient for running two OO/HO trains).

## Wiring

The following pins should be used for connecting from the Raspberry Pi to the motor controller.
Note that only 1 train can be controlled using this version of the code, see later for details about the advanced version.

| Function   | GPIO numbers   | Physical pin   | Comments                |
| ---------- | -------------- | -------------- | ----------------------- |
| Train 1    |    17,18       |    11,12       |                         |
| Train 2    |    22,23       |    15,16       |                         |


Each train has 2 gpio numbers. The first is for forward, the second is for reverse. These can be switched depending upon how the motor is wired to the track.


## Pre-requisites

Install Bottle using
    sudo apt install python3-bottle


## Install

Create directory /opt/train
And change ownership to your own username (replace <username>)

    sudo mkdir /opt/train
    sudo chown <username>: /opt/train

Create directory /opt/train/public
    mkdir /opt/train/public

Save the file train.py into /opt/train
Save the file index.html into /opt/train/public

Run the program using
    python3 train.py

## Advanced version

This progam is created as a tutorial for The MagPi magazine. For a version with more features and an improved interface see the [PenguinTutor model railway pages](http://www.penguintutor.com/projects/model-railway) or [Model Railway code on GitHub](https://github.com/penguintutor/model-railway)

