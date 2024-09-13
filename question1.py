"""
ECE241 Fall 2024 - Homework1 Question1
"""

# Use the following constants if you need
below_20 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thousands = ['', 'thousand', 'million']


def stringify(number):
    """

    :param number:
    :return:
    """

    num = ""

    if number > 999999999:
        return "The number is too big."
    else:
        if number == 0:
            return "zero"
        if number < 20:
            return below_20[number]
        elif 20 <= number < 100:
            if number%10 == 0:
                num = tens[int(number/10)]
            else:
                num = tens[int(number / 10)] + " " + below_20[number % 10]
            return num
        elif 100 <= number < 1000:
            if number%100 == 0:
                num = below_20[int(number/100)] + " hundred"
            else:
                num = below_20[int(number / 100)] + " hundred and "
                temp = number%100
                if temp % 10 == 0:
                    num += tens[int(temp / 10)]
                else:
                    num += tens[int(temp / 10)] + " " + below_20[temp % 10]
            return num
        elif 1000 <= number < 1000000:
            thou = int(number/1000)
            if len(str(thou)) == 3 and thou != 0:
                if thou % 100 == 0:
                    num = below_20[int(thou / 100)] + " hundred " + thousands[1] + ", "
                else:
                    num = below_20[int(thou / 100)] + " hundred and "
                    temp = thou % 100
                    if temp < 20:
                        num += below_20[temp] + " " + thousands[1] + ", "
                    elif temp % 10 == 0:
                        num += tens[int(temp / 10)] + " " + thousands[1] + ", "
                    else:
                        num += tens[int(temp / 10)] + " " + below_20[temp % 10] + " " + thousands[1] + ", "
            elif len(str(thou)) <= 2 and thou != 0:
                if thou < 20:
                    num = below_20[thou] + " " + thousands[1] + ", "
                elif thou % 10 == 0:
                    num = tens[int(thou / 10)] + " " + thousands[1] + ", "
                else:
                    num = tens[int(thou / 10)] + " " + below_20[thou % 10] + " " + thousands[1] + ", "
            hun = number%1000
            if len(str(hun)) == 3:
                if hun % 100 == 0:
                    num += below_20[int(hun / 100)] + " hundred"
                else:
                    num += below_20[int(hun / 100)] + " hundred and "
                    temp = hun % 100
                    if temp < 20:
                        num += below_20[temp]
                    elif temp % 10 == 0:
                        num += tens[int(temp / 10)]
                    else:
                        num += tens[int(temp / 10)] + " " + below_20[temp % 10]
            elif len(str(hun)) <= 2:
                if hun < 20:
                    num += below_20[hun]
                elif hun % 10 == 0:
                    num += tens[int(hun / 10)]
                else:
                    num += tens[int(hun / 10)] + " " + below_20[hun % 10]
            return num
        elif 1000000 <= number < 1000000000:
            mill = int(number / 1000000)
            if len(str(mill)) == 3:
                if mill % 100 == 0:
                    num = below_20[int(mill / 100)] + " hundred"
                else:
                    num = below_20[int(mill / 100)] + " hundred and "
                    temp = mill % 100
                    if temp < 20:
                        num += below_20[temp]
                    elif temp % 10 == 0:
                        num += tens[int(temp / 10)]
                    else:
                        num += tens[int(temp / 10)] + " " + below_20[temp % 10]
            elif len(str(mill)) <= 2:
                if mill < 20:
                    num = below_20[mill]
                elif mill % 10 == 0:
                    num = tens[int(mill / 10)]
                else:
                    num = tens[int(mill / 10)] + " " + below_20[mill % 10]
            num += " " + thousands[2] + ", "
            thoutemp = number % 1000000
            thou = int(thoutemp / 1000)
            if len(str(thou)) == 3 and thou != 0:
                if thou % 100 == 0:
                    num += below_20[int(thou / 100)] + " hundred " + thousands[1] + ", "
                else:
                    num += below_20[int(thou / 100)] + " hundred and "
                    temp = thou % 100
                    if temp < 20:
                        num += below_20[temp] + " " + thousands[1] + ", "
                    elif temp % 10 == 0:
                        num += tens[int(temp / 10)] + " " + thousands[1] + ", "
                    else:
                        num += tens[int(temp / 10)] + " " + below_20[temp % 10] + " " + thousands[1] + ", "
            elif len(str(thou)) <= 2 and thou != 0:
                if thou < 20:
                    num += below_20[thou] + " " + thousands[1] + ", "
                elif thou % 10 == 0:
                    num += tens[int(thou / 10)] + " " + thousands[1] + ", "
                else:
                    num += tens[int(thou / 10)] + " " + below_20[thou % 10] + " " + thousands[1] + ", "
            hun = thoutemp % 1000
            if len(str(hun)) == 3:
                if hun % 100 == 0:
                    num += below_20[int(hun / 100)] + " hundred"
                else:
                    num += below_20[int(hun / 100)] + " hundred and "
                    temp = hun % 100
                    if temp < 20:
                        num += below_20[temp]
                    elif temp % 10 == 0:
                        num += tens[int(temp / 10)]
                    else:
                        num += tens[int(temp / 10)] + " " + below_20[temp % 10]
            elif len(str(hun)) <= 2:
                if hun < 20:
                    num += below_20[hun]
                elif hun % 10 == 0:
                    num += tens[int(hun / 10)]
                else:
                    num += tens[int(hun / 10)] + " " + below_20[hun % 10]
            return num
    pass

if __name__ == "__main__":
    print(stringify(1))         # Excepted: one
    print(stringify(10))        # Excepted: ten
    print(stringify(2024))      # Excepted: two thousand, twenty four
    print(stringify(20242024))  # Excepted: twenty million, two hundred and forty two thousand, twenty four
