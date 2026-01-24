"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Author: Jack Kang 
Email: Yanjun.Kang@metropolia.fi
Date: 21.1.2026
Assignment: https://github.com/metropolia-sw/python/blob/main/en/Exercises.md#3-conditional-structures-if
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Task 3.1
ZANDER_LIMIT = 42
zander_length = float(input("Input zander length: "))

if zander_length >= ZANDER_LIMIT:
    print("You can bring this Zander home.")
else:
    print("You should release this Zander back into the lack.")
    print(f"{zander_length - ZANDER_LIMIT:6.2f} centimeters below the size limit")
    







