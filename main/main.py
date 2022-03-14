import pandas as pd
from pathlib import Path

# 建立res資料夾路徑、csv檔案資料夾路徑
parent_path = Path(__file__).parents[1]
res_path = parent_path / 'res'
csv_path = res_path / 'my-experiment-file.csv'

# 讀取csv檔案
csi_data = pd.read_csv(csv_path)
# print(csi_data)
data_column_10 = csi_data['CSI_DATA'][10:11]
print(data_column_10)
