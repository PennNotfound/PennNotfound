#Fungsi untuk memeriksa apakah input adalah bilangan positif
def input_positif(prompt):
    while true:
        try:
            nilai-float(input(prompt))
            if nilai > 0:
                return nilai
            else :
                print("nilai harus lebih dari 0. coba lagi")
        except ValueError:
            print("input tidak valid. masukan angka")

# meminta input panjang dan lebar dari penggua 
panjang = float(input("masukan panjang persegi panjang :"))
lebar = float(input("masukan lebar persegi panjang :"))

#menghtung luas 
luas = panjang * lebar

#menghitung keliling
keliling = 2 * (panjang + lebar)

#menampilkan hasil luas 
print(f"luas persegi panjang adalah: {luas}")

#menampilkan hasil luas dan keliling 
print(f"luas persegi panjang adlah : {luas}")
print(f"keliling persegi panjang adalah: {keliling}")

