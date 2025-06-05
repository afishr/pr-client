import socket
from fetcher import Fetcher
from parser import Parser
from store import Store
from display import Display
from concurrent.futures import ThreadPoolExecutor

def serve(port):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind(('', port))
  server.listen(6)
  print('$ netcat localhost', port)

  executor = ThreadPoolExecutor(max_workers=6)
  while True:
    client, address = server.accept()
    executor.submit(processRequest, client, address)

def processRequest(client, address):
  try:
    print('Connected', address)

    while True:
      client.sendall(b'> ')
      query = client.recv(1024)
      if not query:
        break

      res = processQuery(query.decode())
      if res:
        res = res + '\n\n'
        client.sendall(res.encode())
      else:
        client.sendall(b'Invalid request\n\n')

    print('Disconnected', address)
  finally:
    client.close()

def processQuery(query):
  query = query.replace('\n', '').split(' ')
  command = query[0].lower()

  if command == 'selectcolumn':
    try:
      args = query[1]
    except IndexError:
      return False

    args = args.split(',')
    args = list(filter(lambda element: element, args))

    if '*' in args:
      storedData = store.selectAllColumns()
    else:
      storedData = store.selectColumns(args)

    return Display.getTableString(storedData)
  else:
    return False


if __name__ == "__main__":
  results = Fetcher('http://localhost:3001').fetch()
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

  serve(8881)
