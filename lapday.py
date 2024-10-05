# import pandas as pd

# # Đọc dữ liệu từ file Excel
# data = pd.read_excel('D:/1.DH_TMMT/PPNCKH/code/ppnckh_drop_filled_median.xlsx')


# print(data.head())

# # Lấp đầy các giá trị null bằng giá trị trung vị của 10 giá trị gần đó cho các cột số
# numeric_columns = data.select_dtypes(include=['number']).columns
# data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].rolling(window=10, min_periods=1).median())

# # Hiển thị dữ liệu sau khi xóa cột và lấp đầy giá trị null
# print("\n lấp đầy giá trị null:")
# print(data.head())

# # Lưu dữ liệu đã xử lý vào file Excel mới
# data.to_excel('ppnckh_drop_filled_median1.xlsx', index=False)
import pandas as pd

# Đọc dữ liệu từ file Excel
data = pd.read_excel('D:/1.DH_TMMT/PPNCKH/code/ppnckh_drop.xlsx')

print("Dữ liệu trước khi lấp đầy giá trị null:")
print(data.head())

# Hiển thị số lượng giá trị null trong mỗi cột trước khi lấp đầy
nan_counts_before = data.isnull().sum()
print("\nSố lượng giá trị null trong mỗi cột trước khi lấp đầy:")
print(nan_counts_before)

# Lấp đầy các giá trị null bằng giá trị trung vị của 10 giá trị gần đó cho các cột số
numeric_columns = data.select_dtypes(include=['number']).columns

# Lặp cho đến khi không còn giá trị null nào
while data.isnull().any().any():  # Kiểm tra xem có giá trị null trong DataFrame không
    for col in numeric_columns:
        data[col] = data[col].fillna(data[col].rolling(window=1000, min_periods=1).median())
        # Hiển thị số lượng giá trị null trong mỗi cột trước khi lấp đầy
        nan_counts_before = data.isnull().sum()
        print("\nSố lượng giá trị null trong mỗi cột trước khi lấp đầy:")
        print(nan_counts_before)

# Sau khi lấp đầy trung vị, kiểm tra lại số lượng giá trị null
nan_counts_after = data.isnull().sum()
print("\nSố lượng giá trị null trong mỗi cột sau khi lấp đầy:")
print(nan_counts_after)

# Hiển thị dữ liệu sau khi lấp đầy giá trị null
print("\nDữ liệu sau khi lấp đầy giá trị null:")
print(data.head())

# Lưu dữ liệu đã xử lý vào file Excel mới
data.to_excel('ppnckh_drop_filled_median1.xlsx', index=False)
