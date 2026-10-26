# File: VarietasKopi.py
# Deskripsi: Kelas untuk merepresentasikan data varietas kopi specialty
#            beserta karakteristik asal dan profil rasanya.

class VarietasKopi:
    def __init__(self, kode_varietas: str = "", nama: str = "", asal: str = "", profil_rasa: str = "", ketinggian: int = 0):
        self.__kode_varietas = kode_varietas
        self.__nama = nama
        self.__asal = asal
        self.__profil_rasa = profil_rasa
        self.__ketinggian = ketinggian

    # Getter & Setter Kode Varietas
    def get_kode_varietas(self) -> str:
        return self.__kode_varietas

    def set_kode_varietas(self, kode_varietas: str) -> None:
        self.__kode_varietas = kode_varietas

    # Getter & Setter Nama
    def get_nama(self) -> str:
        return self.__nama

    def set_nama(self, nama: str) -> None:
        self.__nama = nama

    # Getter & Setter Asal
    def get_asal(self) -> str:
        return self.__asal

    def set_asal(self, asal: str) -> None:
        self.__asal = asal

    # Getter & Setter Profil Rasa
    def get_profil_rasa(self) -> str:
        return self.__profil_rasa

    def set_profil_rasa(self, profil_rasa: str) -> None:
        self.__profil_rasa = profil_rasa

    # Getter & Setter Ketinggian (mdpl)
    def get_ketinggian(self) -> int:
        return self.__ketinggian

    def set_ketinggian(self, ketinggian: int) -> None:
        self.__ketinggian = ketinggian

    def __str__(self) -> str:
        return f"[{self.__kode_varietas}] {self.__nama} (Asal: {self.__asal}, Profil: {self.__profil_rasa}, Alt: {self.__ketinggian} mdpl)"
