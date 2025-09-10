import configparser
import os
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
    def get_db_host():
        db_host = config.get('DB details', 'db_host')
        return db_host
    @staticmethod
    def get_db_user():
        db_username = config.get('DB details', 'db_user')
        return db_username
    @staticmethod
    def get_db_password():
        db_password = config.get('DB details', 'db_password')
        return db_password
    @staticmethod
    def get_db_name():
        db_name = config.get('DB details', 'db_name')
        return db_name
    @staticmethod
    def get_db_port():
        db_port = config.get('DB details', 'db_port')
        return db_port
    @staticmethod
    def get_ssh_host():
        ssh_host = config.get('SSH details', 'ssh_host')
        return ssh_host
    @staticmethod
    def get_ssh_port():
        ssh_port = config.get('SSH details', 'ssh_port')
        return ssh_port
    @staticmethod
    def get_ssh_user():
        ssh_user = config.get('SSH details', 'ssh_user')
        return ssh_user
    @staticmethod
    def get_ssh_key():
        ssh_key_path = config.get('SSH details', 'ssh_pkey')
        return ssh_key_path

    @staticmethod
    def get_local_host():
        local_host = config.get('SSH details', 'local_host')
        return local_host

    @classmethod
    def get_ssh_pkey(cls):
        pass


# Test reading the config
if __name__ == "__main__":
    print(f"URL: {ReadConfig.getApplicationURL()}")
    print(f"Username: {ReadConfig.getUserName()}")
    print(f"Password: {ReadConfig.getPassword()}")
    print(f"DB host: {ReadConfig.get_db_host()}")
    print(f"DB port: {ReadConfig.get_db_port()}")
    print(f"DB User Name : {ReadConfig.get_db_user()}")
    print(f"DB Password : {ReadConfig.get_db_password()}")
    print(f"ssh host name : {ReadConfig.get_ssh_host()}")
    print(f"ssh port : {ReadConfig.get_ssh_port()}")
    print(f"ssh user name : {ReadConfig.get_ssh_user()}")
    print(f"ssh key : {ReadConfig.get_ssh_key()}")
    print(f"local host: {ReadConfig.get_local_host()}")




















