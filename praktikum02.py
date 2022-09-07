
def iteratif(n):
    hasil = [1,2,3,4,5]
    for i in range(5, n):
        jumlah = hasil[(i)-2] + hasil[i//2]
        hasil.append(jumlah)

    return hasil[n-1]

print(iteratif(8))


