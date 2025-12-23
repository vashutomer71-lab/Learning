import requests
from Utilities.helper_functions import get_filter_date_range
from APIs import endpoints
from APIs.headers import auth_headers
from pageObjects.mumin_dashboard_page import MuminDashboardPage


class MuminDashbaordAPi:

    def _get(self, token, its_id, filter_key):
        """Common internal method that returns dict of dashboard data."""
        start, end = get_filter_date_range(filter_key)
        url = f"{endpoints.MUMIN_DASHBOARD}?startDate={start}&endDate={end}&itsId={its_id}"
        print("Final URL:", url)
        res = requests.get(url, headers=auth_headers(token))
        if res.status_code != 200:
            raise AssertionError(f"Dashboard API failed: {res.status_code}")
        data = res.json().get("data") or {}
        # One-line dict creation
        return {
            "total": data.get("totalNiyat", 0),
            "active": data.get("active", 0),
            "pending": data.get("approvalPending", 0),
            "completed": data.get("completed", 0),
            "deactivated": data.get("deactivated", 0),
        }

    # ---------------- PUBLIC METHODS (Return format unchanged) ---------------- #

    def get_dashboard_api_data_all_filter(self, token, its_id, filter_key="all"):
        d = self._get(token, its_id, filter_key)
        return d["total"], d["active"], d["pending"], d["completed"], d["deactivated"]

    def get_dashboard_api_data_1month_filter(self, token, its_id, filter_key="1m"):
        d = self._get(token, its_id, filter_key)
        total_sum = sum(d.values())
        return d["total"], d["active"], d["pending"], d["completed"], d["deactivated"], total_sum

    def get_dashboard_api_data_3_month_filter(self, token, its_id, filter_key="3m"):
        d = self._get(token, its_id, filter_key)

        # original logic kept (3m sum does NOT include total)
        total_sum = d["active"] + d["pending"] + d["completed"] + d["deactivated"]

        return d["total"], d["active"], d["pending"], d["completed"], d["deactivated"], total_sum
    
    def get_dashboard_api_data_6_month_filter(self, token, its_id, filter_key="6m"):
        d = self._get(token, its_id, filter_key)

        # original logic kept (3m sum does NOT include total)
        total_sum = d["active"] + d["pending"] + d["completed"] + d["deactivated"]

        return d["total"], d["active"], d["pending"], d["completed"], d["deactivated"], total_sum
    
    def get_dashboard_api_data_1_year_filter(self, token, its_id, filter_key="1y"):
        d = self._get(token, its_id, filter_key)

        # original logic kept (3m sum does NOT include total)
        total_sum = d["active"] + d["pending"] + d["completed"] + d["deactivated"]

        return d["total"], d["active"], d["pending"], d["completed"], d["deactivated"], total_sum
    
    def trophy_counts(self, token, its_id):
        trophies_count_url = f"{endpoints.TotalAndRedeemedTrophies}?itsId={its_id}"
        print(f"The trophy end point url: {trophies_count_url}")
        response = requests.get(trophies_count_url, headers=auth_headers(token))
        print("Trophy response is:", response)
        print("Trophy response code is:", response.status_code)
        if response.status_code != 200:
            raise AssertionError(f"The api failed and the status code is {response.status_code}")

        data = response.json().get("data") or {}
        # Convert safely to integers
        remaining = int(data.get("remainingTrophies") or 0)
        redeemed = int(data.get("trophiesRedeemed") or 0)
        total = remaining + redeemed

        print(f"Remaining = {remaining}, Redeemed = {redeemed}, Total = {total}")

        return {
            "redeemed": redeemed,
            "remaining": remaining,
            "total": total
        }
    
    def get_all_niyat_V2_list(self, token, its_id, filter_key='all'):
        start, end = get_filter_date_range(filter_key)
        url = f"{endpoints.get_all_niyat_list_v2}?startDate={start}&endDate={end}&itsId={its_id}&search="
        response = requests.get(url, headers=auth_headers(token))
        if response.status_code !=200:
            raise AssertionError (f"The api is failed and the status code is:  {response.status_code}")
        data = response.json().get("data")
        pagination = data.get("pagination")
        total_count_pagination = pagination.get("totalRecords")
        print("Total niyat count is paginationis:  {total_count_pagination}")
        return total_count_pagination
    
    def search_niyat_list(self, token, its_id, db_umoor_name,filter_key= 'all'):
        start, end = get_filter_date_range(filter_key)
        url = f"{endpoints.search_on_niyat_list}?startDate={start}&endDate={end}&itsId={its_id}&search={db_umoor_name}"
        print(f"search api url is:  {url}")
        response = requests.get(url, headers=auth_headers(token))
        print("Response code is: ", response.status_code)
        get_data = response.json().get("data") or {}
        pagination = get_data.get("pagination") or {}
        total_count_after_search = pagination.get("totalRecords")
        print("The count is niyat in pagination is:", total_count_after_search)
        return total_count_after_search


