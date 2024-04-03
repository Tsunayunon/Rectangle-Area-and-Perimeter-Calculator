def alan(u, g):
    A = u * g
    return A

def cevre(u, g):
    c = 2 * (u + g)
    return c

while True:
    while True:
        u = int(input("Uzun kenar: "))
        g = int(input("Kısa kenar: "))
        if u > 0 and g > 0:
            if u > g:
                break
            else:
                print("Uzun kenar kısa kenardan büyük olmalıdır.")
        else:
            print("Kenarlar pozitif olmalıdır.")

    print("Alan: ", alan(u, g))
    print("Çevre: ", cevre(u, g))

    devam = input("Devam etmek istiyor musunuz? (E/H): ")
    if devam.upper() != 'E':
        break
