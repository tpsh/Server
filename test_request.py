import requests;

# url = "https://api.github.com/search/users?q=location:{0}+language:{1}".format(first, second)
url = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=62078294d9aa47698bc140823161303&q=Vladivostok&date=2015-12-01&format=json&enddate=2015-12-31"
response_dict = requests.get(url).json()
print(response_dict)
