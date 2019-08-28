import unittest
import urllib2

print("A is importing")


def B():
    print("A.B is running")

B()

print(urllib2.urlopen("https://google.com").readlines())
