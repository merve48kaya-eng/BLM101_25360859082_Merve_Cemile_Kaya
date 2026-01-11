# Sanal Mantık Devresi Simülatörü
# BLM101 - Merve Cemile Kaya

def AND_gate(a, b):
    return a & b

def OR_gate(a, b):
    return a | b

def NOT_gate(a):
    return 1 - a

def XOR_gate(a, b):
    return a ^ b


def main():
    print("=== Temel Mantık Kapısı Simülasyonu ===")
    gate = input("Kapı türünü giriniz (AND, OR, NOT, XOR): ").upper()

    if gate == "NOT":
        a = int(input("A değerini giriniz (0 veya 1): "))
        print("Sonuç:", NOT_gate(a))

    elif gate in ["AND", "OR", "XOR"]:
        a = int(input("A değerini giriniz (0 veya 1): "))
        b = int(input("B değerini giriniz (0 veya 1): "))

        if gate == "AND":
            print("Sonuç:", AND_gate(a, b))
        elif gate == "OR":
            print("Sonuç:", OR_gate(a, b))
        else:
            print("Sonuç:", XOR_gate(a, b))

    else:
        print("Geçersiz kapı türü!")


main()


