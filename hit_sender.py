import requests

def send(cc, last, username, time_taken):
    ii = cc[:6]

    try:
        response = requests.get(f'https://web-production-71334.up.railway.app/bin-info?bin={ii}')
        data = response.json()

        if response.status_code == 200:
            bank = data.get("Bank name", "Unknown")
            emj = data.get("Flag", "🏳️")
            do = data.get("Country name", "Unknown")
            dicr = data.get("Brand", "Unknown")
            typ = data.get("Type", "Unknown")
        else:
            print(f"API Error: {data.get('error', 'Unknown error')}")
            bank = emj = do = dicr = typ = 'Unknown'
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        bank = emj = do = dicr = typ = 'Unknown'

    msg1 = f"""
𝗚𝗔𝗧𝗘𝗪𝗔𝗬 ➜ SanjiPay $1.00        

𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 ➜ {last}             
𝗖𝗖 ➜ <code>{cc}</code>       
𝗕𝗜𝗡 ➜ {ii}                   
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 ➜ {do}               
𝗕𝗔𝗡𝗞 ➜ {bank}                
𝗙𝗟𝗔𝗚 ➜ {emj}                 

Check by @{username}
𝗕𝗼𝘁 𝗯𝘆: @strawhatchannel96
"""
    return msg1
