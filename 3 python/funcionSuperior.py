# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:21:52 2022

@author: fx_66
"""


def fibo(n):
    if n<2:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
    


    
def mostrarfibo(fibo,n):
    for i in range(n):
        print(fibo(i))
        


mostrarfibo(fibo, 7)
    