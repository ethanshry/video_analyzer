import cv2
import numpy as numpy

import os
import subprocess

FRAMERATE = 240

HSV = (78, 7.8, 100)

for filename in os.listdir('./in'):
    parts = filename.split('.')
    subprocess.run(['mkdir', f'./out/{parts[0]}'])
    subprocess.run(['cp', f'./in/{filename}', f'./out/{parts[0]}/{filename}'])
    subprocess.run(
        ['ffmpeg', '-i', filename, 'thumb%010d.png', '-hide_banner'],
        cwd=f'./out/{parts[0]}')
    subprocess.run(['rm', f'./out/{parts[0]}/{filename}'])

    for frame in os.listdir(f'./out/{parts[0]}'):
        print(frame)
        img = cv2.imread(f'./out/{parts[0]}/{frame}')
        #img = cv2.resize(img, (int(img.shape[1] / 4), int(img.shape[0] / 4)),
        #                 interpolation=cv2.INTER_AREA)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (70, 0, 90), (110, 40, 150))
        thresh = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(f'./out/test/thresh-{frame}', thresh)