from fetcher import Fetcher

def main():
	results = Fetcher('http://0.0.0.0:5000').fetch()


	print(results)

if __name__ == "__main__":
	main()
