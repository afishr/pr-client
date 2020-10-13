from fetcher import Fetcher
from parser import Parser

json = '[{"email":"hschukert2@arizona.edu","organization":"Bubblebox","full_name":"Heath Schukert","employee_id":"32-8682356"},\n{"email":"dbeautyman3@liveinternet.ru","organization":"Riffwire","full_name":"Daryl Beautyman","employee_id":"60-9658600"},\n{"email":"omacneilage4@cargocollective.com","organization":"Topicblab","full_name":"Orelle MacNeilage","employee_id":"74-5679141"},\n{"email":"kscamal8@jigsy.com","organization":"Yakijo","full_name":"Konrad Scamal","employee_id":"15-1125145"},\n{"email":"rdowning9@vimeo.com","organization":"Jabbertype","full_name":"Rancell Downing","employee_id":"87-0369483"},\n{"email":"aparnhama@printfriendly.com","organization":"Minyx","full_name":"Alyson Parnham","employee_id":"93-0291368"},\n{"email":"folenaneb@qq.com","organization":"Yotz","full_name":"Flemming O\'Lenane","employee_id":"64-6365740"},\n{"email":"jpavlitschekc@cnbc.com","organization":"Flipopia","full_name":"Jessamyn Pavlitschek","employee_id":"13-1792324"},\n{"email":"aabrahartd@mayoclinic.com","organization":"Oyoyo","full_name":"Angelia Abrahart","employee_id":"42-7009055"},\n{"email":"mjelki@nih.gov","organization":"Kazu","full_name":"Marshal Jelk","employee_id":"83-6689710"},\n{"email":"cdoustj@yellowpages.com","organization":"Zoomlounge","full_name":"Cass Doust","employee_id":"10-4732717"}]\n'

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<dataset>\n    <record>\n        <id>1</id>\n        <first_name>Ora</first_name>\n        <last_name>Syddie</last_name>\n        <bitcoin_address>1CLTQDLrw9t6CRiSypu2Hnd8ubhkkekbTp</bitcoin_address>\n    </record>\n    <record>\n        <id>2</id>\n        <first_name>Stoddard</first_name>\n        <last_name>Kielty</last_name>\n        <bitcoin_address>1LzEd765aq1RxqF3mTTsGac1DA3Bd4ZkxD</bitcoin_address>\n    </record>\n    <record>\n        <id>5</id>\n        <first_name>Wittie</first_name>\n        <last_name>Weller</last_name>\n        <bitcoin_address>14NXYyXmWDFK1JSFEunZ9AJq9mt1Xq3eAV</bitcoin_address>\n    </record>\n    <record>\n        <id>6</id>\n        <first_name>Koral</first_name>\n        <last_name>Bravey</last_name>\n        <bitcoin_address>1Npsbh7Yz1fZKqKnfadg5Uu2yBBfzWjKAZ</bitcoin_address>\n    </record>\n    <record>\n        <id>7</id>\n        <first_name>Brigit</first_name>\n        <last_name>Curless</last_name>\n        <bitcoin_address>1AQKrdRPHMAuGbkPFmmGsPfrCJm8YqS69J</bitcoin_address>\n    </record>\n</dataset>\n'

yaml = '---\n- id: 3\n  first_name: Collie\n  last_name: Venable\n  card_number: \'6304878179713534098\'\n  card_balance: \n  card_currency: \n- id: 6\n  first_name: Caroljean\n  last_name: Colwill\n  card_number: \'3540356838728217\'\n  card_balance: "$8796.02"\n  card_currency: IRR\n- id: 7\n  first_name: Nikki\n  last_name: Arnauduc\n  card_number: \'3580161468579083\'\n  card_balance: "$9476.63"\n  card_currency: PKR\n- id: 10\n  first_name: Riobard\n  last_name: Smeall\n  card_number: \'5307839238517296\'\n  card_balance: \n  card_currency: \n\n'

csv = 'id,username,email,created_account_data\n11,ncowopea,bedisa@soup.io,3/11/2019\n13,twickeyc,vlowsonc@privacy.gov.au,7/26/2019\n14,ebastind,bfarrearsd@ca.gov,12/20/2018\n17,shenningtong,blumberg@paypal.com,11/26/2018\n18,vgioanih,iandreoneh@hubpages.com,6/18/2019\n19,rbeckinghami,rrockelli@shop-pro.jp,3/25/2019\n'

def main():
  # results = Fetcher('http://localhost:5000').fetch()

  # Parser.parseJSON(json)
  print(Parser.parseXML(xml))

if __name__ == "__main__":
  main()
