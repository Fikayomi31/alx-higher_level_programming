def roman_to_int(num):
    roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman_num = ''
    for i in sorted(roman_dict.keys(), reverse=True):
        while num:
            roman_num += roman_dict[i]
            num -= i
    return roman_num
