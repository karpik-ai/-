volume_one_symbol = 4  # объем одного символа в байтах
symbols_in_a_row = 25  # кол-во символов в строке
row_numbers = 50
pages = 100
volume_disk_in_Mb = 1.44  # объем диска в Мб
Kb_in_mb = 1024  # Килобайт в Мб
B_in_kb = 1024  # Байт в Кб

volume_one_row = volume_one_symbol * symbols_in_a_row  # объем одной строки
volume_one_page = volume_one_row * row_numbers
volume_of_book = volume_one_page * pages
volume_book_in_Kb = volume_of_book / B_in_kb  # объем книги в кб
volume_book_in_Mb = volume_book_in_Kb / Kb_in_mb
number_books = volume_disk_in_Mb / volume_book_in_Mb  # кол-во книг
count = round(number_books,)  # округление

print("Количество книг, помещающихся на дискету:", count)
