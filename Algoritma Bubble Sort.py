#lets make a new program
#algoritma buble sort 

def bubble_sort(arr):  #buat kelompok fungsi bubble_sort

    n = len(arr) # mendapatkan panjang array

    for i in range(n): #memulai perulangan untuk setiap elemen

        for j in range(0, n-i-1): #perulangan untuk membandingkan elemen

            if arr[j] > arr[j+1]: #jika elemen saat ini lebih besar dari elemen berikutnya

                arr[j], arr[j+1] = arr[j+1], arr[j] #tukar posisi elemen
    return arr
# menguji buble sort

#membuat array untuk menguji fungsi bubble_sort
numbers = input("Masukkan angka yang ingin diurutkan (pisahkan dengan spasi): ")
# meminta input dari pengguna
numbers = list(map(int, numbers.split()))  #mengubah input string menjadi list angka
#memanggil fungsi bubble_sort
sorted_numbers = bubble_sort(numbers)
# menampilkan hasil pengurutan
print("Array terpendek adalah:", sorted_numbers)

#kode di buat oleh sendiri dengan bantuan github copilot (masih pemula njir)