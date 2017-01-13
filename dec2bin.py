# coding=UTF-8
from decimal import Decimal


def dec2bin(n, bit=20):
    """
    n, integer or float to convert
    bit, bits after point
    return binary, string
    """
    negative = False
    if n < 0:
        negative = True
        n *= -1

    integer = int(n)
    decimal = n - integer
    binary = ""

    if n == 0:
        return "0"

    while integer != 0:
        result = int(integer % 2)
        integer /= 2
        binary = str(result) + binary

    if decimal != 0:
        i = 0
        decimal_bin = ""  # binary decimal after convert
        while decimal != 0 and i < bit:
            result = int(decimal * 2)
            decimal = decimal * 2 - result
            decimal_bin += str(result)
            i += 1
        binary = binary + '.' + decimal_bin

    if negative:
        binary = '-' + binary

    return binary

def bin2dec(n):
    """
    n binary, support point
    return integer or float
    """
    negative = False
    if n < 0:
        negative = True
        n *= -1

    integer = int(n)
    decimal = n - integer

    if integer != 0:
        integer_str = str(integer)
        length = len(integer_str)

        integer = 0
        for i in xrange(0, length):
            bit = int(integer_str[i])
            if bit == 1:
                integer += 2 ** (length - i - 1)
            elif bit != 0:
                print "invalid integer:" + str(n)

    if decimal != 0:
        decimal_str = str(decimal)[2:] # skip "0."
        length = len(decimal_str)

        decimal = 0
        for i in xrange(0, length):
            bit = int(decimal_str[i])
            if bit == 1:
                decimal += 2 ** (-1 * (i + 1))
            elif bit != 0:
                print "invalid decimal:" + str(n)

    result = integer + decimal

    if negative:
        result *= -1

    return result


def testcases():
    for pair in [(125, '1111101'),
                 (1.3, '1.01001100110011001100'),
                 (2.5, '10.1'),
                 (0, '0'),
                 (-1, '-1'),
                 (0.5, '.1')]:
        assert pair[1] == dec2bin(pair[0])

    for pair in [(-1001.1100, -9.75),
                 (-1101, -13),
                 (111.111, 7.875),
                 (0.1101, 0.8125),
                 (1001, 9),
                 (0, 0),
                 (0.1, 0.5)]:
        assert pair[1] == bin2dec(pair[0])

    print "all test case success"


if __name__ == "__main__":
    # testcases()
    print bin2dec(0.5)
