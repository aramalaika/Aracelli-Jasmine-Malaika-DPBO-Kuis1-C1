# File: RoasterKopi.py
# Deskripsi: Subclass dari EntitasBisnis yang merepresentasikan perusahaan pemanggang biji kopi,
#            memiliki relasi agregasi dengan daftar objek VarietasKopi.

from typing import List
from EntitasBisnis import EntitasBisnis
from VarietasKopi import VarietasKopi

class RoasterKopi(EntitasBisnis):
    def __init__(self, kode_roaster: str = "", nama: str = "", alamat: str = "", metode_roasting: str = "medium", list_varietas_kopi: List[VarietasKopi] = None):
        super().__init__(kode_roaster, nama, alamat)
        self.__metode_roasting = metode_roasting
        self.__list_varietas_kopi = list_varietas_kopi if list_varietas_kopi is not None else []

    # Getter & Setter Kode Roaster (Spesifik entitas roaster)
    def get_kode_roaster(self) -> str:
        return self.get_kode_entitas()

    def set_kode_roaster(self, kode_roaster: str) -> None:
        self.set_kode_entitas(kode_roaster)

    # Getter & Setter Metode Roasting
    def get_metode_roasting(self) -> str:
        return self.__metode_roasting

    def set_metode_roasting(self, metode_roasting: str) -> None:
        self.__metode_roasting = metode_roasting

    # Getter & Setter List Varietas Kopi
    def get_list_varietas_kopi(self) -> List[VarietasKopi]:
        return self.__list_varietas_kopi

    def set_list_varietas_kopi(self, list_varietas_kopi: List[VarietasKopi]) -> None:
        self.__list_varietas_kopi = list_varietas_kopi

    # Metode untuk menambah varietas kopi yang diroasting
    def tambah_varietas_kopi(self, varietas: VarietasKopi) -> None:
        self.__list_varietas_kopi.append(varietas)

    def __str__(self) -> str:
        varietas_str = ", ".join([v.get_nama() for v in self.__list_varietas_kopi]) if self.__list_varietas_kopi else "Belum ada varietas"
        return f"[Roaster] [{self.get_kode_roaster()}] {self.get_nama()} ({self.get_alamat()}) | Profil Roasting: {self.__metode_roasting} | Varietas Biji: [{varietas_str}]"
