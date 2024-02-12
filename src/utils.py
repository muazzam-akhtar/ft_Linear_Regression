from math_utils import normalizeElem
from math_utils import denormalizeElem

import csv
import os
import matplotlib.pyplot as plt

def	getPath(filename: str) -> str:
	return os.path.join(os.path.dirname(__file__), filename)

def	fetchData(filePath: str) -> tuple:
	mileages = []
	prices = []
	with open(filePath, 'r') as csvfile:
		csvReader = csv.reader(csvfile, delimiter=',')
		for row in csvReader:
			if len(row) != 2:
				print("Error")
				exit(1)
			mileages.append(row[0])
			prices.append(row[1])
	mileages.pop(0)
	prices.pop(0)
	for i in range(len(mileages)):
		mileages[i] = eval(mileages[i])
		prices[i] = eval(prices[i])
	return mileages, prices

def	getThetas(filePath: str) -> tuple:
	t0, t1 = 0, 0
	if (os.path.isfile(filePath)):
		with open(filePath, 'r') as csvfile:
			csvReader = csv.reader(csvfile, delimiter=',')
			for row in csvReader:
				if len(row) == 2:
					t0 = float(row[0])
					t1 = float(row[1])
					break
				print("Error")
				exit(1)
	return (t0, t1)

def	estimatePrice(thetas, mileage, mileages, prices):
	price = thetas[1] * normalizeElem(mileages, mileage) + thetas[0]
	return (denormalizeElem(prices, price))

def	estimatePrice(thetas: tuple, mileage: float, mileages: list, prices: list) -> float:
	return(denormalizeElem((thetas[1] * normalizeElem(mileage, max(mileages),
								min(mileages))) + thetas[0], max(prices), min(prices)))

def	earlyStopping(lossHistory: list) -> bool:
	check = 8
	if len(lossHistory) > check:
		mean = sum(lossHistory[-check:]) / check
		last = lossHistory[-1]
		if round(mean, 9) == round(last, 9):
			return True
	return False

def	boldDriver(loss: float, lossHistory: list, t0: float, t1: float,
			dt0: float, dt1: float, learningRate: float, length: int) -> tuple:
	if len(lossHistory) > 1:
		if loss >= lossHistory[-1]:
			t0 += (dt0 / length * learningRate)
			t1 += (dt1 / length * learningRate)
			learningRate *= 0.5
		else:
			learningRate *= 1.05
	return (t0, t1, learningRate)

def	storeData(t0: float, t1: float, filename: str):
	with open(filename, 'w') as csvfile:
		csvWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvWriter.writerow([t0, t1])
		
def	plotting(t0: float, t1: float, mileages: list, prices: list):
	lineX = [float(min(mileages)), float(max(mileages))]
	lineY = []
	for elem in lineX:
		elem = (t1 * normalizeElem(elem, max(mileages), min(mileages))) + t0
		lineY.append(denormalizeElem(elem, max(prices), min(prices)))
	plt.figure("Linear Regression")
	plt.plot(mileages, prices, 'bo', lineX, lineY, 'r-')
	plt.xlabel('mileage')
	plt.ylabel('price')
	plt.show()