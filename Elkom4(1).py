print("@   @  @@@@@  @    @  @@@@    @@@@@")
print(" @ @   @   @  @ @  @  @   @   @   @")
print("  @    @@@@@  @  @ @  @    @  @@@@@")
print("  @    @   @  @   @@  @   @   @   @")
print("  @    @   @  @    @  @@@@    @   @\n")

loop=17
while loop==17:
    yanda=input('masukan list angka: ')
    for yanda in yanda.split():

        if int(yanda)%2==0:
                print('terdapat elemen genap')
                break

        elif (int(yanda)%2==1 and int(yanda)%2==0) or (int(yanda)%2==1):
                print('tidak terdapat elemen genap')
                break
        