class Fraction(object):

	numerator = 0
	denominator = 1

	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __add__(self, other):
		if other