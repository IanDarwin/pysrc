#!/usr/bin/env python

message = "The price of %(commodity)s is %(price)s"

values = {"commodity":"rice", "price":42 }

print(message % values)
