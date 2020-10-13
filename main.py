from fetcher import Fetcher

def main():
  results = Fetcher('http://localhost:5000').fetch()

  for element in results:
    print()
    print(element)
    print()

if __name__ == "__main__":
  main()
