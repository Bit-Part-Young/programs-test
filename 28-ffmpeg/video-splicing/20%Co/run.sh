#!/bin/bash

input_vn=415b-30-60
x=150

ffmpeg -i ${input_vn}.avi -filter:v "crop=out_w=in_w-2*${x}:out_h=in_h:x=${x}" ${input_vn}-crop.avi

