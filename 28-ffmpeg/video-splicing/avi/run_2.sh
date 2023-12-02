#!/bin/bash

input1=30-60frame
input2=30-60frame-2-crop

ffmpeg -i ${input1}.avi -i ${input2}.avi -filter_complex "[0:v][1:v]hstack=inputs=2[v]" -map "[v]" output.avi

