book_list = []

while True:
    print(f"""
    {10*"="} PROGRAM MENYIMPAN BUKU SEDERHANA {"="*10}
    """.strip())
    name = input("Judul Buku\t\t: ")
    writer = input("Penulis Buku\t: ")

    book = [name, writer]
    book_list.append(book)

    print()
    print(f"{10*'='} LIST BUKU {'='*10}")
    for number, book in enumerate(iterable=book_list, start=1):
        print(f"{number}. {book[0]} | {book[1]}")
    print()

    isNext = input("Apakah ingin memasukan buku lagi?(y,n) ")
    print()
    if isNext == "n":
        break
