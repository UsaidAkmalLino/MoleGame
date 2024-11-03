import random #import artinya mengambil dan random adalah sebuah library
import pprint
import io
from libs import welcome_message

hello_massage='WELCOME TO THE GAMES'
spasi=' '
bentuk_goa = '''
   ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗
   ║     ║ ║     ║ ║     ║ ║     ║ ║     ║ ║     ║ ║     ║
   ║     ║ ║     ║ ║     ║ ║     ║ ║     ║ ║     ║ ║     ║
   ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝
'''
goa_kosong = [''.join(bentuk_goa)] * 20 # ini tetap harus kosong


goa=goa_kosong.copy() #ini tempat baru buat CUYPY



# Menangkap output pprint ke dalam string
output = io.StringIO()
pprint.pprint(goa, stream=output)
formatted_goa = output.getvalue()  # Mengambil hasil sebagai string

while True:
    
    # Tentukan posisi cuypy secara acak
    posisi_cuypy = random.randint(1, 20)
    
    # Reset tampilan goa dengan posisi cuypy yang baru
    goa = goa_kosong.copy()  # ini tempat baru buat CUYPY
    goa[posisi_cuypy - 1] = '''
   ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗
   ║(•◡•)║ ║     ║ ║     ║ ║     ║ ║(•◡•)║ ║     ║ ║     ║
   ║ ; ; ║ ║     ║ ║     ║ ║     ║ ║ ; ; ║ ║     ║ ║     ║ 
   ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ 
    '''
    tampilan_goa = '   '.join(goa_kosong)
    
    # Menampilkan lubang goa dalam format string untuk tampilan konsol
    output.truncate(0)
    output.seek(0)
    pprint.pprint(goa, stream=output)
    formatted_goa = output.getvalue()

    welcome_message()

    # def tambah():
    #     a = 1
    #     b = 2
    #     c = 3
    #     hasil= a-b-c
    #     return hasil

    # print(tambah())

    # def tambah(a, b):
    #     hasil= a-b
    #     return hasil

    # print(tambah(10, 300))
    # print(tambah(30,300))

    # -290
    # -270

    # if nomor_saya == 4: #ini adalah sebuah kondisi dibaca dengan jika var nomer_saya sama dengan 4, maka 
    #     print('KAMU BENAR NOMOR SAYA ADALAH',nomor_saya) #cetaklah string berikut
    # else: #namun jika tidak, maka
    #     print('KAMU SALAH !!!') #cetaklah string berikut    
    nama_user = input("[+] MASUKKAN NAMA KAMU: ")

    while nama_user == "":
        nama_user = input ("JANGAN DIKOSONGIN COKKK, isi dulu cokkk:")
        
    print(hello_massage + ' ' + nama_user + '!!!' + f'''
        
    _____________________________________________________________________________   
    |                                                                           |\ 
    | UNTUK MEMULAI GAMENYA KAMU DAPAT MEMPERHATIKAN LUBANG-LUBANG DIBAWAH,     |█|
    | KAMU HARUS MENEMUKAN 2 TIKUS TANAH YANG SEDANG                            |█|
    | BERSEMBUNYI DI BAWAH LUBANG LUBANG INI                                    |█|
    | Cobalah untuk teliti                                                      |█|
    | Dan jangan menebak-nembak !!!                                             |█|
    |                                                                           |█|
    |___________________________________________________________________________|█|
    \█████████████████████████████████████████████████████████████████████████████|
    
    
    _________________________________________________
    |                                               |\ 
    |   █▀▀ █░█ █▄█ █▀█ █▄█   █░█ █▀█ █░░ █▀▀ █▀    |█
    |   █▄▄ █▄█ ░█░ █▀▀ ░█░   █▀█ █▄█ █▄▄ ██▄ ▄█    |█
    |_______________________________________________|█
    |   find a cuypy, and see what happens          |█
    |_______________________________________________|█
    \█████████████████████████████████████████████████
    
    
    {tampilan_goa}
        
        
        ''')


    pilihan_user= int(input("menurut kamu di BARIS lubang yang mana CUYPY berada? [1,2,3,4,5,6,..]? "))  #jika kita menggunakan function input maka nilai yang di input oleh user formatnya adalah string.

    while pilihan_user < 1 or pilihan_user > 20:  # Memeriksa apakah nilai dalam rentang yang valid
        try:
            pilihan_user = int(input("Menurut kamu di BARIS lubang yang mana CUYPY berada? [1,2,3,4,5,...,20]? "))
            
            if pilihan_user > 20:  # Memeriksa apakah nilai lebih dari 20
                print("Main yang bener COKKK, masukkan nilai yang tidak lebih dari 20!")
        
        except ValueError:  # Menangani input yang tidak bisa diubah menjadi integer
            print("Masukkan angka yang valid!")

    # function konfirmasi input user
    konfirmasi_user=input(f'''
                
            |█|  ⭕ K O N F I R M A S I         
            |█|
            |█|  F O K U S
            |█|  APAKAH KAMU YAKIN,BAHWA CUYPY BERADA DI BARIS {pilihan_user} ?
            |█|  kalo salah nanti di ledekin developernya lhoo, kamu milih BARIS KE {pilihan_user},yakin? 
            |█|             
            |█|
            
            |█|===> [+] JAWABAN KAMU,[Y/n]:
                        ''').lower()
    # function kondisi /n
    if konfirmasi_user == "n":
        print(f"YAHHH {nama_user} CUPUUU,KAMU HARUS-nya YAKIN !!!")
        exit()
    # function kondisi /Y
    elif konfirmasi_user == "y":
        if pilihan_user == posisi_cuypy:
            print (f'''
                
            {formatted_goa}, 
            
            
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
                        TADI AKU NGUMPET DI : DI BARIS LUBANG {posisi_cuypy} 
                        kamu tadi milih BARIS lubang yang {pilihan_user} KANNNNN
                        AKU JADI MALU o_o 
                
                ''')
        else:
            print(f'''
                
            {formatted_goa},
            
            
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

                CUYPY ADA DI BARIS LUBANG {posisi_cuypy}
                KAMU MILIH BARIS LUBANG {pilihan_user}
                {nama_user} KAMU CUPU ULANG LAGI SANA !!!!
                
                ''')
            
    else:
        print(f'''
            
            
            
            
            |█|  ⭕ W A R N I N G
            |█| 
            |█|  INI USER NGINPUT APAAN KOCAK!!!
            |█|  {nama_user} SEPERTINYA KAMU LELAH, BERISTIRAHAT LAH!!!!
            |█|
            |█|
            
            |█|===> [+] ANOMALI INPUT DETECTED [{konfirmasi_user}] ULANG GAME DARI AWAL, DAN MASUKAN INPUT SESUAI OPSI!
            
            
            ''')

        exit()
            # selain dari kondisi ttersebut maka lanjutkan program
    respon_pengguna=input("MASUKAN UNTUK DEVELOPER ?")

    print(f'''
        
        |████████████████████████████████████████████████████████████████
        |█|
        |█|  {respon_pengguna}
        |█|
        |█|
        |█| TERIMAKSIH {nama_user} TELAH BERKONTRIBUSI :)
        |█|
        |█| tiada yang sempurna di dunia ini, kita harus terus berkembang
        |█| seperti layaknya game CUYPYGAMES ini,akan selalu dikembangkan oleh sang developer.
        |█|
        |█| message from creator @deaAfrizal_ and modifier @usaidAkmal_
        |█|
        |█|
        |███████████████████████████████████████████████████████████████
        
        ''')
    
    main_lagi = input("\n\n APAKAH KAMU INGIN BERMAIN LAGI ? [y/n]")
    if main_lagi == "n":
        break
    
print("GAMES SELESAI !!!")