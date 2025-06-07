from fetcher import Fetcher
from store import Store
from server import Server

if __name__ == "__main__":
  data = Fetcher(base_url='http://localhost:3001').fetch()
  store = Store(data)
  Server(store).serve(8881)
