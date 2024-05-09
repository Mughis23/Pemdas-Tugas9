listSatu = ["Apel", "Jeruk", "Mangga"]
listDua = ["Apel", "Anggur", "Nanas"]

buah = listSatu.copy()
buah.extend(listDua)
filter = set(buah)
buahDewi=sorted(filter)
print("Dewi memiliki buah", buahDewi)
