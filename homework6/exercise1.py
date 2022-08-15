dva_slova = input()
dva_slova2 = len(dva_slova.split())
while dva_slova2 != 2:
    dva_slova = input()
    dva_slova2 = len(dva_slova.split())
if dva_slova2 == 2:
    dva_slova = dva_slova[::-1]
    dva_slova = dva_slova.split()
    dva_slova = " ".join(dva_slova[::-1])
    print(dva_slova.title())