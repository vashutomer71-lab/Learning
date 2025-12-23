from Utilities.ReadProperties import ReadConfig

USERNAME = ReadConfig.getUserName()
PASSWORD = ReadConfig.getPassword()

AUTH_PAYLOAD = {
    "itsId": USERNAME,
    "password": PASSWORD,
    "isMumin": True
}
