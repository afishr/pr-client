class Store:

  def __init__(self, init_list=[]):
    self.__list = init_list

  def add(self, data):
    self.__list.append(data)

  def adds(self, data):
    for el in data:
      self.add(el)

  def selectColumn(self, name):
    results = []
    for element in self.__list:
      if name in element:
        results.append(element[name])
      else:
        results.append(None)
    return {name: results}

  def selectColumns(self, names):
    results = {}
    for name in names:
      results.update(self.selectColumn(name))
    return results

  def selectAllColumns(self):
    columnNames = set()

    for entry in self.__list:
      columnNames = columnNames | set(list(entry.keys()))

    return self.selectColumns(list(columnNames))
