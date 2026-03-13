def diem_trung_binh(ds):
    tong = 0
    dem = 0

    for diem in ds.values():
        tong = tong + diem
        dem = dem + 1

    return tong / dem


# Dictionary lưu tên sinh viên và điểm
sinh_vien = {
    "An": 8,
    "Binh": 7,
    "Chi": 9
}

tb = diem_trung_binh(sinh_vien)

print("Điểm trung bình của các sinh viên là:", tb)