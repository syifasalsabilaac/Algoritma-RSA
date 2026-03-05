# Fungsi untuk menghitung FPB (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Fungsi untuk mencari inverse modular (Extended Euclidean Algorithm)
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

print("=== PEMBUATAN KUNCI RSA ===")

p = int(input("Masukkan bilangan prima p: "))
q = int(input("Masukkan bilangan prima q: "))

n = p * q
print("n = p * q =", n)

phi = (p - 1) * (q - 1)
print("phi(n) =", phi)

# memilih e
e = int(input("Masukkan nilai e (relatif prima dengan phi): "))

while gcd(e, phi) != 1:
    print("e tidak relatif prima dengan phi(n), masukkan lagi!")
    e = int(input("Masukkan nilai e: "))

# mencari d
d = mod_inverse(e, phi)

print("\nPublic Key (e,n) =", (e, n))
print("Private Key (d,n) =", (d, n))

print("\n=== ENKRIPSI ===")

m = int(input("Masukkan pesan (angka): "))

c = pow(m, e) % n

print("Ciphertext =", c)

print("\n=== DEKRIPSI ===")

dekripsi = pow(c, d) % n

print("Pesan setelah didekripsi =", dekripsi)