mayin_gemisi1 = [0, 0, 0, 2]
mayin_gemisi2 = [0, 0, 0, 2]

firkateyn1 = [0, 0, 0, 3]
firkateyn2 = [0, 0, 0, 3]

deniz_alti1 = [0, 0, 0, 3]
deniz_alti2 = [0, 0, 0, 3]

kruvazor1 = [0, 0, 0, 4]
kruvazor2 = [0, 0, 0, 4]

ucak_gemisi1 = [0, 0, 0, 5]
ucak_gemisi2 = [0, 0, 0, 5]

harita1 = [[0 for i in range(10)] for j in range(10)]
harita2 = [[0 for i in range(10)] for j in range(10)]


def gemi_gir(gemi):
    gemi[0] = int(input("gemi x koordinatı:"))
    gemi[1] = int(input("gemi y koordinatı:"))
    gemi[2] = int(input("gemi yönü (0:yatay, 1:dikey) :"))


def haritaya_gemi_yerlestir(harita, gemi):
    x = gemi[0]
    y = gemi[1]
    yon = gemi[2]
    uzunluk = gemi[3]
    for i in range(uzunluk):
        harita[x][y] = 1
        if yon == 0:
            y += 1
        else:
            x += 1


def harita_ciz(harita):
    for i in range(10):
        for j in range(10):
            print(harita[i][j], end=' ')
        print()


def hamle_yap(isim, harita):
    print('hamle sırası sende: ', isim)
    x = int(input('x koordinatı gir: '))
    y = int(input('y koordinatı gir: '))
    if (harita[x][y] == 1):
        harita[x][y] = 0
        return True
    else:
        return False


def galibiyet_kontrol(harita):
    for i in range(10):
        for j in range(10):
            if harita[i][j] == 1:
                return False
    return True


if __name__ == '__main__':
    isim1 = input('1. oyuncu: ')
    print(isim1 + ' gemilerini gir:')
    gemi_gir(mayin_gemisi1)
    gemi_gir(firkateyn1)
    gemi_gir(deniz_alti1)
    gemi_gir(kruvazor1)
    gemi_gir(ucak_gemisi1)
    haritaya_gemi_yerlestir(harita1, mayin_gemisi1)
    haritaya_gemi_yerlestir(harita1, firkateyn1)
    haritaya_gemi_yerlestir(harita1, deniz_alti1)
    haritaya_gemi_yerlestir(harita1, kruvazor1)
    haritaya_gemi_yerlestir(harita1, ucak_gemisi1)
    harita_ciz(harita1)
    isim2 = input('2. oyuncu: ')
    gemi_gir(mayin_gemisi2)
    gemi_gir(firkateyn2)
    gemi_gir(deniz_alti2)
    gemi_gir(kruvazor2)
    gemi_gir(ucak_gemisi2)
    haritaya_gemi_yerlestir(harita2, mayin_gemisi2)
    haritaya_gemi_yerlestir(harita2, firkateyn2)
    haritaya_gemi_yerlestir(harita2, deniz_alti2)
    haritaya_gemi_yerlestir(harita2, kruvazor2)
    haritaya_gemi_yerlestir(harita2, ucak_gemisi2)
    harita_ciz(harita2)
    oyuncu1_vurdu = True
    oyuncu2_vurdu = True
    while True:
        while oyuncu1_vurdu:
            oyuncu1_vurdu = hamle_yap(isim1, harita2)
            if oyuncu1_vurdu:
                print('gemi vurdun !')
                harita_ciz(harita2)
                sonuc = galibiyet_kontrol(harita2)
                if sonuc:
                    print('tebrikler', isim1, 'kazandın!')
                    exit(0)
            else:
                oyuncu2_vurdu = True
        while oyuncu2_vurdu:
            oyuncu2_vurdu = hamle_yap(isim2, harita1)
            if oyuncu2_vurdu:
                harita_ciz(harita1)
                sonuc = galibiyet_kontrol(harita1)
                if sonuc:
                    print('tebrikler', isim2, 'kazandın!')
                    exit(0)
            else:
                oyuncu1_vurdu = True
