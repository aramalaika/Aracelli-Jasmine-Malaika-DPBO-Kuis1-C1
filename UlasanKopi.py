# File: UlasanKopi.py
# Deskripsi: Kelas untuk merepresentasikan data ulasan/review pelanggan
#            terhadap pelayanan dan kopi di Cafe.

class UlasanKopi:
    def __init__(self, kode_ulasan: str = "", kode_cafe: str = "", nama_pelanggan: str = "", rating: int = 5, komentar: str = "", tanggal: str = ""):
        self.__kode_ulasan = kode_ulasan
        self.__kode_cafe = kode_cafe
        self.__nama_pelanggan = nama_pelanggan
        self.__rating = rating
        self.__komentar = komentar
        self.__tanggal = tanggal

    # Getter & Setter Kode Ulasan
    def get_kode_ulasan(self) -> str:
        return self.__kode_ulasan

    def set_kode_ulasan(self, kode_ulasan: str) -> None:
        self.__kode_ulasan = kode_ulasan

    # Getter & Setter Kode Cafe
    def get_kode_cafe(self) -> str:
        return self.__kode_cafe

    def set_kode_cafe(self, kode_cafe: str) -> None:
        self.__kode_cafe = kode_cafe

    # Getter & Setter Nama Pelanggan
    def get_nama_pelanggan(self) -> str:
        return self.__nama_pelanggan

    def set_nama_pelanggan(self, nama_pelanggan: str) -> None:
        self.__nama_pelanggan = nama_pelanggan

    # Getter & Setter Rating
    def get_rating(self) -> int:
        return self.__rating

    def set_rating(self, rating: int) -> None:
        self.__rating = rating

    # Getter & Setter Komentar
    def get_komentar(self) -> str:
        return self.__komentar

    def set_komentar(self, komentar: str) -> None:
        self.__komentar = komentar

    # Getter & Setter Tanggal
    def get_tanggal(self) -> str:
        return self.__tanggal

    def set_tanggal(self, tanggal: str) -> None:
        self.__tanggal = tanggal

    def __str__(self) -> str:
        bintang = "★" * self.__rating + "☆" * (5 - self.__rating)
        return f"[{self.__kode_ulasan}] Cafe: {self.__kode_cafe} | {self.__nama_pelanggan} ({bintang} {self.__rating}/5): \"{self.__komentar}\" [{self.__tanggal}]"
