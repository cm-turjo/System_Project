# Function to convert numbers to Bengali words
def number_to_bengali_words(number):
    # Bengali number words
    ones = ['', 'এক', 'দুই', 'তিন', 'চার', 'পাঁচ', 'ছয়', 'সাত', 'আট', 'নয়']
    teens = ['দশ', 'এগারো', 'বারো', 'তেরো', 'চৌদ্দ', 'পনেরো', 'ষোল', 'সতেরো', 'আঠারো', 'ঊনিশ']
    tens = ['', '', 'বিশ', 'ত্রিশ', 'চল্লিশ', 'পঞ্চাশ', 'ষাট', 'সত্তর', 'আশি', 'নব্বই']
    thousands = ['হাজার', 'লাখ', 'কোটি']
    
    # Helper function to process three-digit groups
    def three_digits_to_words(n):
        word = ''
        if n >= 100:
            word += ones[n // 100] + 'শো '
            n %= 100
        if n >= 20:
            word += tens[n // 10] + ' '
            n %= 10
        if n >= 10:
            word += teens[n % 10] + ' '
        elif n > 0:
            word += ones[n] + ' '
        return word.strip()
    
    # Convert the integer part
    integer_part = int(number)
    parts = []
    for thousand in thousands:
        integer_part, rem = divmod(integer_part, 1000)
        if rem > 0:
            parts.append(three_digits_to_words(rem) + thousand + ' ')
    parts.reverse()
    word = three_digits_to_words(integer_part) + ' '.join(parts)
    
    # Convert the decimal part
    decimal_part = round(number - int(number), 2)
    if decimal_part > 0:
        decimal_words = three_digits_to_words(int(decimal_part * 100))
        word += 'টাকা দশমিক ' + decimal_words + 'পয়সা'
    else:
        word += 'টাকা'
    
    return word.strip()

# Example usage
number = 18253.13
print(number_to_bengali_words(number))
