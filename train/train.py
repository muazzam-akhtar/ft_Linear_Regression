from utils import fetchData
from utils import getPath

def	main():
    mileages, prices = fetchData(getPath('data.csv'))
    print(mileages, prices)
    

if __name__ == '__main__':
	main()