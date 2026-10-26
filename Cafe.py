# File: Cafe.py
# Deskripsi: Subclass dari EntitasBisnis yang merepresentasikan kedai kopi/kafe,
#            memiliki relasi agregasi dengan MenuKopi dan Barista,
#            serta relasi komposisi dengan UlasanKopi.

from typing import List
from EntitasBisnis import EntitasBisnis
from MenuKopi import MenuKopi
from Barista import Barista
from UlasanKopi import UlasanKopi

class Cafe(EntitasBisnis):
    def __init__(self, kode_cafe: str = "", nama: str = "", alamat: str = "", jenis_cafe: str = "specialty",
                 list_menu_kopi: List[MenuKopi] = None, list_barista: List[Barista] = None,
                 list_ulasan_kopi: List[UlasanKopi] = None):
        super().__init__(kode_cafe, nama, alamat)
        self.__jenis_cafe = jenis_cafe
        self.__list_menu_kopi = list_menu_kopi if list_menu_kopi is not None else []
        self.__list_barista = list_barista if list_barista is not None else []
        self.__list_ulasan_kopi = list_ulasan_kopi if list_ulasan_kopi is not None else []

    # Getter & Setter Kode Cafe
    def get_kode_cafe(self) -> str:
        return self.get_kode_entitas()

    def set_kode_cafe(self, kode_cafe: str) -> None:
        self.set_kode_entitas(kode_cafe)

    # Getter & Setter Jenis Cafe
    def get_jenis_cafe(self) -> str:
        return self.__jenis_cafe

    def set_jenis_cafe(self, jenis_cafe: str) -> None:
        self.__jenis_cafe = jenis_cafe

    # Getter & Setter List Menu Kopi
    def get_list_menu_kopi(self) -> List[MenuKopi]:
        return self.__list_menu_kopi

    def set_list_menu_kopi(self, list_menu_kopi: List[MenuKopi]) -> None:
        self.__list_menu_kopi = list_menu_kopi

    def tambah_menu_kopi(self, menu: MenuKopi) -> None:
        self.__list_menu_kopi.append(menu)

    # Getter & Setter List Barista
    def get_list_barista(self) -> List[Barista]:
        return self.__list_barista

    def set_list_barista(self, list_barista: List[Barista]) -> None:
        self.__list_barista = list_barista

    def tambah_barista(self, barista: Barista) -> None:
        self.__list_barista.append(barista)

    # Getter & Setter List Ulasan Kopi
    def get_list_ulasan_kopi(self) -> List[UlasanKopi]:
        return self.__list_ulasan_kopi

    def set_list_ulasan_kopi(self, list_ulasan_kopi: List[UlasanKopi]) -> None:
        self.__list_ulasan_kopi = list_ulasan_kopi

    def tambah_ulasan_kopi(self, ulasan: UlasanKopi) -> None:
        self.__list_ulasan_kopi.append(ulasan)

    # Rata-rata Rating Cafe
    def hitung_rata_rata_rating(self) -> float:
        if not self.__list_ulasan_kopi:
            return 0.0
        total = sum(u.get_rating() for u in self.__list_ulasan_kopi)
        return total / len(self.__list_ulasan_kopi)

    def __str__(self) -> str:
        avg_rating = self.hitung_rata_rata_rating()
        rating_str = f"{avg_rating:.1f}/5.0" if avg_rating > 0 else "Belum ada ulasan"
        return f"[Cafe] [{self.get_kode_cafe()}] {self.get_nama()} ({self.get_alamat()}) | Konsep: {self.__jenis_cafe} | Rating: {rating_str} | Menu: {len(self.__list_menu_kopi)} item | Barista: {len(self.__list_barista)} orang | Ulasan: {len(self.__list_ulasan_kopi)}"
