# File: Barista.py
# Deskripsi: Subclass dari Manusia yang merepresentasikan peracik/penyeduh kopi profesional,
#            memiliki relasi agregasi dengan daftar MenuKopi yang dikuasainya.

from typing import List
from Manusia import Manusia
from MenuKopi import MenuKopi

class Barista(Manusia):
    def __init__(self, no_ktp: str = "", nama: str = "", alamat: str = "", level_sertifikasi: str = "beginner", list_menu_kopi: List[MenuKopi] = None):
        super().__init__(no_ktp, nama, alamat)
        self.__level_sertifikasi = level_sertifikasi
        self.__list_menu_kopi = list_menu_kopi if list_menu_kopi is not None else []

    # Getter & Setter Level Sertifikasi
    def get_level_sertifikasi(self) -> str:
        return self.__level_sertifikasi

    def set_level_sertifikasi(self, level_sertifikasi: str) -> None:
        self.__level_sertifikasi = level_sertifikasi

    # Getter & Setter List Menu Kopi
    def get_list_menu_kopi(self) -> List[MenuKopi]:
        return self.__list_menu_kopi

    def set_list_menu_kopi(self, list_menu_kopi: List[MenuKopi]) -> None:
        self.__list_menu_kopi = list_menu_kopi

    # Metode untuk menambah penguasaan menu kopi
    def tambah_menu_kopi(self, menu: MenuKopi) -> None:
        self.__list_menu_kopi.append(menu)

    def __str__(self) -> str:
        menu_str = ", ".join([m.get_nama() for m in self.__list_menu_kopi]) if self.__list_menu_kopi else "Belum ada menu"
        return f"[Barista] {self.get_nama()} (KTP: {self.get_no_ktp()}, Sertifikasi: {self.__level_sertifikasi}) | Penguasaan Menu: [{menu_str}]"
