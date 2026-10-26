# File: MenuKopi.py
# Deskripsi: Kelas untuk merepresentasikan menu minuman kopi pada Cafe,
#            yang memiliki relasi memakai (asosiasi/agregasi) dengan VarietasKopi.

from VarietasKopi import VarietasKopi

class MenuKopi:
    def __init__(self, kode_menu: str = "", nama: str = "", metode_seduh: str = "", harga_per_cangkir: float = 0.0, varietas_kopi: VarietasKopi = None):
        self.__kode_menu = kode_menu
        self.__nama = nama
        self.__metode_seduh = metode_seduh
        self.__harga_per_cangkir = harga_per_cangkir
        self.__varietas_kopi = varietas_kopi

    # Getter & Setter Kode Menu
    def get_kode_menu(self) -> str:
        return self.__kode_menu

    def set_kode_menu(self, kode_menu: str) -> None:
        self.__kode_menu = kode_menu

    # Getter & Setter Nama
    def get_nama(self) -> str:
        return self.__nama

    def set_nama(self, nama: str) -> None:
        self.__nama = nama

    # Getter & Setter Metode Seduh
    def get_metode_seduh(self) -> str:
        return self.__metode_seduh

    def set_metode_seduh(self, metode_seduh: str) -> None:
        self.__metode_seduh = metode_seduh

    # Getter & Setter Harga Per Cangkir
    def get_harga_per_cangkir(self) -> float:
        return self.__harga_per_cangkir

    def set_harga_per_cangkir(self, harga_per_cangkir: float) -> None:
        self.__harga_per_cangkir = harga_per_cangkir

    # Getter & Setter Varietas Kopi (Objek)
    def get_varietas_kopi(self) -> VarietasKopi:
        return self.__varietas_kopi

    def set_varietas_kopi(self, varietas_kopi: VarietasKopi) -> None:
        self.__varietas_kopi = varietas_kopi

    def __str__(self) -> str:
        info_varietas = self.__varietas_kopi.get_nama() if self.__varietas_kopi else "Tanpa Varietas Spesifik"
        return f"[{self.__kode_menu}] {self.__nama} | Seduh: {self.__metode_seduh} | Biji: {info_varietas} | Harga: Rp {self.__harga_per_cangkir:,.0f}"
