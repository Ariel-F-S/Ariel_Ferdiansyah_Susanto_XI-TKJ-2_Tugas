# Nama      : Ariel Ferdiansyah Susanto
# Kelas     : XI-TKJ 2
# No. Absen : 04

# SOAL : Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.

def fibonacci(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Masukkan nilai n untuk bilangan Fibonacci ke-n: "))

print(f"Bilangan Fibonacci ke-{n} adalah {fibonacci(n)}")
