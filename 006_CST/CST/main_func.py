#from sub_func1 import product
import sub_func1

#s = product(3, 5)
s = sub_func1.product(3,5)
print(s)

import sub_folder.sub_func2
s = sub_folder.sub_func2.sum(3,5)
print(s)