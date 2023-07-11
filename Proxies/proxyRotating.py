import requests

with open('./filteredProxies.txt', 'r') as proxyFile:
    proxyList = proxyFile.read().splitlines()
    
for count in range(10):
    proxies = {'https': proxyList[count%len(proxyList)], 'http': proxyList[count%len(proxyList)]}
    try:
        resp = requests.get('http://ipinfo.io/json', proxies=proxies, timeout=10)
        print(f"For Proxy {proxyList[count%len(proxyList)]}:")
        if(resp.status_code==200):
            print(resp.json())
    except:
        pass