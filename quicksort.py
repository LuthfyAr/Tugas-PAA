def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr[1:] if x > pivot]
        
        return quick_sort(less) + equal + quick_sort(greater)

# Contoh penggunaan Quick Sort untuk memecahkan permasalahan cerita
rak_buku = ["Perancangan dan Analisis Algoritme", "Grafika Komputer", "Jaringan Komputer", "Kewarnganegaraan", "Sistem Basis Data"]

rak_buku_urut = quick_sort(rak_buku)

print("Rak buku setelah diurutkan:")
for buku in rak_buku_urut:
    print(buku)
