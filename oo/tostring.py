#!/usr/bin/env python


class Trip:
    def __init__(self, depCity, arrCity):
        self.depCity = depCity
        self.arrCity = arrCity
        
    ''' The equivalent of toString in Java and like languages '''
    def __str__(self):
        return "Trip from {} to {}".format(self.depCity, self.arrCity)

trip = Trip('Toronto', 'Jamaica')

print(trip)

