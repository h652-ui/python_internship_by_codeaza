import requests

print('\nThis Program fetch all time best cricketer in every format\n')

url = "https://cricketapi-icc.pulselive.com/icc-ratings/allTimeBestPlayers?playerRatingRole={}&matchScope={}&pageSize=10&dmsPlayerIdRequired=true"

dept = input("Enter Department : ")
format = input("Enter Format : ")


resp = requests.get(url.format(dept, format))
content = resp.json()['content']

for rank, player in enumerate(content):
    name = player['player']['fullName']
    nationality = player['player']['nationality']
    print(f"\nRank No: {rank}")
    print(f"Name:  {name}")
    print(f"Nationality:  {nationality}\n")