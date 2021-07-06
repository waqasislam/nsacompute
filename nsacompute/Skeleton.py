# Python port of bitcompute, original project here: https://github.com/drivevio/bitcompute/blob/main/src/index.ts 
#--IMPORTS 
import numpy as np
# *** MATH ***
#--Adding Negative Numbers
#   To add negative numbers we first remove the dash to make it a normal number and add them then we add the dash back to make it a negative number. e.g -4 + -1 would equal -5
class Math:
   def __init__(self, set):
      self.set = set
      
   def addNegativeNumbers(mbytes64): 
      # First remove the - (Dash) out of each number to convert it into a normal number. 
      # To do this we use for loop to spit out each number without the first character which is the dash.
      # We then convert it into a int.
      cl_newnums = []
      for Byte in mbytes64:
        cl_newnums.append(int(Byte[1:]))
      # We return the sum of all the numbers in the array with the dash back with makes it negative.
      return '-' + str(sum(cl_newnums)) 

class Algorithms:
    def __init__(self, set):
      self.set = set


  
