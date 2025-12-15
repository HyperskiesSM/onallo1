import unittest

def abs_max(a:int, b:int)->int:
   if(abs(a)>abs(b)):
      return abs(a)
   else: 
      return abs(b)

unittest.main()