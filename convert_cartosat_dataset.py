import json
import os
import sys
# from PIL import Image
import re

os.chdir(r'Z:\BITS_Pilani\YoloV8\json files')
# for fname in os.listdir():
#     test = os.path.splitext(fname)[0]
#     fp = open(test+".txt", "w")

#### Old categories
# map={11:0, 12:1, 13:2, 15:3,
#     17:4, 18:5, 19:6, 20:7, 21:8,
#     23:9, 24:10, 25:11, 26:12,27:13,
#     28:14, 29:15, 32:16,
#     33:17, 34:18, 35:19, 36:20, 37:21,
#     38:22, 40:23, 41:24, 42:25, 44:26, 45:27,
#     47:28, 49:29, 50:30, 51:31, 52:32,
#     53:33, 54:34, 55:35, 56:36,
#     57:37, 59:38, 60:39, 61:40, 62:41,
#     63:42, 64:43, 65:44, 66:45, 71:46,
#     72:47, 73:48, 74:49, 76:50, 77:51, 79:52,
#     83:53, 84:54, 86:55, 89:56, 91:57,
#     93:58, 94:59,75:60,82:61}


# maplst = [73]
# map = {73:0}

map = {"building":0, "buildings":0, "vegetation":1, "metro station": 2, "railway station":3, "agriculture and grassland": 4, "agriculture and grasslands":4, "Agriculture":4, "bare ground and vacant plots": 5, "bare ground and vacant plot": 5, "bare land and vacant plot": 5, "bare ground/vacant plots":5, "bare ground/vacant plot": 5, "bare land/vacant plots":5, "water bodies":6, "water body":6, "plane": 7, "planes":7, "stadium":8, "airport hangar": 9}

for fname in os.listdir():
    if fname.endswith(".json"):
        f = open(fname)
        data = json.load(f)
        test = os.path.splitext(fname)[0]
        fp = open(test+".txt", "w")
        lst=data['shapes']
        for i in lst:
            bb = i['points']
            x1 = bb[0][0]
            x2 = bb[1][0]
            # print(bb)
            # print(x1, x2)
            type_id=map[i['label']]
            y1 = bb[0][1]
            y2 = bb[1][1]
            x_center = ((x1 + x2) / 2) / 1280
            y_center = ((y1 + y2) / 2) / 1280
            width = (x2 - x1) / 1280
            height = (y2 - y1) / 1280
            fp.write(f'{type_id} {x_center} {y_center} {width} {height}\n')

        fp.close()
    f.close()
                
                
                # # Assuming class '0' for all, replace or modify as necessary
                # out.write(f'0 {x_center} {y_center} {width} {height}\n')

        # fp = open("labels.txt", "r")
        # for fname in os.listdir():
        #     if not fname.endswith(".jpg"):
        #         continue
        #     print(fname)
        #     image = Image.open(fname)
        #     lines = fp.readlines()
        #     for row in lines:
        #         # check if string present on a current line

        #         #print(row.find(word))
        #         # find() method returns -1 if the value is not found,
        #         # if found it returns index of the first occurrence of the substring
        #         if row.find(fname) != -1:
        #             print('string exists in file')
        #             print('line Number:', lines.index(row))
            



        # os.chdir(r'C:\Users\kriti\OneDrive\Desktop\ps\JPEG')