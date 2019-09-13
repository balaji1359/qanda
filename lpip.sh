#!/bin/bash

TARGET_DIR=vendor

pip3.7 install -t $TARGET_DIR --upgrade $@
rm -fr $TARGET_DIR/*.{dist,egg}-info
rm -fr $TARGET_DIR/__pycache__
