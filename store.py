class Store:

  def __init__(self):
    self.__list = []

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
    return results
