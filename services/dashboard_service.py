from datetime import datetime
from services.data_cache import get_master_df
from services.google_sheet_service import get_master
from services.pod_service import get_pending_pod
from services.photo_service import get_pending_photos

def get_dashboard_summary():

df = get_master_df()

    today = datetime.today()

    current_month = today.month
    current_year = today.year

    if current_month == 1:
        previous_month = 12
        previous_year = current_year - 1
    else:
        previous_month = current_month - 1
        previous_year = current_year

    current_month_trips = 0
    previous_month_trips = 0

    for _, row in df.iterrows():

        lr_date = str(row.get("LR DATE", "")).strip()

        if not lr_date:
            continue

        try:
            trip_date = datetime.strptime(lr_date, "%d/%m/%Y")
        except:
            continue

        if (
            trip_date.month == current_month
            and trip_date.year == current_year
        ):
            current_month_trips += 1

        elif (
            trip_date.month == previous_month
            and trip_date.year == previous_year
        ):
            previous_month_trips += 1
    pending_billing = 0

    for _, row in df.iterrows():

        bill_no = str(row.get("BILL NO", "")).strip()

        booking = row.get("BOOKING", 0)

        if bill_no == "":

            try:
                booking = float(str(booking).replace(",", ""))
                pending_billing += booking
            except:
                pass
    # ADD THESE TWO LINES
    pod = {"count": 0}
    photos = {"count": 0}
    return {

        "current_month_trips": current_month_trips,

        "previous_month_trips": previous_month_trips,

        "delivered": 0,

        "in_transit": 0,

        "pending_pod": pod["count"],

        "pending_billing": f"₹{pending_billing/100000:.1f} L",

        "pending_tracking": 0,

        "pending_photos": photos["count"]

    }


def get_company_summary():

    return [

        {"name": "PEPPL", "trips": 42},

        {"name": "PEIPL", "trips": 18},

        {"name": "PEGPL", "trips": 14},

        {"name": "PSPPL", "trips": 8},

        {"name": "TOSHIBA", "trips": 16},

        {"name": "RENEWSYS", "trips": 11}

    ]