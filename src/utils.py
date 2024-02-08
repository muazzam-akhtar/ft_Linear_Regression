import os
import csv
import matplotlib.pyplot as plt

def	getPath(filePath: str) -> str:
	return os.path.join(os.path.dirname(__file__), filePath)

def	getData(file: str) -> tuple:
	mileages = []
	prices = []
	with open(file, 'r') as csvfile:
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

def	normalizeElem(elem: float, data: list) -> float:
	return ((elem - min(data)) / (max(data) - min(data)))

def	denormalizeElem(elem: float, data: list) -> float:
	return ((elem * (max(data) - min(data))) + min(data))

def	normalizeData(data: list) -> list:
	minM = min(data)
	maxM = max(data)
	_result = []
	for i in data:
		_result.append((i - minM) / (maxM - minM))
	return _result

def	lossFunction(t0: float, t1: float, mileages: list, prices: list) -> float:
	loss = 0.0
	for mileage, price in zip(mileages, prices):
		loss += (price - (t1 * mileage + t0)) ** 2
	return loss / len(mileages)

def	boldDriver(loss: float, lossHistory: list, t0: float,
               t1: float, dt0: float, dt1: float, learningRate: float,
               length: int) -> tuple:
    newLearningRate = learningRate
    if len(lossHistory) > 1:
        if loss >= lossHistory[-1]:
            t0 += dt0 / length * learningRate
            t1 += dt1 / length * learningRate
            newLearningRate *= 0.5
        else:
            newLearningRate *= 1.05
    return (t0, t1, newLearningRate)

def	earlyStopping(lossHistory: list) -> bool:
    check = 8
    if len(lossHistory) > check:
        mean = sum(lossHistory[-check:]) / check
        last = lossHistory[-1]
        if round(mean, 9) == round(last, 9):
            return True
    return False

def	storeData(t0: float, t1: float, filename: str):
    with open(filename, 'w') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow([t0, t1])

def	plotting(t0: float, t1: float, mileages: list,
             prices: list, lossHistory: list,
             t0History: list, t1History: list):
    lineX = [float(min(mileages)), float(max(mileages))]
    lineY = []
    for elem in lineX:
        elem = t1 * normalizeElem(elem, mileages) + t0
        lineY.append(denormalizeElem(elem, prices))
    
    plt.figure(1)
    plt.plot(mileages, prices, 'bo', lineX, lineY, 'r-')
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.show()