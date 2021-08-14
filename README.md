# Approximate an integral 

Approximate the function given its integral and boundaries. 

	array = np.linspace(0,9,10)
	print(array)
	# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

	A = Approx(array, 2)
	s = 0
	for a in A: 
	    print(a)
	    s += a[1]
	print("\n",s)

		# (0, 0.0)
		# (1, 0.1)
		# (2, 0.2)
		# (3, 0.3)
		# (4, 0.4)
		# (5, 0.5)
		# (6, 0.6)
		# (7, 0.7)
		# (8, 0.8)
		# (9, 0.9)
		# 
		# 1.9500000000000002

# Use case 

Approximate a work schedule given a total amount of work required and length of time. 
