#!/bin/bash

input1=100b-30-60
input2=415b-30-60-crop

ffmpeg -i ${input1}.avi -i ${input2}.avi -filter_complex "[0:v][1:v]hstack=inputs=2[v]" -map "[v]" output.avi

