import csv
import pandas as pd
import numpy as np
from pathlib import Path

parent_path = Path(__file__).parents[1]
res_path = parent_path / 'res'
csv_path = res_path / 'my-experiment-file.csv'
with open(csv_path, newline='') as csvfile:
    # 讀取 CSV 檔案內容
    reader = csv.reader(csvfile)
    data_list = list(reader)

    # 輸出第十列的 CSI DATA
    # print(data_list[9][25])
    # print(type(data_list[9][25]))
    # print("--------------------------------------------")

    # 將 CSI DATA 轉成字串
    data_str = "".join(data_list[9][25])  # 透過 join() 連接 string 來串接起來
    data_str2 = "".join(data_list[10][25])
    # print(data_str)
    # print(type(data_str))
    # print(len(data_str))
    # print("--------------------------------------------")

    # 將 String 轉成 Series
    data_frame = pd.Series(data_str)
    data_frame2 = pd.Series(data_str2)
    # print(data_frame2)
    # print("--------------------------------------------")

    # 將 Series 轉成字串並分割
    data_frame = data_frame.str.replace("[", "")
    data_frame = data_frame.str.replace("]", "")
    data_split = data_frame.str.split()

    data_frame2 = data_frame2.str.replace("[", "")
    data_frame2 = data_frame2.str.replace("]", "")
    data_split2 = data_frame2.str.split()

    data = pd.Series(data_split)
    data2 = pd.Series(data_split2)
    # print(data)
    # print(data2)
    # print("--------------------------------------------")

    # 將轉換成字串的 data 放進 list 裡
    mylist = list(data)
    mylist = mylist[0]
    # print(mylist)
    # print("--------------------------------------------")

    mylist2 = list(data2)
    mylist2 = mylist2[0]
    # print(mylist2)
    # print("--------------------------------------------")

    # 將 list 裡的值放到 array(陣列) 裡
    result = np.array(mylist)
    result2 = np.array(mylist2)
    # print(result)
    # print(len(result))
    # print("--------------------------------------------")

    # 印出想要的位數
    a = result[0:12]
    a2 = result2[0:12]
    # print(a)
    b = result[12:64]
    b2 = result2[12:64]
    # print(b)
    c = result[64:66]
    c2 = result2[64:66]
    # print(c)
    d = result[66:118]
    d2 = result2[66:118]
    # print(d)
    e = result[118:128]
    e2 = result2[118:128]
    # print(e)
    # print("--------------------------------------------")
    # 印出奇數位
    # print(result[::2])
    # print("--------------------------------------------")
    # 印出偶數位
    # print(result[1::2])
    # print("--------------------------------------------")

with open("output1.txt", "w") as csvfile:
    csvfile.write(" ".join(a))
    csvfile.write("\n")
    csvfile.write(" ".join(a2))
with open("output2.txt", "w") as csvfile:
    csvfile.write(" ".join(b))
    csvfile.write("\n")
    csvfile.write(" ".join(b2))
with open("output3.txt", "w") as csvfile:
    csvfile.write(" ".join(c))
    csvfile.write("\n")
    csvfile.write(" ".join(c2))
with open("output4.txt", "w") as csvfile:
    csvfile.write(" ".join(d))
    csvfile.write("\n")
    csvfile.write(" ".join(d2))
with open("output5.txt", "w") as csvfile:
    csvfile.write(" ".join(e))
    csvfile.write("\n")
    csvfile.write(" ".join(e2))
