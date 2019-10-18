nama = 'friesca ayazya'
program = 'usaha'

print(f'{program} oleh (nama)')

def hitung_usaha(gaya, jarak) :
    usaha = gaya * jarak
    print(f'gaya = {gaya/20}newton diperoleh dari jarak = {jarak/40}meter')
    print(f'sehingga usaha = {usaha} joule')

#gaya = 20
#jarak = 40
usaha = hitung_usaha(20, 40)

def hitung_tekanan(gaya, luaspenampang) :
    tekanan = gaya / luaspenampang
    print(f'gaya = {gaya/10}newton diperoleh dari luaspenampang = {luaspenampang/5}meter^2')
    print(f'sehingga tekanan = {tekanan} N/m^2')

#gaya = 10
#luaspenampang = 5
tekanan = hitung_tekanan(10,5)



nama = 'friesca ayazya'
program = 'hitng_tekanan'

print(f'{program}oleh (nama)')

def hitung_arus(tegangan, hambatan):
    arus = tegangan / hambatan
    print(f'tegangan = {tegangan/30}volt diperoleh dari hambatan = {hambatan/15}ohm')
    print(f'sehingga arus = {arus} ampere')


# tegangan = 30
# hambatan = 15
arus = hitung_arus(30, 15)
arus = hitung_arus(60, 30)
