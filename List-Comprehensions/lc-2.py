#!/usr/bin pypy3

# applications : 

rates = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(rate) :
    return rate * (1 + TAX_RATE)

final_prices = [get_price_with_tax(i) for i in rates]
print(final_prices )

# $ pypy List-Comprehensions/lc-2.py 
# [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]