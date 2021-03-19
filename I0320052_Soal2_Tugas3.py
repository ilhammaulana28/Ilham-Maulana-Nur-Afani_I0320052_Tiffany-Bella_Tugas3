print("Soal 2\n")
print("Bagian 1")
#dictionary pertama
datadiri = {'Nama': 'Ilham Maulana Nur Afani',
            'Hobi1': 'Bulutangkis',
            'Hobi2': 'Main gitar',
            'Hobi3': 'Main game',
            'Sosmed1': 'IG: @ilhummm_',
            'Sosmed2': 'WA: 082132578375',
            'Sosmed3': 'Line: ilhummm',
            'Lagu_fav1': 'Instrumedley-Dream Theater',
            'Lagu_fav2': 'All Alone-Blind Witness',
            'Lagu_fav3': 'Nothing left-As I Lay Dying',
            'Mkn_fav1': 'Trancam',
            'Mkn_fav2': 'Bakso',
            'Mkn_fav3': 'Bubur ayam'}
print(datadiri)
print(type(datadiri), '\n')

print("Bagian 2")
#ubah salah satu hobi dan sosmed
#hobi baru
datadiri['Hobi3'] = 'Bersepeda'
#sosmed baru
datadiri['Sosmed3'] = 'Twitter: @ilhummm'
print("Datadiri dengan penggantian hobi dan sosmed: ", datadiri, "\n")
#hapus 2 makanan fav
del datadiri['Mkn_fav3']
del datadiri['Mkn_fav2']
print("Datadiri dengan penghapusan 2 makanan favorit: ", datadiri, "\n")
#penambahan 1 hobi
datadiri['Hobi4'] = 'Gym'
print("Datadiri dengan penambahan 1 hobi baru: ", datadiri, "\n")
input("Tekan enter untuk keluar")
