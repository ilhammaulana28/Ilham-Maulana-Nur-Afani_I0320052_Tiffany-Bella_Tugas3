print("Soal 1\n")

print("Bagian 1")
#Isi 10 teman
list = ['Ivan', 'Ilham', 'Totok', 'Hafiz', 'Alam', 'Aji', 'Vicka', 'Berlian', 'Ojat', 'Rian']
#Tampilan teman indeks ke 4, 6, 7
print("Teman saya yang berada di indeks 4, 6, 7 adalah", list[4], ",", list[6], ", dan", list[7], "\n")

print("Bagian 2")
#Ganti teman di list 3, 5, 9
list[3] = 'Afnan'
list[5] = 'Hani'
list[9] = 'Rafli'
print("Teman saya setelah diganti pada list 3, 5, 9 adalah", list, "\n")

print("Bagian 3")
#menambahkan 2 teman
list.insert(0, 'Ahnaf')
list.append('Yuki')
print("Setelah penambahan 2 teman, teman saya menjadi", list, "\n")

print("Bagian 4")
#Menampilkan semua teman dengan perulangan
#teman saya dalam list total adalah 'Ahnaf', 'Ivan', 'Ilham', 'Totok',
# 'Afnan', 'Alam', 'Hani', 'Vicka', 'Berlian', 'Ojat', 'Rafli', 'Yuki'
#menggunakan for
for teman in list:
    print(teman, end='')
print("\n")
#menggunakan while
temananda = []
namatemananda = input("Tuliskan nama teman anda : ")
while namatemananda != '':
    temananda.append(namatemananda)
    namatemananda = input("Tuliskan nama teman anda lagi (kosongi dan tekan enter jika cukup) : ")
print("Teman-teman anda adalah", temananda)
print("\n")

print("Bagian 5")
#menampilkan jumlah yang ada di list
print("Total teman saya adalah", len(list))

input("Tekan enter untuk keluar")
