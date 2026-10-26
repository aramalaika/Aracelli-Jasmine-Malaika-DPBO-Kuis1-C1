# File: SupplierAlatKopi.py
# Deskripsi: Subclass dari EntitasBisnis yang merepresentasikan perusahaan pemasok alat kopi,
#            memiliki relasi agregasi dengan daftar objek AlatKopi.

from typing import List
from EntitasBisnis import EntitasBisnis
from AlatKopi import AlatKopi

class SupplierAlatKopi(EntitasBisnis):
    def __init__(self, kode_supplier: str = "", nama: str = "", alamat: str = "", list_alat_kopi: List[AlatKopi] = None):
        super().__init__(kode_supplier, nama, alamat)
        self.__list_alat_kopi = list_alat_kopi if list_alat_kopi is not None else []

    # Getter & Setter Kode Supplier
    def get_kode_supplier(self) -> str:
        return self.get_kode_entitas()

    def set_kode_supplier(self, kode_supplier: str) -> None:
        self.set_kode_entitas(kode_supplier)

    # Getter & Setter List Alat Kopi
    def get_list_alat_kopi(self) -> List[AlatKopi]:
        return self.__list_alat_kopi

    def set_list_alat_kopi(self, list_alat_kopi: List[AlatKopi]) -> None:
        self.__list_alat_kopi = list_alat_kopi

    # Metode untuk menambah alat kopi ke katalog supplier
    def tambah_alat_kopi(self, alat: AlatKopi) -> None:
        self.__list_alat_kopi.append(alat)

    def __str__(self) -> str:
        alat_str = ", ".join([a.get_nama() for a in self.__list_alat_kopi]) if self.__list_alat_kopi else "Belum ada alat"
        return f"[Supplier] [{self.get_kode_supplier()}] {self.get_nama()} ({self.get_alamat()}) | Katalog Alat: [{alat_str}]"
