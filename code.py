from datetime import datetime, timedelta

class ThuCung:
    def __init__(self, ten, loai, lich_su_kham=None, lich_su_vaccine=None):
        self.ten = ten
        self.loai = loai
        self.lich_su_kham = lich_su_kham if lich_su_kham else []
        self.lich_su_vaccine = lich_su_vaccine if lich_su_vaccine else []

    def them_ho_so_kham(self, ho_so):
        self.lich_su_kham.append(ho_so)

    def them_ho_so_vaccine(self, ho_so):
        self.lich_su_vaccine.append(ho_so)

    def hien_thi_thong_tin(self):
        print(f"Thu cưng: {self.ten}, Loai: {self.loai}")
        print("Lich su kham benh:")
        for record in self.lich_su_kham:
            print(f"  - {record}")
        print("Lich su vaccine:")
        for record in self.lich_su_vaccine:
            print(f"  - {record}")

class CuocHen:
    def __init__(self, thu_cung, ngay, bac_si=None):
        self.thu_cung = thu_cung
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.bac_si = bac_si
        self.trang_thai_thanh_toan = False

    def dat_cuoc_hen(self, thanh_toan):
        self.trang_thai_thanh_toan = thanh_toan
        print(f"Cuoc hen da duoc dat cho {self.thu_cung.ten} vao {self.ngay.strftime('%d/%m/%Y')}")
        if thanh_toan:
            print("Thanh toan da duoc nhan.")
        else:
            print("Thanh toan chua hoan tat.")

    def huy_cuoc_hen(self, so_ngay_truoc):
        if so_ngay_truoc >= 7:
            hoan_tien = "hoan lai 100%"
        elif 3 <= so_ngay_truoc < 7:
            hoan_tien = "hoan lai 75%"
        else:
            hoan_tien = "khong hoan tien"
        print(f"Cuoc hen da duoc huy. {hoan_tien} da duoc hoan lai.")
        self.trang_thai_thanh_toan = False

class NhanVien:
    def __init__(self):
        self.da_dang_nhap = False
        self.bac_si = ["Dr. Smith", "Dr. Johnson"]
        self.phong = ["Phong A", "Phong B", "Phong C"]

    def dang_nhap(self, ten_dang_nhap, mat_khau):
        """Dang nhap cho nhan vien."""
        if ten_dang_nhap == "staff" and mat_khau == "password":
            self.da_dang_nhap = True
            print("Dang nhap thanh cong!")
        else:
            print("Dang nhap that bai. Vui long thu lai.")

    def hien_thi_menu(self):
        """Hien thi menu chuc nang cho nhan vien sau khi dang nhap."""
        if not self.da_dang_nhap:
            print("Vui long dang nhap truoc.")
            return
        
        while True:
            print("\n--- Menu Quan ly Cham soc Thu Cung ---")
            print("1. Quan ly thong tin chuong (phong)")
            print("2. Quan ly cac booking va xu ly huy booking")
            print("3. Quan ly thong tin thu cưng nhap vien")
            print("4. Sap lich cho bac si thu y (kham truc tiep)")
            print("5. Sap lich cho bac si thu y cham soc thu cưng nhap vien")
            print("6. Thoat")

            choice = input("Chon chuc nang (1-6): ")

            if choice == "1":
                self.quan_ly_phong()
            elif choice == "2":
                self.quan_ly_booking()
            elif choice == "3":
                self.quan_ly_thu_cung_nhap_vien()
            elif choice == "4":
                self.sap_lich_bac_si_kham()
            elif choice == "5":
                self.sap_lich_bac_si_cham_soc_nhap_vien()
            elif choice == "6":
                print("Thoat khoi he thong.")
                break
            else:
                print("Lua chon khong hop le, vui long chon lai.")
    
    def quan_ly_phong(self):
        """Quan ly thong tin chuong (phong)."""
        print("Quan ly thong tin chuong (phong). Cac chuong co san: ", self.phong)
        action = input("Ban muon them chuong moi (them/xoa)? ")
        if action == "them":
            room_name = input("Nhap ten chuong moi: ")
            self.phong.append(room_name)
            print(f"Chuong {room_name} da duoc them.")
        elif action == "xoa":
            room_name = input("Nhap ten chuong muon xoa: ")
            if room_name in self.phong:
                self.phong.remove(room_name)
                print(f"Chuong {room_name} da duoc xoa.")
            else:
                print("Chuong khong ton tai.")
    
    def quan_ly_booking(self):
        """Quan ly cac booking va xu ly huy booking."""
        print("Quan ly booking.")
        pet_name = input("Nhap ten thu cưng: ")
        pet = ThuCung(pet_name, "Cho")  # Gia su day la mot thu cưng voi ten va loai xac dinh
        appointment_date = input("Nhap ngay hen kham (dd/mm/yyyy): ")
        appointment = CuocHen(pet, appointment_date)
        payment_status = input("Da thanh toan chua? (y/n): ") == "y"
        appointment.dat_cuoc_hen(payment_status)
        
        cancel = input("Ban co muon huy booking? (y/n): ")
        if cancel == "y":
            days_before = int(input("Nhap so ngay truoc khi huy: "))
            appointment.huy_cuoc_hen(days_before)

    def quan_ly_thu_cung_nhap_vien(self):
        """Quan ly thong tin thu cưng nhap vien (luu chuong)."""
        print("Quan ly thong tin thu cưng nhap vien.")
        pet_name = input("Nhap ten thu cưng nhap vien: ")
        kennel = input("Chon chuong cho thu cưng (Phong A, Phong B, Phong C): ")
        if kennel in self.phong:
            print(f"Thu cưng {pet_name} da duoc luu trong chuong {kennel}.")
        else:
            print("Chuong khong ton tai.")
    
    def sap_lich_bac_si_kham(self):
        """Sap lich cho bac si thu y (kham truc tiep)."""
        print("Sap lich kham cho bac si thu y.")
        pet_name = input("Nhap ten thu cưng: ")
        veterinarian = input("Chon bac si thu y (Dr. Smith, Dr. Johnson): ")
        appointment_date = input("Nhap ngay hen kham (dd/mm/yyyy): ")
        pet = ThuCung(pet_name, "Cho")
        appointment = CuocHen(pet, appointment_date, veterinarian)
        payment_status = input("Da thanh toan chua? (y/n): ") == "y"
        appointment.dat_cuoc_hen(payment_status)

    def sap_lich_bac_si_cham_soc_nhap_vien(self):
        """Sap lich cho bac si thu y cham soc thu cưng nhap vien."""
        print("Sap lich cho bac si thu y cham soc thu cưng nhap vien.")
        pet_name = input("Nhap ten thu cưng nhap vien: ")
        veterinarian = input("Chon bac si thu y (Dr. Smith, Dr. Johnson): ")
        appointment_date = input("Nhap ngay cham soc thu cưng (dd/mm/yyyy): ")
        pet = ThuCung(pet_name, "Cho")
        appointment = CuocHen(pet, appointment_date, veterinarian)
        print(f"Thu cưng {pet_name} se duoc cham soc boi {veterinarian} vao ngay {appointment_date}.")

# Su dung chuong trinh
staff = NhanVien()

# Dang nhap vao he thong
username = input("Nhap ten nguoi dung: ")
password = input("Nhap mat khau: ")
staff.dang_nhap(username, password)

# Hien thi menu sau khi dang nhap
staff.hien_thi_menu()
