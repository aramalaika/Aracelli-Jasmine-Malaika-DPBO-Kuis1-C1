# File: EntitasBisnis.py
# Deskripsi: Superclass untuk merepresentasikan entitas bisnis/usaha
#            dalam ekosistem industri kopi (Roaster, Cafe, Supplier).

class EntitasBisnis:
    def __init__(self, kode_entitas: str = "", nama: str = "", alamat: str = ""):
        self.__kode_entitas = kode_entitas
        self.__nama = nama
        self.__alamat = alamat

    # Getter & Setter Kode Entitas
    def get_kode_entitas(self) -> str:
        return self.__kode_entitas

    def set_kode_entitas(self, kode_entitas: str) -> None:
        self.__kode_entitas = kode_entitas

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
        return f"Kode: {self.__kode_entitas} | Nama Usaha: {self.__nama} | Alamat: {self.__alamat}"
