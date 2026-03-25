import time
so_giay_hien_tai = int(time.time())
days = so_giay_hien_tai // 86400
so_giay_con_lai = so_giay_hien_tai % 86400
hours = so_giay_con_lai // 3600
minutes = (so_giay_con_lai % 3600) // 60
seconds = so_giay_con_lai % 60
print("So ngay da troi qua tu 1/1/1970:", days)
print("Thoi gian hien tai:", hours, "gio", minutes, "phut", seconds, "giay")
