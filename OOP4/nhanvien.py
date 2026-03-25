class NhanVien:
    LUONG_MAX = 50000

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong

    def get_tenNhanVien(self):
        return self.__tenNhanVien

    def set_tenNhanVien(self, tenNhanVien):
        self.__tenNhanVien = tenNhanVien

    def get_luongCoBan(self):
        return self.__luongCoBan

    def set_luongCoBan(self, luongCoBan):
        self.__luongCoBan = luongCoBan

    def get_heSoLuong(self):
        return self.__heSoLuong

    def set_heSoLuong(self, heSoLuong):
        self.__heSoLuong = heSoLuong

    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong

    def tangLuong(self, giaTriTang):
        heSoMoi = self.__heSoLuong + giaTriTang
        luongMoi = self.__luongCoBan * heSoMoi
        if luongMoi > NhanVien.LUONG_MAX:
            print("❌ Lương vượt quá mức tối đa cho phép!")
            return False
        else:
            self.__heSoLuong = heSoMoi
            return True

    def inTTin(self):
        print(f"Tên nhân viên: {self.__tenNhanVien}")
        print(f"Lương cơ bản: {self.__luongCoBan}")
        print(f"Hệ số lương: {self.__heSoLuong}")
        print(f"Lương hiện tại: {self.tinhLuong()}")
nv1 = NhanVien("Nguyen Van A", 3000, 10)

nv1.inTTin()

print("\n👉 Thử tăng lương:")
nv1.tangLuong(5)
nv1.inTTin()
