# File: Manusia.py
# Deskripsi: Superclass untuk merepresentasikan entitas manusia/individu
#            yang memiliki identitas dasar (No KTP, Nama, Alamat).

class Manusia:
    def __init__(self, no_ktp: str = "", nama: str = "", alamat: str = ""):
        self.__no_ktp = no_ktp
        self.__nama = nama
        self.__alamat = alamat

    # Getter & Setter No KTP
    def get_no_ktp(self) -> str:
        return self.__no_ktp

    def set_no_ktp(self, no_ktp: str) -> None:
        self.__no_ktp = no_ktp

    # Getter & Setter Nama
    def get_nama(self) -> str:
        return self.__nama

    def set_nama(self, nama: str) -> None:
        self.__nama = nama

    # Getter & Setter Alamat
    def get_alamat(self) -> str:
        return self.__alamat

    def set_alamat(self, alamat: str) -> None:
        self.__alamat = alamat

    def __str__(self) -> str:
        return f"No KTP: {self.__no_ktp} | Nama: {self.__nama} | Alamat: {self.__alamat}"
