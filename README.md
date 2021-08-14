# Approximate an integral 

Approximate the function given its integral and boundaries. 

	array = np.linspace(0,9,10)
	print("array: ", array)

	A = Approx(array, 2)
	s = 0
	for a in A: 
	    print("a:", a)
	    s += a[1]
	print("s: ",s)

Will return: 

	array: [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
	a: (0, 0.0)
	a: (1, 0.1)
	a: (2, 0.2)
	a: (3, 0.3)
	a: (4, 0.4)
	a: (5, 0.5)
	a: (6, 0.6)
	a: (7, 0.7)
	a: (8, 0.8)
	a: (9, 0.9)
	
	s: 1.9500000000000002

# Use case 

Approximate a work schedule given a total amount of work required and length of time. 
