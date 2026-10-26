# File: PetaniKopi.py
# Deskripsi: Subclass dari Manusia yang merepresentasikan petani kopi penghasil green beans,
#            memiliki relasi agregasi dengan daftar objek VarietasKopi.

from typing import List
from Manusia import Manusia
from VarietasKopi import VarietasKopi

class PetaniKopi(Manusia):
    def __init__(self, no_ktp: str = "", nama: str = "", alamat: str = "", tahun_awal_bertani: int = 0, list_varietas_kopi: List[VarietasKopi] = None):
        super().__init__(no_ktp, nama, alamat)
        self.__tahun_awal_bertani = tahun_awal_bertani
        self.__list_varietas_kopi = list_varietas_kopi if list_varietas_kopi is not None else []

    # Getter & Setter Tahun Awal Bertani
    def get_tahun_awal_bertani(self) -> int:
        return self.__tahun_awal_bertani

    def set_tahun_awal_bertani(self, tahun_awal_bertani: int) -> None:
        self.__tahun_awal_bertani = tahun_awal_bertani

    # Getter & Setter List Varietas Kopi
    def get_list_varietas_kopi(self) -> List[VarietasKopi]:
        return self.__list_varietas_kopi

    def set_list_varietas_kopi(self, list_varietas_kopi: List[VarietasKopi]) -> None:
        self.__list_varietas_kopi = list_varietas_kopi

    # Metode untuk menambah varietas kopi
    def tambah_varietas_kopi(self, varietas: VarietasKopi) -> None:
        self.__list_varietas_kopi.append(varietas)

    def __str__(self) -> str:
        varietas_str = ", ".join([v.get_nama() for v in self.__list_varietas_kopi]) if self.__list_varietas_kopi else "Belum ada varietas"
        return f"[Petani] {self.get_nama()} (KTP: {self.get_no_ktp()}, Alamat: {self.get_alamat()}, Mulai Tani: {self.__tahun_awal_bertani}) | Lahan Tanam: [{varietas_str}]"
