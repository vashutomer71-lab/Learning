from Utilities.ReadProperties import ReadConfig

BASE_URL = ReadConfig.getBackEndUrl()

"""OR easy format:"""

AUTHENTICATE = f"{BASE_URL}/authenticate"
MUMIN_DASHBOARD = f"{BASE_URL}/api/getAllNiyatStatus"
TotalAndRedeemedTrophies =f"{BASE_URL}/api/getTotalAndRedeemedTrophies"
get_all_niyat_list_v2 = f"{BASE_URL}/api/getAllNiyatListV2"
search_on_niyat_list = f"{BASE_URL}/api/getAllNiyatListV2"
