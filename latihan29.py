lst = [10, 20, 10, 30, 40, 10, 50]
print("awal:", lst)
print("1. len:", len(lst))
print("2. count 10:", lst.count(10))
print("3. min:", min(lst))
print("4. max:", max(lst))

lst.append(60)
print("5. append:", lst) # nambah 60 di ujung
lst.insert(2, 99)
print("6. insert:", lst) # sisip 99 di index 2
lst.remove(10)
print("7. remove:", lst) # hapus 10 pertama
rem = lst.pop()
print(f"8. pop ({rem}):", lst) # buang elemen terakhir
lst.reverse()
print("9. reverse:", lst) # dibalik
sub = lst[1:4]
print("10. slicing:", sub) # ambil index 1 sampe 3