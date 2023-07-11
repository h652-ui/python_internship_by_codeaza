import requests

filteredProxies = []

with open('./proxies.txt', 'r') as proxyFile:
    proxyList = proxyFile.read().splitlines()

for proxy in proxyList:
    proxies = {'https': proxy, 'http': proxy}
    try:
        resp = requests.get('http://ipinfo.io/json', proxies=proxies, timeout=10)
        print(proxy, resp.status_code)
        if(resp.status_code==200):
            filteredProxies.append(proxy)
    except:
        pass