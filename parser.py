import xmltodict
import json

class Parser:

  @staticmethod
  def parseXML(raw):
    return json.dumps(xmltodict.parse(raw)['dataset']['record'])

  @staticmethod
  def parseJSON(raw):
    print(json.loads(raw))
