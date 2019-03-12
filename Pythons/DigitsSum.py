#!/usr/bin/python
# -*- coding: utf-8 -*-
# www.algorytm.org

def suma(a):
    s=0
    while a>0:      #dopóki zostały jakieś cyfry
        s=s+(a%10)     #dodaj ostatnią cyfrę (jedności)
        a=a//10       #podziel liczbę przez 10
    return s

liczba=int(input("podaj liczbe : "))
print( "suma: "+ str(suma(liczba))) #wypisz sumę
