# latihan konversi satuan temperatur

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

# celcius
celcius = float(input("Masukkan Suhu Dalam Celcius: "))
print("Suhu Dalam Celcius Adalah",celcius)

# reamur
reamur = (4/5) * celcius
print("Suhu Dalam Reamur Adalah",reamur)

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu Dalam Fahrenheit Adalah",fahrenheit)

# kelvin 
kelvin = celcius + 273
print("Suhu Dalam Kelvin Adalah", kelvin)

print("=====Fahrenheit Ke Kelvin")
# Fahrenheit ke Kelvin

fahrenheit = float(input("Masukkan Suhu Dalam Fahrenheit:"))
kelvin = (5/9) * (fahrenheit - 32) + 273
print("suhu dalam kelvin adalah:",kelvin,"K")

print("=====Kelvin Ke Fahrenheit")
# Kelvin ke Fahrenheit

kelvin = float(input("Masukkan Suhu Dalam Kelvin:"))
fahrenheit = (kelvin - 273) * (9/5) + 32
print("suhu dalam fahrenheit adalah:",fahrenheit)











