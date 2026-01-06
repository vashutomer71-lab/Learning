import configparser
import os

# Construct the path to the config.ini file
config_path = os.path.join(os.path.dirname(__file__), "..", "Configuration", "config.ini")

# Print the path to verify
print(f"Reading config from: {config_path}")

config = configparser.RawConfigParser()
config.read(config_path)

if not config.sections():
    raise Exception(f"Config file not found or empty: {config_path}")

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def get_back_end_url():
        back_end_url = config.get('common info', 'back_end_url')
        return back_end_url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_login_url():
        login_url = config.get('common info', 'login_url')
        return login_url

    @staticmethod
    def get_db_name():
        db_name = config.get('database', 'dbname')
        return db_name

    @staticmethod
    def get_user():
        db_username = config.get('database', 'user')
        return db_username

    @staticmethod
    def get_password():
        db_password = config.get('database', 'db_password')
        return db_password

    @staticmethod
    def get_host():
        host_url = config.get('database', 'host')
        return host_url

    @staticmethod
    def get_port():
        db_port = config.get('database', 'port')
        return db_port


# Test reading the config
if __name__ == "__main__":
    print(f"URL: {ReadConfig.getApplicationURL()}")
    print(f"Username: {ReadConfig.getUserName()}")
    print(f"Password: {ReadConfig.getPassword()}")
    print(f"db_name: {ReadConfig.get_db_name()}")
    print(f" db user name: {ReadConfig.get_user()}")
    print(f"db password :{ReadConfig.getPassword()}")
    print(f"db host : {ReadConfig.get_host()}")
    print(f"db port: {ReadConfig.get_port()}")
    print(f"login url: {ReadConfig.get_login_url()}")
    print(f"back end url: {ReadConfig.get_back_end_url()}")

