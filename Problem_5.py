def smallest_number_divisible_by_all_numbers_to(n):
	
	n_start = n
	x = 1

	while n != 1:
		if x % n == 0:
			n = n - 1
		else:
			x = x + 1
			n = n_start
	return x


print(smallest_number_divisible_by_all_numbers_to(20))
