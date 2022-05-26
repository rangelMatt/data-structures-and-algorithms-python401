def roman_to_arabic(roman):
  total = 0

  for i in range(len(roman)-1):
    print(f'Range for loop result: {i}')
    left_char = roman[i]
    print(f'This is the left char:{left_char}')
    right_char = roman[i + 1]
    print(f'This is the right char:{right_char}')
    left_value = convert_character(left_char)
    print(f'Converted left character: {left_value}')
    right_value = convert_character(right_char)
    print(f'Converted right character: {left_value}')
    if left_value < right_value:
      left_value =- left_value
    print(f'Compared and deducted left value: {left_value}')
    print(f'This is the converted num: {total}')
    total += left_value

  if roman:

    total += convert_character(roman[-1])

  print(f'This is ALSO the converted num: {total}')
  return total

def convert_character(roman_char):
  conversion_map = {
    'M':1000,
    'D':500,
    'C':100,
    'L':50,
    'X':10,
    'V':5,
    'I':1,
    }

  # print(conversion_map.get(roman_char,0))
  return conversion_map.get(roman_char,0)

roman_to_arabic('XVX')
