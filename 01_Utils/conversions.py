"""
	Author: Luis_C-137
	Contains method to parse data
"""

def secondComplement(n) :
	mask = int('11111111111111111111111111111111', 2)
	if (n < 0) :
		n = n ^ mask
		n += 1
		n *= -1
	hex = format(n, '08X')
	return hex;