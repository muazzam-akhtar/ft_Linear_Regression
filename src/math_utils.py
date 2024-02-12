def	normalizeElem(elem: float, _max: float, _min: float) -> float:
	return ((elem - _min) / (_max - _min))

def	denormalizeElem(elem: float, _max: float, _min: float) -> float:
	return ((elem * (_max - _min)) + _min)

def	normalizeData(data: list) -> list:
	_result = []
	for i in data:
		_result.append(normalizeElem(i, max(data), min(data)))
	return (_result)

def	lossFunction(t0: float, t1: float, mileages: list, prices: list) -> float:
	loss = 0.0
	for mileage, price in zip(mileages, prices):
		loss += (price - ((t1 * mileage) + t0)) ** 2
	return loss / len(mileages)