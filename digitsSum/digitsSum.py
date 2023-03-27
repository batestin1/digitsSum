
#############################################################################################################################
#   filename:digitsSum.py                                                       
#   created: 2023-03-27                                                              
#   import your librarys below                                                    
#############################################################################################################################


def digitsSum(num, decimal=True):
    digits_sum = sum(int(digit) for digit in str(num))
    if decimal == True:
        return digits_sum
    else:
        return sum(int(digit) for digit in str(digits_sum))
    