from utils import getPath
from utils import fetchData
from utils import getThetas
from utils import estimatePrice

def	getAccuracy(thetas: tuple, mileages: list, prices: list) -> float:
	price_average = sum(prices) / len(prices)
	ssr = sum(map(lambda mileage, price: pow(price - estimatePrice(thetas,
        mileage, mileages, prices), 2), mileages, prices))
	sst = sum(map(lambda price: pow(price - price_average, 2), prices))
	return (1 - (ssr / sst))

def	main():
	thetas = getThetas(getPath('thetas.csv'))
	mileages, prices = fetchData(getPath('data.csv'))
	accuracy = getAccuracy(thetas, mileages, prices) * 100
	print("Accuracy is {:.5}%".format(accuracy))

if __name__ == '__main__':
	main()