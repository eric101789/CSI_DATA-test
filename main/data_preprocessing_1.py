# -*- coding: utf-8 -*-
"""
SMS採樣方式的數據整理
把採樣到的.DB轉成.CSV，放在同一個目錄下然後執行這個檔案
需要另外製作XYZ座標點的.CSV檔案，row的數量需要等同於.db檔案的數量
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
from nva import nva

#改變目前工作目錄, 把要整理的.csv檔案放在一起
os.chdir('C://Users//hungh//Creative Cloud Files//A02-教學//101-大學部專題//2021-呂玟錡//python_code')
#os.chdir('C://Users//hhliu//Creative Cloud Files//A02-教學//101-大學部專題//2021-呂玟錡//python_code')

#讀入座標檔案
path = os.getcwd()
df1 = pd.read_csv('座標.csv')
xyz = df1.loc[:, ['route', 'Xstart', 'Ystart', 'Zstart(floor)', 'Xend', 'Yend', 'Zend(floor)']].values

#os.chdir('C://Users//hungh//Creative Cloud Files//A02-教學//101-大學部專題//2021-呂玟錡//python_code//2021_8_WiFi_database')
  
# use glob to get all the csv files 
# in the folder
path = path + '\\2021_8_WiFi_database'
csv_files = glob.glob(os.path.join(path, "*.csv"))

#建立初始化矩陣
x_2G = np.empty([0, 11])
x_5G = np.empty([0, 11])

RP_ID = 0
file_number = 0

ap24_list = []
ap50_list = []

    
# loop over the list of csv files
for f in csv_files:
    #讀入.csv檔案
    df = pd.read_csv(f)
    
    #修改venueName內容
    df['venueName'] = xyz[file_number][0]

    #取得xyz開始與結束座標    
    coordinate = [[xyz[file_number][1], xyz[file_number][2], xyz[file_number][3]], 
                  [xyz[file_number][4], xyz[file_number][5], xyz[file_number][6]]]
    
    number_of_pace = df['TRACK'].iloc[-1]
    
    x_gap = (coordinate[1][0] - coordinate[0][0]) / (number_of_pace - 1)  # 有可能是負值或零
    y_gap = (coordinate[1][1] - coordinate[0][1]) / (number_of_pace - 1)  # 有可能是負值或零
    z_gap = (coordinate[1][2] - coordinate[0][2]) / (number_of_pace - 1)  # 有可能是負值或零
    
    file_number += 1
    
    
    # 增加新欄位
    new_col = 'rp_id'
    df.insert(3, new_col, 0)  # 調整欄位順序用
    
    # 加入RP ID
    df[new_col] = df.TRACK.apply(lambda x: x + RP_ID)
    RP_ID = df[new_col].iloc[-1]
    # 增加新欄位
    new_col = 'x'
    df.insert(4, new_col, 0)  # 調整欄位順序用
    df[new_col] = df.TRACK.apply(lambda x: coordinate[0][0] + (x-1)*x_gap)
    new_col = 'y'
    df.insert(5, new_col, 0)  # 調整欄位順序用
    df[new_col] = df.TRACK.apply(lambda x: coordinate[0][1] + (x-1)*y_gap)
    new_col = 'z'
    df.insert(6, new_col, 0)  # 調整欄位順序用
    df[new_col] = df.TRACK.apply(lambda x: coordinate[0][2] + (x-1)*z_gap)
    
    
    
    #以BSSID和TRACK排序
    df = df.sort_values(by=['BSSID', 'TRACK'])   
    
    #把需要的欄位取出來
    x = df.loc[:, ['rp_id', 'BSSID', 'SSID', 'frequency', 'level', 'ttimestamp', 'onReceiveTime', 'venueName', 'x', 'y', 'z']].values
    
    #設定過濾器，只保留'TANetRoaming'跟'iCYCU'
    isCampusWiFi = np.logical_or(x[:,2] == 'TANetRoaming', x[:,2] == 'iCYCU')
    x = x[isCampusWiFi]
    
    x_2G = np.append(x_2G, x[x[:,3] < 3000], axis=0)
    x_5G = np.append(x_5G, x[x[:,3] > 3000], axis=0)
    
    x_2G_shaped = x_2G.copy()
    x_5G_shaped = x_5G.copy()
    
    # 進行波形整形算法
    # 考慮NVA, GPR, RLOWESS, ...
    ap2list =[]
    for i in x_2G[:,1]:
        if i not in ap2list:
            ap2list.append(i)   #加入目前路線的aplist
            if i not in ap24_list:
                ap24_list.append(i)     #加入整棟建築物的aplist, 2.4G
                
            index = np.where(x_2G[:,1] == i)    
            rssi = [x_2G[index, 0], x_2G[index, 4]]     #理論上，是已經按照採樣順序排序好的
            
            s_rssi = nva(rssi, 7)
            x_2G[index, 4] = rssi
            
            # print(rssi)
            pass
        pass
            
    pass
            

    

    
    

 


