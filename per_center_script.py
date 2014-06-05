from __future__ import division

def  per_center(test, baseline):
	# Calculate the % difference between test value and the baseline
	# value
	if test > baseline:
		val = ((test - baseline) / baseline) * 100
		print "Test is %f greater than baseline" %val
	elif test < baseline:
		val = ((baseline - test) / baseline) * 100
		print "Test is %f less than baseline" %val