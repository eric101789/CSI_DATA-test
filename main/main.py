import pandas as pd
from pathlib import Path

# 建立res資料夾路徑、csv檔案資料夾路徑
parent_path = Path(__file__).parents[1]
res_path = parent_path / 'res'
csv_path = res_path / 'my-experiment-file.csv'

# 讀取csv檔案
csi_data = pd.read_csv(csv_path)
# print(csi_data)

csi_data['CSI_DATA'] = pd.Series(csi_data['CSI_DATA'], dtype="string")  # 輸出資料型別為DataFrame(二維資料)
csi_data_10 = csi_data['CSI_DATA'][10:11]  # 輸出資料型別為Series(一維資料)
print(csi_data_10)
csi_data_10 = csi_data_10.str.replace("[", "")
csi_data_10 = csi_data_10.str.replace("]", "")
split_data = csi_data_10.str.split()  # 將資料轉為字串並切分
print(split_data)
data = pd.Series(split_data)
print(data)

# 選取特定資料片段(第十列CSI_DATA)
# data_column_10 = csi_data['CSI_DATA'][10:11]
# print(data_column_10)
