import pandas as pd


data = pd.read_excel('ppnckh.xlsx')
print("Dữ liệu trước khi xóa cột:")
print(data.head())
columns_to_drop = ['prcp', 'snow', 'wpgt', 'tsun', 'coco']
data = data.drop(columns=columns_to_drop)
print("\nDữ liệu sau khi xóa cột:")
print(data.head())


data.to_excel('ppnckh_processed.xlsx', index=False)
