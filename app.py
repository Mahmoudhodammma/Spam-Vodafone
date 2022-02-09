import flask
import requests
from flask import *
app = Flask(__name__)
@app.route("/id/instagram/")
def fj():
	User = request.args.get("User")
	head = {
'HOST': "www.instagram.com",
'KeepAlive' : 'True',
'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
'Cookie': 'cookie',
'Accept' : "*/*",
'ContentType' : "application/x-www-form-urlencoded",
"X-Requested-With" : "XMLHttpRequest",
"X-IG-App-ID": "936619743392459",
"X-Instagram-AJAX" : "missing",
"X-CSRFToken" : "missing",
"Accept-Language" : "en-US,en;q=0.9"
}
	url_id = f'https://www.instagram.com/{User}/?__a=1'
	req_id = requests.get(url_id,headers=head).json()
	idd  = str(req_id['graphql']['user']['id'])
	return jsonify(Telegram="@uufffuu",ID=idd)
if __name__=="__main__":
	app.run()
