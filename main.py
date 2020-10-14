from fetcher import Fetcher
from parser import Parser

def main():
  results = Fetcher('http://localhost:5000').fetch()

  for element in results:
    print()
    data = element['data']
    if 'mime_type' in element:
      mimeType = element['mime_type']

      if mimeType == 'application/xml':
        print(Parser.parseXML(data))
      elif mimeType == 'text/csv':
        print(Parser.parseCSV(data))
      elif mimeType == 'application/x-yaml':
        print(Parser.parseYAML(data))
    else:
      print(Parser.parseJSON(data))

    print()


if __name__ == "__main__":
  main()
