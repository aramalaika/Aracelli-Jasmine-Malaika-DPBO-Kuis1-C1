# File: AlatKopi.py
# Deskripsi: Kelas untuk merepresentasikan alat-alat pengolahan dan penyeduhan kopi.

class AlatKopi:
    def __init__(self, kode_alat: str = "", nama: str = "", jenis: str = "", merek: str = "", harga: float = 0.0):
        self.__kode_alat = kode_alat
        self.__nama = nama
        self.__jenis = jenis
        self.__merek = merek
        self.__harga = harga

    # Getter & Setter Kode Alat
    def get_kode_alat(self) -> str:
        return self.__kode_alat

    def set_kode_alat(self, kode_alat: str) -> None:
        self.__kode_alat = kode_alat

    # Getter & Setter Nama
    def get_nama(self) -> str:
        return self.__nama

    def set_nama(self, nama: str) -> None:
        self.__nama = nama

    # Getter & Setter Jenis
    def get_jenis(self) -> str:
        return self.__jenis

    def set_jenis(self, jenis: str) -> None:
        self.__jenis = jenis

    # Getter & Setter Merek
    def get_merek(self) -> str:
        return self.__merek

    def set_merek(self, merek: str) -> None:
        self.__merek = merek

    # Getter & Setter Harga
    def get_harga(self) -> float:
        return self.__harga

    def set_harga(self, harga: float) -> None:
        self.__harga = harga

    def __str__(self) -> str:
        return f"[{self.__kode_alat}] {self.__nama} ({self.__jenis} - {self.__merek}) - Rp {self.__harga:,.0f}"
