from fetcher import Fetcher
from parser import Parser
from store import Store

def main():
  results = Fetcher('http://localhost:5000').fetch()
  store = Store()

  for element in results:
    data = element['data']
    if 'mime_type' in element:
      mimeType = element['mime_type']

      if mimeType == 'application/xml':
        store.adds(Parser.parseXML(data))
      elif mimeType == 'text/csv':
        store.adds(Parser.parseCSV(data))
      elif mimeType == 'application/x-yaml':
        store.adds(Parser.parseYAML(data))

    else:
      store.adds(Parser.parseJSON(data))

  print(store.selectColumns(['first_name', 'last_name','email']))


if __name__ == "__main__":
  main()
