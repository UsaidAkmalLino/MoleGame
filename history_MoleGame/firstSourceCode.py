import random #import artinya mengambil dan random adalah sebuah library

Hello_Massage='WELCOME TO THE GAMES'
spasi=' '
posisi_cuypy=random.randint(1,30)
# nomor_saya=4

print('''
    _________________________________________________
    |                                               |\ 
    |  █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█   ▀█▀ █▀█        | \ 
    |  ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█   ░█░ █▄█        |  |
    |                                               |  |
    |  █▀▀ █░█ █▄█ █▀█ █▄█   █▀▀ ▄▀█ █▀▄▀█ █▀▀ █▀   |  |
    |  █▄▄ █▄█ ░█░ █▀▀ ░█░   █▄█ █▀█ █░▀░█ ██▄ ▄█   |  |
    |                                               |  |
    |  BY BANG DEA_AFRIZAL,modified from OxCircuitz |  |
    |_______________________________________________|  |
    \________________________________________________\ |
     \________________________________________________\|

      ''')
# if nomor_saya == 4: #ini adalah sebuah kondisi dibaca dengan jika var nomer_saya sama dengan 4, maka
#     print('KAMU BENAR NOMOR SAYA ADALAH',nomor_saya) #cetaklah string berikut
# else: #namun jika tidak, maka
#     print('KAMU SALAH !!!') #cetaklah string berikut

nama_user=input("[+] MASUKAN NAMA KAMU :")
print(Hello_Massage + ' ' + nama_user + '!!!' '''

   |                                                                           |
   | UNTUK MEMULAI GAMENYA KAMU DAPAT MEMPERHATIKAN LUBANG-LUBANG DIBAWAH,     |
   | KAMU HARUS MENEMUKAN TIKUS TANAH YANG SEDANG                              |
   | BERSEMBUNYI DI BAWAH LUBANG LUBANG INI                                    |
   | cobalah untuk teliti                                                      |
   | Dan jangan menebak-nembak !!!                                             |
   |                                                                           |

   |    █▀▀ █░█ █▄█ █▀█ █▄█   █▄▄ █▀█ ▀▄▀
   |    █▄▄ █▄█ ░█░ █▀▀ ░█░   █▄█ █▄█ █░█

_____________________________________________________
|                                                    |\ 
|  █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█   | \ 
|  █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█   | |
|                                                    | |
|  █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█   | |
|  █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█   | |
|                                                    | |
|  █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█   | |
|  █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█   | |
|                                                    | |
|  █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀█   | |
|  █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█ █▄█   | |
|____________________________________________________| |
\_____________________________________________________\|

    ''')

pilihan_user= int(input("menurut kamu di lubang yang mana CUYPY berada? [1,2,3,4,5,6,..]? "))  #jika kita menggunakan function input maka nilai yang di input oleh user formatnya adalah string.

if pilihan_user == posisi_cuypy:
    print (f'''

     ⢀⣴⠶⢶⣄⣀⣀⣤⣴⠶⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀
⠀⠀⠀⢀⣼⡟⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠈⣷⡀⠀⠀
⠀⠀⠀⣾⠁⠀⠀⣠⡾⠛⠉⠉⠉⠉⠉⠙⢿⣄⠹⣧⠀⠀
⠀⠀⠀⡇⠀⠀⠀⡏⠀⣀⣀⣀⠀⠀⠀⠀⠀⢻⡄⢸⡇⠀
⠀⠀⠀⡇⠀⠀⠀⡇⠀⠈⠉⠉⠁⠀⣀⣀⣀⡼⠁⢸⡇⠀
⠀⠀⠀⣷⡀⠀⠀⠈⠳⢦⣤⣤⣤⡾⠛⠉⠁⠀⠀⣼⠇⠀
⠀⠀⠀⠈⠻⣦⣄⣀⣀⣀⣀⣀⣀⣤⣶⣶⣶⣶⡾⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀YAHHH AKU KETAUAN :(, {nama_user} KAMU HACKER YA ?⠀⠀⠀⠀⠀⠀⠀⠀
                   TADI AKU NGUMPET DI : LUBANG {posisi_cuypy}
                   kamu tadi milih lubang yang {pilihan_user} KANNNNN
                   AKU JADI MALU o_o

           ''')
else:
    print(f'''

      ⢀⣠⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠛⠉⠁⠀⠀⠈⠙⠷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀
⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀
⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀
⢀⡟⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⢻⡄
⢸⡇⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⣷
⠘⣧⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⣶⣤⡀⠀⠀⠀⠀⣰⡟
⠀⠈⢳⣄⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣰⡿⠁
⠀⠀⠀⠙⢷⣤⣀⠀⠈⠉⠉⠉⠉⠉⠁⠀⣀⣴⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠶⢤⣤⣤⣤⣶⠶⠟⠋⠁⠀⠀⠀

               KAMU SALAH,
           KAMU BUKAN HACKER :(

           CUYPY ADA DI LUBANG {posisi_cuypy}
           KAMU MILIH NOMER {pilihan_user}
           {nama_user} KAMU CUPU ULANG LAGI SANA !!!!

          ''')