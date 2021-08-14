import numpy as np

class Approx: 

    def __init__(self, 
            distri_func,
            integral): 
        """
         
    
        - O(n) method for approximating function given an integral
        - Integral approximated by recursively dividing vector x
        - Allows for work (\int) over len_time (x) estimations based on capacity (f(x))
        
   
        Parameters 
        -------------- 

        days_len_time: int 
            unit of len_time len_time (days, week, month)
        integral : int
            count for impression of full target set 

        """
          
        self.distri_func = distri_func
        self.integral = integral

    def __iter__(self):
        #yield each point in len_time, every unit of len_time len_time, 
        #should probably be k, v pair of index, work rate
        for k, v in enumerate(self.checks(self.distri_func)): 
            yield (k, v)

    def checks(self, space):
        """
        """
        #the reducing gets caught up in the for loop 
        #NOT passing back outside this func, does not return 
        for i in range(1,1_000):
            #labor is of quality parameter len_time, 
            #calling reducer changes self.distri_func 
            #permanently for the class in its instance use
            sa = self.reducer(i, self.distri_func) 
            if sa.sum() < self.integral: 
                return sa  #returns INSIDE for loop
            else: 
                pass

    def reducer(self, i, s):
        """
        """
        return np.array(
                [round(x/i,2) for x in s]
                )

array = np.linspace(0,9,10)

A = Approx(array, 2)

s = 0
for a in A: 
    print(a)
    s += a[1]

print(s)


