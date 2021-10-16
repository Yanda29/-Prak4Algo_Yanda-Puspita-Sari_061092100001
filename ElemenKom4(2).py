print("@   @  @@@@@  @    @  @@@@    @@@@@")
print(" @ @   @   @  @ @  @  @   @   @   @")
print("  @    @@@@@  @  @ @  @    @  @@@@@")
print("  @    @   @  @   @@  @   @   @   @")
print("  @    @   @  @    @  @@@@    @   @")
import sys
ulang=9
while ulang==9:
    print("==========KONVERSI=============")
    print("1.Desimal ke Biner")
    print("2.Biner ke Desimal")
    print("3.Keluar")
    satu=int(input("silahkan Pilih Menu: "))
    if satu==1:
        koma = int(input("masukan Desimal: "))
        if koma ==0:
            print(0)
        else:
            print("hasil bagi sisa biner")
            bit=""
        while koma > 0:
            sisanya= koma % 2
            koma = koma//2
            bit= str(sisanya) + bit
            print("Binernya adalah: ",bit)
    elif satu==2:
        bit=input("Masukan String nilai Binner: ")
        koma=0
        eks = len(bit)-1
        for digit in bit:
            koma += int(digit)*2**eks
            eks -= 1
        print ("Nilai Desimal adalah :",koma)
    elif satu==3:
        sys.exit(0)