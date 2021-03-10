from math import *

# Calculate the mean of a list of numbers
def mean(nums):
    return sum(nums) / float(len(nums))

# Calculate the standard deviation of a list of numbers
def stdev(nums):
    avg = mean(nums)
    variance = sum([(x-avg)**2 for x in nums]) / float(len(nums)-1)
    return sqrt(variance)

# Calculate the Gaussian probability distribution function for x
def calc_prob(x, mean, stdev):
    exponent = exp(-(x-mean)**2 / (2 * stdev ** 2))
    return (1 / (sqrt(2 * pi) * stdev)) * exponent


# Calculate the probabilities of predicting each class for a given row
def calculate_class_probabilities(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])
	probabilities = dict()
	for class_value, class_summaries in summaries.items():
		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(class_summaries)):
			mean, stdev, _ = class_summaries[i]
			probabilities[class_value] *= calc_prob(row[i], mean, stdev)
	return probabilities