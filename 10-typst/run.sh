#!/bin/bash

file="main.typ"

typst compile ${file} --font-path fonts

cp main.pdf typst-learning.pdf
