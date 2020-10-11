
print('\n')
Heading = "A Program to convert number in-words 😎"
print("\t"*3, Heading, "\n", "\t"*3, len(Heading)*str('-'))

numToWords1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
               10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
               17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
               20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
               90: 'Ninety', 100: 'Hundred'}

numToWords2 = {0: 'and', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'Seventy',
               8: 'Eighty', 9: 'Ninety'}

numToWords3 = {1: 'One Hundred', 2: 'Two Hundred', 3: 'Three Hundred', 4: 'Four Hundred',
               5: 'Five Hundred', 6: 'Six Hundred', 7: 'Seven Hundred', 8: 'Eight Hundred',
               9: 'Nine Hundred', 10: 'One Thousand'}
# print('\n')
Number = int(input('Enter number to convert it into words :- '))
print("*************************************")
if Number < 100:
    if Number % 10 == 0:
        print('in-wards',numToWords1[Number])
    else:
        first1 = int(Number / 10)
        digits1 = Number % 10
        print('in-wards :~', numToWords2[first1], numToWords1[digits1])

elif Number > 100:

    if Number % 100 == 0:
        zeroNum = int(Number / 100)
        print('in-wards :~', numToWords3[zeroNum])
    else:
        first2 = int(Number / 100)
        digits2 = Number % 100
        if (Number > 110) and (Number < 120):
            print('in-wards :~', numToWords3[first2], numToWords1[digits2])

        elif digits2 % 10 == 0:
            digits3 = int(digits2 / 10)
            print('in-wards :~', numToWords3[first2], numToWords2[digits3])
        else:
            deep1 = int(digits2 / 10)
            deep2 = digits2 % 10
            print('in-wards :~', numToWords3[first2], numToWords2[deep1], numToWords1[deep2])

print("************************************")


