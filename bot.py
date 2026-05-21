import urllib.request, json, urllib.parse, time

# المتغيرات الخاصة بك
TOKEN = "8706248467:AAF-jJ-hmYehFK_mzp04ZQcUCWF-tkhnjG4"
CHAT_ID = 709511655

def get_gold_price():
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/GC=F?interval=1m&range=1m"
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            return float(data['chart']['result'][0]['meta']['regularMarketPrice'])
    except: 
        return 0.0

def send_menu(msg):
    kb = {"inline_keyboard": [[{"text": "💰 السعر", "callback_data": "price"}], [{"text": "📊 تحليل", "callback_data": "analysis"}]]}
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg, "reply_markup": json.dumps(kb), "parse_mode": "Markdown"}
    data = urllib.parse.urlencode(payload).encode()
    urllib.request.urlopen(url, data=data)

last_id = 0
print("البوت يعمل الآن على السحابة...")

while True:
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={last_id + 1}"
        with urllib.request.urlopen(url, timeout=5) as res:
            data = json.loads(res.read().decode())
            for update in data.get("result", []):
                last_id = update["update_id"]
                if "callback_query" in update:
                    val = update["callback_query"]["data"]
                    price = get_gold_price()
                    if val == "price": 
                        send_menu(f"السعر الحالي: {price}")
                    elif val == "analysis": 
                        send_menu(f"السوق مستقر عند: {price}")
    except: 
        pass
    time.sleep(2)
