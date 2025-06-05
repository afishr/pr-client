from fetcher import Fetcher
from store import Store
from server import Server

if __name__ == "__main__":
  store = Store()
  Fetcher(store).fetch('http://localhost:3001')
  Server(store).serve(8881)
