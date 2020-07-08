#!/bin/bash

#rm -rf eps/* 

#python ./loop.py


cd eps

 
convert  hex-00.png  hex-03.png  hex-06.png  hex-08.png  hex-10.png   +append X1.png
convert  hex-12.png  hex-14.png  hex-16.png  hex-18.png  hex-20.png   +append X2.png
convert  hex-22.png  hex-24.png  hex-26.png  hex-28.png  hex-30.png   +append X3.png
convert  hex-32.png  hex-34.png  hex-36.png  hex-38.png  hex-40.png   +append X4.png
convert  hex-42.png  hex-44.png  hex-46.png  hex-48.png  hex-50.png   +append X5.png
convert  hex-52.png  hex-54.png  hex-56.png  hex-58.png  hex-60.png   +append X6.png
 
convert X1.png X2.png X3.png X4.png X5.png X6.png -append X0.png

