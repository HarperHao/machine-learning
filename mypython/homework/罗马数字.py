"整数转罗马数字"


def intToRoman(num):
    m = [
        ['', 'M', 'MM', 'MMM'],
        ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    ]

    d = [1000, 100, 10, 1]
    r = ''
    for k, v in enumerate(d):
        r += m[k][int(num / v)]
        num = num % v
    return r


num = int(input('请输入一个整数：'))
print(intToRoman(num))



