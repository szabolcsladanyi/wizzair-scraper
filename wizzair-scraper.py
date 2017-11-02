import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    #"Accept": "application/json, text/plain, */*",
    #"Accept-Encoding": "gzip, deflate, sdch, br",
    #"Accept-Language": "en-US,en;q=0.8,lt;q=0.6,ru;q=0.4",
}

s = requests.Session()
s.headers.update(headers)

# to get cookies
r = s.get("https://www.wizzair.com/")

payload = {
	"flightList":[
        {
		"departureStation": "BUD",
		"arrivalStation": "OPO",
		"from": "2017-12-01",
		"to": "2017-12-30"
        },
	{
                "departureStation": "OPO",
                "arrivalStation": "BUD",
                "from": "2017-12-01",
                "to": "2017-12-30"
	}
    	],
	"priceType": "regular"
}

url = 'https://be.wizzair.com/7.4.0/Api/search/timetable'

r = s.post(url, json=payload)

print(r.text)

data = r.json()

#print(data['outboundFlights'][0]['price']['amount'])
for i in data['outboundFlights']:
	print i['departureDates'][0]+ ' ::: ' + i['departureStation'] + ' --> ' + i['arrivalStation'] + ' === ' + str(i['price']['amount']) + str(i['price']['currencyCode'])

for i in data['returnFlights']:
        print i['departureDates'][0]+ ' ::: ' + i['departureStation'] + ' --> ' + i['arrivalStation'] + ' === ' + str(i['price']['amount']) + str(i['price']['currencyCode'])

