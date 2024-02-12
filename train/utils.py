import csv
import os

def	getPath(filename: str) -> str:
	return os.path.join(os.path.dirname(__file__), filename)

def	fetchData(filePath: str) -> tuple:
	mileages = []
	prices = []
	with open(filePath, 'r') as csvfile:
		csvReader = csv.reader(csvfile, delimiter=',')
		for row in csvReader:
			mileages.append(row[0])
			prices.append(row[1])
	mileages.pop(0)
	prices.pop(0)
	for i in range(len(mileages)):
		mileages[i] = eval(mileages[i])
		prices[i] = eval(prices[i])
	return mileages, prices