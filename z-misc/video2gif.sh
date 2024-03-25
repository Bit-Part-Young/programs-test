#!/bin/bash

input=input
output_tmp=output_video
output=output

ffmpeg -i ${input}.mp4 -c:v copy -an ${output_tmp}.mp4

ffmpeg -i ${output_tmp}.mp4 -vf "fps=10,scale=320:-1:flags=lanczos" -c:v gif -f gif ${output}.gif

rm ${output_tmp}.mp4

echo "video to gif done!"

