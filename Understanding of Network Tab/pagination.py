import requests

url = "https://www.laufen.co.at/automatic-category-detail?p_p_id=ProductList_INSTANCE_80H5hgzHtYEp&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&roca_env=3vjR5WgLKZIHLB3Uu8eoUA%3D%3D"

with open('./payloadPagination.txt', 'r') as my_file:
    payload = my_file.read()

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Requested-With': 'XMLHttpRequest',
  'Origin': 'https://www.laufen.co.at',
  'Connection': 'keep-alive',
  'Referer': 'https://www.laufen.co.at/produkte/waschtische-wandhangend?page=1',
  'Cookie': 'GUEST_LANGUAGE_ID=de_DE; _pin_unauth=dWlkPU1UUTFOak01TXprdFlXTXhNaTAwT1RNNUxXRmlOekF0TURFeFptRmpOV0U1WkdJMQ; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jul+10+2023+16%3A20%3A24+GMT%2B0500+(Pakistan+Standard+Time)&version=202210.1.0&isIABGlobal=false&hosts=&consentId=98768aa7-aaa0-4e1f-ac69-9efa80fa1ee3&interactionCount=2&landingPath=NotLandingPage&groups=C0004%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false&geolocation=%3B; _ga_BPY6HHXTQX=GS1.1.1688984280.13.1.1688988031.48.0.0; _ga=GA1.3.1030190087.1688804038; _ga_NGNL8PVVV5=GS1.1.1688984280.13.1.1688988031.48.0.0; _fbp=fb.2.1688804043560.538948168; OptanonAlertBoxClosed=2023-07-08T08:14:36.533Z; sizeFav=0; sizeComparator=1; JSESSIONID=80AE2A0A069C9999F6778BBE8E17100C; ln_or=eyI1NTgwMjMzIjoiZCJ9; LFR_SESSION_STATE_20103=1688988024642; _gid=GA1.3.1475424855.1688976731; _dc_gtm_UA-23220698-3=1; _gat_UA-23220698-3=1; _gat_UA-23220698-41=1; GUEST_LANGUAGE_ID=de_DE; JSESSIONID=A4E113FAB907C5C208813D4F83B55720',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin'
}

def getUrls():
    global payload
    links = []
    # Get to all pages using recurison and changing payload
    def getJSON(count, payload=payload):
        response = requests.request("POST", url, headers=headers, data=payload.format(count))
        obj = response.json()
        if(obj['currentPage']<=obj['maxPages']):
            print(obj['currentPage'], obj['maxPages'])
            for prod in obj['products']:
                links.append(prod['url'])
            getJSON(count+1) if obj['currentPage']<obj['maxPages'] else ''
        else:
            return
    getJSON(1)
    print(len(links))
getUrls()