#!/usr/bin/env python

''' The equivalent of toString in Java and like languages '''

class Trip:
    def __init__(self, depCity, arrCity):
        self.depCity = depCity
        self.arrCity = arrCity
        
    def __str__(self):
        return "Trip from {} to {}".format(self.depCity, self.arrCity)

trip = Trip('Toronto', 'Jamaica')
print(trip)

