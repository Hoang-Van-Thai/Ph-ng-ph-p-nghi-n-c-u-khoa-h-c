
import pandas as pd
# Đọc dữ liệu từ file Excel
data = pd.read_excel('D:/1.DH_TMMT/PPNCKH/code/ppnckh_drop.xlsx')
print("Dữ liệu trước khi lấp đầy giá trị null:")
print(data.head())
nan_counts_before = data.isnull().sum()
print("\nSố lượng giá trị null trong mỗi cột trước khi lấp đầy:")
print(nan_counts_before)
numeric_columns = data.select_dtypes(include=['number']).columns
while data.isnull().any().any():  
    for col in numeric_columns:
        data[col] = data[col].fillna(data[col].rolling(window=1000, min_periods=1).median())
        nan_counts_before = data.isnull().sum()
        print("\nSố lượng giá trị null trong mỗi cột trước khi lấp đầy:")
        print(nan_counts_before)
nan_counts_after = data.isnull().sum()
print("\nSố lượng giá trị null trong mỗi cột sau khi lấp đầy:")
print(nan_counts_after)


print("\nDữ liệu sau khi lấp đầy giá trị null:")
print(data.head())


data.to_excel('ppnckh_drop_filled_median1.xlsx', index=False)
