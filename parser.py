import xmltodict
import json
import yaml
import csv
import ast

class Parser:

  @staticmethod
  def __clean_json(raw):
    raw = raw.replace('null', 'None').replace('true', 'True').replace('false', 'False')
    return ast.literal_eval(raw)

  @staticmethod
  def parseXML(raw):
    return json.dumps(xmltodict.parse(raw)['dataset']['record'])

  @staticmethod
  def parseJSON(raw):
    return json.dumps(Parser.__clean_json(raw))

  @staticmethod
  def parseYAML(raw):
    return yaml.safe_load(raw)

  @staticmethod
  def parseCSV(raw):
    data = []
    csvReader = csv.DictReader(raw.splitlines())
    for rows in csvReader:
      data.append(rows)

    return data
