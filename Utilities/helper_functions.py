from Utilities.ReadProperties import ReadConfig
from datetime import date
from dateutil.relativedelta import relativedelta

def format_date(d: date) -> str:
    return d.strftime("%Y-%m-%d")

def get_filter_date_range(filter_key: str):
    today = date.today()
    end_date = today

    if filter_key == "all":
        start_date = end_date - relativedelta(years=20)
    elif filter_key == "1m":
        start_date = end_date - relativedelta(months=1)
    elif filter_key == "3m":
        start_date = end_date - relativedelta(months=3)
    elif filter_key == "6m":
        start_date = end_date - relativedelta(months=6)
    elif filter_key == "1y":
        start_date = end_date - relativedelta(years=1)
    else:
        raise ValueError(f"Invalid filter key: {filter_key}")

    return format_date(start_date), format_date(end_date)
