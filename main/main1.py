import csv
import pandas as pd
import numpy as np

with open('my-experiment-file.csv', newline='') as csvfile:
    # 讀取 CSV 檔案內容
    reader = csv.reader(csvfile)
    data_list = list(reader)

    # 輸出第十列的 CSI DATA
    # print(data_list[9][25])
    # print(type(data_list[9][25]))
    # print("--------------------------------------------")

    # 將 CSI DATA 轉成字串
    data_str = "".join(data_list[9][25])
    # print(data_str)
    # print(type(data_str))
    # print(len(data_str))
    # print("--------------------------------------------")

    # 將 String 轉成 Series
    data_frame = pd.Series(data_str)
    # print(data_frame)
    # print("--------------------------------------------")

    # 將 Series 轉成字串並分割
    data_frame = data_frame.str.replace("[", "")
    data_frame = data_frame.str.replace("]", "")
    data_split = data_frame.str.split()

    data = pd.Series(data_split)
    print(data)
    print("--------------------------------------------")

    # 將轉換成字串的 data 放進 list 裡
    mylist = list(data)
    mylist = mylist[0]
    print(mylist)
    print("--------------------------------------------")

    # 將 list 裡的值放到 array(陣列) 裡
    result = np.array(mylist)
    print(len(result))
    print("--------------------------------------------")

    # 印出想要的位數
    print(result[13:20])
    print("--------------------------------------------")
    # 印出奇數位
    print(result[::2])
    print("--------------------------------------------")
    # 印出偶數位
    print(result[1::2])
    print("--------------------------------------------")
