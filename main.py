# Saya Aracelli Jasmine Malaika (2501804) mengerjakan Kuis 1 dalam mata kuliah 
# Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak 
# melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# import seluruh kelas 
from Manusia import Manusia
from EntitasBisnis import EntitasBisnis
from VarietasKopi import VarietasKopi
from AlatKopi import AlatKopi
from MenuKopi import MenuKopi
from UlasanKopi import UlasanKopi
from PetaniKopi import PetaniKopi
from Barista import Barista
from RoasterKopi import RoasterKopi
from SupplierAlatKopi import SupplierAlatKopi
from Cafe import Cafe

# membuat fungsi untuk mencetak garis
def cetak_garis(karakter="=", panjang=100):
    print(karakter * panjang)

# membuat fungsi untuk mencetak judul
def cetak_judul(teks):
    cetak_garis("=")
    print(f" {teks.upper()}")
    cetak_garis("=")

# membuat fungsi untuk mencetak subjudul
def cetak_subjudul(teks):
    print()
    cetak_garis("-", 90)
    print(f" >>> {teks}")
    cetak_garis("-", 90)

def main():
    # inisialisasi data varietas kopi
    varietas_list = [
        VarietasKopi("VAR-01", "Arabika Gayo Wine", "Takengon, Aceh Tengah", "Fruity, Winey, Sweet Acidity", 1450),
        VarietasKopi("VAR-02", "Arabika Java Preanger", "Pangalengan, Jawa Barat", "Floral Jasmine, Citrus, Sweet Honey", 1550),
        VarietasKopi("VAR-03", "Arabika Toraja Sapan", "Toraja Utara, Sulsel", "Herbal, Dark Chocolate, Spicy", 1600)
    ]

    # inisialisasi data alat kopi
    alat_list = [
        AlatKopi("ALT-01", "EK43 Commercial Grinder", "Grinder", "Mahlkönig", 48500000.0),
        AlatKopi("ALT-02", "Linea Mini 1-Group", "Espresso Machine", "La Marzocco", 89000000.0),
        AlatKopi("ALT-03", "V60 Ceramic Dripper 02", "Dripper", "Hario", 320000.0),
        AlatKopi("ALT-04", "Stagg EKG Electric Pour-Over Kettle", "Kettle", "Fellow", 2850000.0)
    ]

    # inisialisasi data petani kopi
    petani_1 = PetaniKopi("3204112233440001", "Pak Asep", "Kec. Pangalengan, Kab. Bandung", 2012)
    petani_1.tambah_varietas_kopi(varietas_list[1]) # menanam Java Preanger

    petani_2 = PetaniKopi("1104556677880002", "Pak Adi", "Kec. Bebesen, Kab. Aceh Tengah", 2008)
    petani_2.tambah_varietas_kopi(varietas_list[0]) # menanam Gayo Wine
    petani_2.tambah_varietas_kopi(varietas_list[2]) # menanam Toraja (kemitraan)

    petani_list = [petani_1, petani_2] # list petani kopi

    # inisialisasi data roaster kopi
    roaster_1 = RoasterKopi("RST-01", "Preanger Artisan Roastery", "Jl. Kolonel Masturi No. 15, Bandung", "Light to Medium")
    roaster_1.tambah_varietas_kopi(varietas_list[1]) # roasting Java Preanger
    roaster_1.tambah_varietas_kopi(varietas_list[2]) # roasting Toraja

    roaster_2 = RoasterKopi("RST-02", "Gayo Mountain Specialty Roasters", "Jl. Sengeda No. 8, Takengon", "Medium")
    roaster_2.tambah_varietas_kopi(varietas_list[0]) # roasting Gayo Wine

    roaster_list = [roaster_1, roaster_2] # list roaster kopi

    # inisialisasi data menu kopi
    menu_list = [
        MenuKopi("MNU-01", "V60 Preanger Floral Reserve", "pour over", 32000.0, varietas_list[1]),
        MenuKopi("MNU-02", "Gayo Wine Espresso Shot", "espresso", 28000.0, varietas_list[0]),
        MenuKopi("MNU-03", "Toraja Spiced Cold Brew", "cold brew", 35000.0, varietas_list[2]),
        MenuKopi("MNU-04", "Preanger Honey French Press", "french press", 30000.0, varietas_list[1])
    ]

    # inisialisasi data barista
    barista_1 = Barista("3273112233440003", "Fajar", "Coblong, Kota Bandung", "expert")
    barista_1.tambah_menu_kopi(menu_list[0])
    barista_1.tambah_menu_kopi(menu_list[1])

    barista_2 = Barista("3273556677880004", "Dinda", "Sukajadi, Kota Bandung", "intermediate")
    barista_2.tambah_menu_kopi(menu_list[0])    
    barista_2.tambah_menu_kopi(menu_list[2])
    barista_2.tambah_menu_kopi(menu_list[3])

    barista_list = [barista_1, barista_2] # list barista

    # inisialisasi data supplier alat kopi
    supplier_1 = SupplierAlatKopi("SPL-01", "PT Seduh Alat Nusantara", "Kawasan Niaga Meruya, Jakarta Barat")
    supplier_1.tambah_alat_kopi(alat_list[0]) # EK43 Grinder
    supplier_1.tambah_alat_kopi(alat_list[1]) # Linea Mini

    supplier_2 = SupplierAlatKopi("SPL-02", "CV Barista Supply Priangan", "Jl. Buah Batu No. 88, Bandung")
    supplier_2.tambah_alat_kopi(alat_list[2]) # Hario V60
    supplier_2.tambah_alat_kopi(alat_list[3]) # Stagg Kettle

    supplier_list = [supplier_1, supplier_2] # list supplier alat kopi

    # inisialisasi data ulasan kopi
    ulasan_cafe_1 = [
        UlasanKopi("REV-001", "CFE-01", "Budi", 5, "V60 Preanger sangat wangi bunga dan aftertaste manis madu!", "2026-09-12"),
        UlasanKopi("REV-002", "CFE-01", "Clara", 5, "Barista sangat ramah dan edukatif menjelaskan cupping notes.", "2026-09-14")
    ]

    ulasan_cafe_2 = [
        UlasanKopi("REV-003", "CFE-02", "Rian", 4, "Cold brew Toraja mantap, aroma cokelat tebal menyegarkan.", "2026-09-15"),
        UlasanKopi("REV-004", "CFE-02", "Siti", 5, "Suasana kafe nyaman untuk WFC, biji kopi specialty terkurasi baik.", "2026-09-16")
    ]

    # inisialisasi data cafe
    cafe_1 = Cafe("CFE-01", "Kopi Selasar Specialty", "Jl. Bukit Pakar Timur No. 42, Dago, Bandung", "specialty")
    cafe_1.tambah_menu_kopi(menu_list[0])
    cafe_1.tambah_menu_kopi(menu_list[1])
    cafe_1.tambah_barista(barista_1)
    for u in ulasan_cafe_1:
        cafe_1.tambah_ulasan_kopi(u)

    cafe_2 = Cafe("CFE-02", "Ruang Seduh Priangan", "Jl. LLRE Martadinata No. 108, Riau, Bandung", "specialty")
    cafe_2.tambah_menu_kopi(menu_list[0])
    cafe_2.tambah_menu_kopi(menu_list[2])
    cafe_2.tambah_menu_kopi(menu_list[3])
    cafe_2.tambah_barista(barista_2)
    for u in ulasan_cafe_2:
        cafe_2.tambah_ulasan_kopi(u)

    cafe_list = [cafe_1, cafe_2] # list cafe

    # tampilan daftar varietas kopi
    cetak_subjudul("DAFTAR VARIETAS KOPI SPECIALTY")
    print(f"{'Kode':<10} | {'Nama Varietas':<25} | {'Daerah Asal':<26} | {'Ketinggian':<11} | {'Profil Rasa'}")
    print("-" * 115)
    for v in varietas_list:
        print(f"{v.get_kode_varietas():<10} | {v.get_nama():<25} | {v.get_asal():<26} | {v.get_ketinggian()} mdpl     | {v.get_profil_rasa()}")

    # tampilan petani kopi
    cetak_subjudul("DAFTAR PETANI KOPI")
    for p in petani_list:
        print(f"• No KTP          : {p.get_no_ktp()}")
        print(f"  Nama Petani     : {p.get_nama()}")
        print(f"  Domisili/Lahan  : {p.get_alamat()}")
        print(f"  Tahun Bertani   : {p.get_tahun_awal_bertani()} (Pengalaman: {2026 - p.get_tahun_awal_bertani()} tahun)")
        print(f"  Varietas Ditanam: {len(p.get_list_varietas_kopi())} jenis")
        for idx, var in enumerate(p.get_list_varietas_kopi(), 1):
            print(f"    {idx}. [{var.get_kode_varietas()}] {var.get_nama()} - Asal: {var.get_asal()}")
        print()

    # tampilan roaster kopi
    cetak_subjudul("DAFTAR ROASTER KOPI")
    for r in roaster_list:
        print(f"• Kode Roaster    : {r.get_kode_roaster()}")
        print(f"  Nama Roastery   : {r.get_nama()}")
        print(f"  Lokasi Fasilitas: {r.get_alamat()}")
        print(f"  Profil Sangrai  : {r.get_metode_roasting()}")
        print(f"  Varietas Biji   : {len(r.get_list_varietas_kopi())} jenis di-roasting")
        for idx, var in enumerate(r.get_list_varietas_kopi(), 1):
            print(f"    {idx}. [{var.get_kode_varietas()}] {var.get_nama()} ({var.get_profil_rasa()})")
        print()

    # tampilan supplier alat kopi
    cetak_subjudul("DAFTAR SUPPLIER ALAT KOPI")
    for s in supplier_list:
        print(f"• Kode Supplier   : {s.get_kode_supplier()}")
        print(f"  Nama Perusahaan : {s.get_nama()}")
        print(f"  Alamat Kantor   : {s.get_alamat()}")
        print(f"  Katalog Produk  : {len(s.get_list_alat_kopi())} item alat kopi")
        for idx, a in enumerate(s.get_list_alat_kopi(), 1):
            print(f"    {idx}. [{a.get_kode_alat()}] {a.get_nama():<35} | Jenis: {a.get_jenis():<16} | Merek: {a.get_merek():<12} | Rp {a.get_harga():>12,.0f}")
        print()

    # tampilan barista
    cetak_subjudul("DAFTAR BARISTA KOPI")
    for b in barista_list:
        print(f"• No KTP          : {b.get_no_ktp()}")
        print(f"  Nama Barista    : {b.get_nama()}")
        print(f"  Alamat          : {b.get_alamat()}")
        print(f"  Sertifikasi     : {b.get_level_sertifikasi().upper()}")
        print(f"  Keahlian Menu   : {len(b.get_list_menu_kopi())} resep seduhan")
        for idx, m in enumerate(b.get_list_menu_kopi(), 1):
            var_info = m.get_varietas_kopi().get_nama() if m.get_varietas_kopi() else "-"
            print(f"    {idx}. [{m.get_kode_menu()}] {m.get_nama():<30} | Metode: {m.get_metode_seduh():<12} | Biji: {var_info}")
        print()

    # tampilan menu kopi
    cetak_subjudul("DAFTAR MENU KOPI")
    print(f"{'Kode':<8} | {'Nama Menu':<30} | {'Metode Seduh':<14} | {'Harga':<14} | {'Biji Varietas (Single Origin)'}")
    print("-" * 115)
    for m in menu_list:
        biji = f"{m.get_varietas_kopi().get_nama()} ({m.get_varietas_kopi().get_asal()})" if m.get_varietas_kopi() else "-"
        print(f"{m.get_kode_menu():<8} | {m.get_nama():<30} | {m.get_metode_seduh():<14} | Rp {m.get_harga_per_cangkir():>10,.0f} | {biji}")

    # tampilan cafe
    cetak_subjudul("DAFTAR CAFE")
    for c in cafe_list:
        print(f"==========================================================================================")
        print(f" KEDAI KOPI: [{c.get_kode_cafe()}] {c.get_nama()} (Konsep: {c.get_jenis_cafe().upper()})")
        print(f" Alamat    : {c.get_alamat()}")
        print(f" Rata-rata : {c.hitung_rata_rata_rating():.1f} / 5.0 bintang dari {len(c.get_list_ulasan_kopi())} ulasan")
        print(f"------------------------------------------------------------------------------------------")
        
        print(" [A] Tim Barista yang Bertugas:")
        for idx, b in enumerate(c.get_list_barista(), 1):
            print(f"     {idx}. {b.get_nama()} (Sertifikasi: {b.get_level_sertifikasi()})")

        print(" [B] Daftar Menu Tersedia:")
        for idx, m in enumerate(c.get_list_menu_kopi(), 1):
            biji = m.get_varietas_kopi().get_nama() if m.get_varietas_kopi() else "Blend"
            print(f"     {idx}. {m.get_nama():<30} | {m.get_metode_seduh():<12} | Rp {m.get_harga_per_cangkir():>9,.0f} | Biji: {biji}")

        print(" [C] Ulasan & Kepuasan Pelanggan (Komposisi):")
        for idx, u in enumerate(c.get_list_ulasan_kopi(), 1):
            bintang = "★" * u.get_rating() + "☆" * (5 - u.get_rating())
            print(f"     {idx}. [{u.get_tanggal()}] {u.get_nama_pelanggan()} ({bintang} {u.get_rating()}/5)")
            print(f"        \"{u.get_komentar()}\"")
        print()

    # contoh penggunaan pewarisan dan polimorfisme
    cetak_subjudul("PEWARISAN DAN POLIMORFISME")
    print("Data Petani dan Barista:")
    daftar_manusia = [petani_1, petani_2, barista_1, barista_2]
    for orang in daftar_manusia:
        tipe = "Petani" if isinstance(orang, PetaniKopi) else "Barista"
        print(f"   [{tipe:<7}] KTP: {orang.get_no_ktp()} | Nama: {orang.get_nama():<20} | Alamat: {orang.get_alamat()}")

    print("\nData Roaster, Supplier, dan Cafe:")
    daftar_bisnis = [roaster_1, roaster_2, supplier_1, supplier_2, cafe_1, cafe_2]
    for usaha in daftar_bisnis:
        tipe = usaha.__class__.__name__
        print(f"   [{tipe:<18}] Kode: {usaha.get_kode_entitas():<8} | Nama: {usaha.get_nama():<35} | Alamat: {usaha.get_alamat()}")

    cetak_garis("=")
    print(" PROGRAM SELESAI")
    cetak_garis("=")

# memanggil fungsi utama
if __name__ == "__main__":
    main()
