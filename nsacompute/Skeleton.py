#--IMPORTS 
import numpy as np
import os
import pandas as pd

# *** decoder ***

class Decoder():
	def read(f):
		data = pd.read_csv(str(f))
		
