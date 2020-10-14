from prettytable import PrettyTable

class Display:

  @staticmethod
  def getTable(raw):
    table = PrettyTable(raw.keys())
    length = len(raw[next(iter(raw))])

    for i in range(length):
      isVisible = False
      row = []

      for key in raw:
        data = raw[key]
        isVisible = isVisible or data[i]
        row.append(data[i])

      if isVisible:
        table.add_row(row)

    return table

  @staticmethod
  def printTable(raw):
    table = Display.getTable(raw)
    print(table)

  @staticmethod
  def getTableString(raw):
    table = Display.getTable(raw)
    return table.get_string()

