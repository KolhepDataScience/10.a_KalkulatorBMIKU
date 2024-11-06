# program body mass index
print("Perhitungan BMI (Body Mass Index)")
print("-----------------------------------")
berat_badan = input("Masukan Berat Badan Anda: ")
# hasil input masih string, supaya bisa interger maka ditambahkan fungsi interger dan float
berat_badan = (input("Masukan Berat Badan Anda (Kilogram): "))
berat_badan = int(berat_badan)
tinggi_badan = (input("Masukan Tinggi Badan Anda (Meter): "))
tinggi_badan = float(tinggi_badan)
bmi = berat_badan/(tinggi_badan**2) 
print("**************************************")

print(f"Nilai BMI Anda adalah: {bmi:.2f} Kg/m^2")
print("Nilai BMI Normal adalah: 18.5 - 25 Kg/m^2")

berat_ideal_bawah = 18.5*(tinggi_badan**2)
berat_ideal_atas = 25*(tinggi_badan**2)
print(f"Berat Badan Ideal adalah: {berat_ideal_bawah:.2f} - {berat_ideal_atas:.2f} Kg") 

print("Terima kasih sudah menggunakan program ini")