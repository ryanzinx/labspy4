nama=[]
nim=[]
tugas=[]
uts=[]
uas=[]
akhir=[]
i=0
stop=False

while not stop:
    n=input("Nama  : ")
    nama.append(n)
    ni=input("NIM   : ")
    nim.append(ni)
    tug=input("Nilai Tugas  : ")
    tugas.append(tug)
    ut=input("Nilai UTS    : ")
    uts.append(ut)
    ua=input("Nilai UAS    : ")
    uas.append(ua)

    akh=(int(tug)*0.30)+(int(ut)*0.35)+(int(ua)*0.35)
    akhir.append(akh)
    
    tambah=input("Tambah Data (y/t)? ")
    i += 1
    if(tambah == "t" ):
        stop = True

print("===================================================================================================")
print("|    No.    |      Nama      |       NIM       |    Tugas   |    UTS    |    UAS     |    Akhir   |")
print("===================================================================================================")
for n in range(i):
    print("|    ",n+1,"    |    ",nama[n],"    |   ",nim[n],"   |    ",tugas[n],"    |   ",uts[n],"    |    ",uas[n],"    |   ",akhir[n],"   |")
print("===================================================================================================")
    

