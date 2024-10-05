import pandas as pd

# Đọc dữ liệu từ file Excel
data = pd.read_excel('ppnckh.xlsx')

# Hiển thị dữ liệu trước khi xóa cột
print("Dữ liệu trước khi xóa cột:")
print(data.head())

# Xóa các cột prcp, snow, wpgt, tsun, coco
columns_to_drop = ['prcp', 'snow', 'wpgt', 'tsun', 'coco']
data = data.drop(columns=columns_to_drop)

# Hiển thị dữ liệu sau khi xóa cột
print("\nDữ liệu sau khi xóa cột:")
print(data.head())

# Lưu dữ liệu đã xử lý vào file Excel mới
data.to_excel('ppnckh_processed.xlsx', index=False)
