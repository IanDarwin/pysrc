#!/usr/bin/env python

''' The equivalent of toString in Java and like languages '''

class Trip:
    def __init__(self, x):
        self.x = x
        
    def __str__(self):
        return "Trip:" + self.x

trip = Trip('123')
print(trip)

