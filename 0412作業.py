# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:56:21 2022

@author: Acer
""" 

"""
第一個作業
1
22
333
4444
55555
"""

for a in range(1,6):
    for b in range(a):
        print(a,end="")
    print()
    
"""
第二個作業
55555
4444
333
22
1
"""
for a in range(5,0,-1):
    for b in range(a):
        print(a,end="")
    print()
"""
第三個作業
999999999
7777777
55555
333
1
"""
for a in range(9,0,-2):
    for b in range(a):
        print(a,end="")
    print()
"""  
第四個作業
求質數
#1~100之間有那些
"""

for i in range(1,100):
    if i%2!=0 and i%3!=0 and i%5!=0:
       print(i,'質數')  
       
    
