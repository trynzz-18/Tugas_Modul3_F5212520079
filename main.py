print("     KALKULATOR KONVERSI SUHU")

print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

pilihan = input("Pilih konversi (1/2): ")

if pilihan == "1":
    celsius = float(input("Masukkan suhu Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Hasil: {celsius}°C = {fahrenheit}°F")

elif pilihan == "2":
    fahrenheit = float(input("Masukkan suhu Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Hasil: {fahrenheit}°F = {celsius:.2f}°C")

else:
    print("Pilihan tidak valid.")
