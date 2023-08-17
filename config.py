import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22299340")

API_HASH = os.environ.get("API_HASH", "09b09f3e2ff1306da4a19888f614d937")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6544161566:AAGRs0j26zsEecrrzCGzth77tdJ6IF7p8hE") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","jidovi4576")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://jidovi4576:B6HywpSzpSqZZ3W@clusterbot2.ezfn734.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
