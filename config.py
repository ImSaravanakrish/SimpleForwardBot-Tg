import os, re, time

id_pattern = re.compile(r'^.\d+$')


class Config:
    # Client Config              
    API_ID = int(os.environ.get("API_ID", "1779071")) # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "3448177952613312689f44b9d909b5d3") # ⚠️ Required       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6092537699:AAFdfZ5oo-P5peFlWJTN2iqzr_govF0jD-M") # ⚠️ Required
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")

    # Database Config 
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://filestream:filestream@cluster0.d1dlfzv.mongodb.net/?retryWrites=true&w=majority") # ⚠️ Required
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")

    # other configs 
    OWNER_ID = int(os.environ.get("OWNER_ID", "1169076058")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "")) # ⚠️ Required
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001751333376")) # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1001253253985') # ⚠️ Required
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    USERDATA = os.environ.get('USERDATA', 'USER_DATA')
    BOT_UPTIME  = time.time()
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None 
    BOT_USERNAME = os.environ.get('BOT_USERNAME', "NazriyaFilterBot") # No need if you don't want to auto forward when bot restarted
    SESSION = os.environ.get('STRING_SESSION', '') # ⚠️ Required 

    # Web Support 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True)) # for web support on/off
    PORT = os.environ.get("PORT","8080")


