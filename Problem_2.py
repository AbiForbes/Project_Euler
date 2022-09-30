
x_Minus_1 = 0
x = 1
x_storage = 0
sum_of_even_terms= 0

while x <= 4000000:
    if x%2 == 0:
        sum_of_even_terms = sum_of_even_terms +  x
    x_storage = x
    x =  x +  x_Minus_1
    x_Minus_1 = x_storage

print (sum_of_even_terms)
