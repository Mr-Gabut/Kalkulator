import sys,os,time

time.sleep(2)
os.system ('git pull')
os.system('clear')
# Warna 
h="\33[0;32m"
m="\33[31;1m"
p="\33[37;1m"
k="\33[1;33m"
print (f'{p}Gabung ke Group {h}WhatsApp {p}admin yuk!.')
time.sleep (2)
os.system('xdg-open https://chat.whatsapp.com/DuYq8oFeTEv7qgmAhtTcsL')
time.sleep (5)
os.system ('clear')
def nyerat(c):
  c = c + '\n'
  for x in c:
    time.sleep(0.01)
    print(x, end='', flush=True)
    
def nulis(c):
  c = c + '\n'
  for x in c:
    time.sleep(0.05)
    print(x, end='', flush=True)
 
nyerat(f'{m}██╗░░██╗{p}░█████╗░██╗░░░░░')
nyerat(f'{m}██║░██╔╝{p}██╔══██╗██║░░░░░')
nyerat(f'{m}█████═╝░{p}███████║██║░░░░░')
nyerat(f'{m}██╔═██╗░{p}██╔══██║██║░░░░░')
nyerat(f'{m}██║░╚██╗{p}██║░░██║███████╗{k}KULATOR {p}V.{m}1.0')
nyerat(f'{m}╚═╝░░╚═╝{p}╚═╝░░╚═╝╚══════╝')

garis = f'{p}========================'
print (garis)
print (f'• {k}Creator{p} : {k}Mr-Gabut')
print (f'{p}• {k}Youtube{p} : {k}FireMe')
print (garis)
nama = input(f"{m}? {p}Nama :{h} ")
# Kita Mulai ke codingannya ya
nulis(f"\n{p}Selamat datang {m}{nama} {p}semoga harimu menyenangkan jangan lupa solat!. \n\n{m}CTRL + c Untuk keluar.\n\n{p}Thanks to Allah and Propet Muhammad Sallallahu alaihi wasallam.\nBiar aku makin semangat bantu subs my chanel yutub sampahku ini ya.\nTerimakasih\n\nFireMe17 Team\n\nBuat yang pengin mondok kalian bisa hubungi nomor {h}WhatsApp {p}kami.\n")
time.sleep (2)
os.system ('xdg-open https://wa.me/6282116348574')
time.sleep (3)
pilih = f'''{p}1{m}.{p} Dikali
{p}2{m}. {p}Ditambah
{p}3{m}. {p}Dikurang
{p}4{m}. {p}Dibagi'''
while True:
  total = 0
  angka1 = int(input(f"{m}? {p}Angka : {h}"))
  print (garis)
  print (pilih)
  print (garis)
  salma = int(input(f'{m}? {k}Pilih {p}: {h}'))
  angka2 = int(input(f'{m}? {p}Angka : {h}'))
  if salma == 1:
    total = angka1 * angka2 # Perkalian
  elif salma == 2:
    total = angka1 + angka2 # Penjumlahan
  elif salma == 3:
    total = angka1 - angka2 # Pengurangan
  elif salma == 4:
    total = angka1 / angka2 # Ngabagi
  else:
    print (f'{m}Salah milihnya!.\n{p}')
    time.sleep (3)
  os.system('clear')
  print (f"\n{m}Hasil : {p}{total}\n")
  lanjut = input(f"{m}[{p}Enter{m}] ")
  print (' ')
