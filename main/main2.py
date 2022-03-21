import numpy as np
import pandas as pd

x = pd.read_csv('my-experiment-file.csv')
x.columns = ["type", "role", "mac", "rssi", "rate", "sig_mode",
             "mcs", "bandwidth", "smoothing", "not_sounding", "aggregation",
             "stbc", "fec_coding", "sgi", "noise_floor", "ampdu_cnt",
             "channel", "secondary_channel", "local_timestamp", "ant", "sig_len",
             "rx_state", "real_time_set", "real_timestamp", "len", "CSI_DATA"]
# 取出 my-experiment-file.csv 檔案的所有 CSI_DATA
d = x[["CSI_DATA"]]
data_csi = np.array(d)
# print(d_csi)
# print(type(d_csi))

for i in data_csi:
    # print(i)
    data_str = "".join(i)
    data_frame = pd.Series(data_str)
    data_frame = data_str.replace("[", "")
    data_frame = data_str.replace("]", "")
    data_split = data_frame.split()
    data = pd.Series(data_split)
    data = data.str.replace("[", "")
    mylist = list(data)
    # mylist_1 = mylist[12:64]
    # print(mylist)
    result = np.array(mylist)
    print(result)

with open("output.txt", "w") as outputfile:
    outputfile.write("\t".join(mylist))

# data_9 = data_csi[9]
# data_str = "".join(data_9)
# data_frame = pd.Series(data_str)
# data_frame = data_str.replace("[", "")
# data_frame = data_str.replace("]", "")
# print(data_frame)
# print("--------------------------------------------")

# data_split = data_frame.split()
# print(data_split)
# print(len(data_split))
# print("--------------------------------------------")

# data = pd.Series(data_split)
# data = data.str.replace("[", "")
# print(data)
# print("--------------------------------------------")

# mylist = list(data)
# mylist.insert(2, "128")
# print(mylist[0])
# print(len(mylist))
# print("--------------------------------------------")

# result = np.array(mylist[::2])
# print(result)
# print(len(result))

# with open("output0.txt", "w") as csvfile:
#    csvfile.write("\n".join(result))
