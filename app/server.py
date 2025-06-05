import socket
from display import Display
from concurrent.futures import ThreadPoolExecutor

from store import Store


class Server:
  def __init__(self, store):
    self.store = store

  def serve(self, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', port))
    server.listen(6)

    print('$ netcat localhost', port)

    executor = ThreadPoolExecutor(max_workers=6)
    try:
        while True:
            client, address = server.accept()
            executor.submit(self.processRequest, client, address)
    except KeyboardInterrupt:
        print("\nShutting down server gracefully...")
    finally:
        server.close()
        executor.shutdown(wait=True)
        print("Server stopped.")

  def processRequest(self, client, address):
    try:
      print('Connected', address)

      while True:
        client.sendall(b'> ')
        query = client.recv(1024)
        if not query:
          break

        res = self.processQuery(query.decode())
        if res:
          res = res + '\n\n'
          client.sendall(res.encode())
        else:
          client.sendall(b'Invalid request\n\n')

      print('Disconnected', address)
    finally:
      client.close()

  def processQuery(self, query):
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
        storedData = self.store.selectAllColumns()
      else:
        storedData = self.store.selectColumns(args)

      return Display.getTableString(storedData)
    else:
      return False
