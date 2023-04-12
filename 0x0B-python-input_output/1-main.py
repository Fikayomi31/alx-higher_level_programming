#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_character = write_file("my _first_file.txt", "This is so cool!\n")
print(nb_character)
