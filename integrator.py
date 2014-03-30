#! /usr/bin/env python3

def euler(f, y0, a, b, h):
	t, y = a, y0
	while t < b:
		print (t, y)
		t += h
		y += h * f(t, y)

def newtoncooling(time, temp):
	return -0.07 * (temp - 20)

euler(newtoncooling, 100, 0, 100 ,10)

