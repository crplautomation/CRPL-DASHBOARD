from collections import defaultdict
from datetime import datetime
from openpyxl import Workbook
from services.data_cache import get_master_df
PREMIER = {
    "PEPPL",
    "PEIPL",
    "PEGPL",
    "PSPPL",
    "PEL"
}


def get_pending_billing():

df = get_master_df()

    today = datetime.today().date()

    summary = defaultdict(
        lambda: {
            "amount": 0,
            "trips": 0,
            "oldest_days": 0
        }
    )

    details = []

    for _, row in df.iterrows():

        bill_no = str(row.get("BILL NO", "")).strip()

        if bill_no != "":
            continue

        party = str(row.get("PARTY NAME", "")).strip().upper()

        if party in PREMIER:
            group = "PREMIER"

        elif "HBL" in party:
            group = "HBL"

        else:
            group = party

        booking = row.get("BOOKING", 0)

        try:
            booking = float(str(booking).replace(",", ""))
        except:
            booking = 0

        lr_date = str(row.get("LR DATE", "")).strip()

        age = 0

        try:
            d = datetime.strptime(lr_date, "%d/%m/%Y").date()
            age = (today - d).days
        except:
            pass

        summary[group]["amount"] += booking
        summary[group]["trips"] += 1

        if age > summary[group]["oldest_days"]:
            summary[group]["oldest_days"] = age

        details.append({

            "group": group,

            "party": row.get("PARTY NAME", ""),

            "lr_no": row.get("LR NO", ""),

            "lr_date": lr_date,

            "from": row.get("FROM", ""),

            "to": row.get("TO", ""),

            "vehicle": row.get("VEHICLE NO", ""),

            "booking": booking,

            "bill_no": bill_no,

            "age_days": age

        })

    summary_rows = []

    for party, data in summary.items():
      
        if data["amount"] <= 0:
            continue

        summary_rows.append({

            "party": party,

            "amount": data["amount"],

            "amount_lakh": round(data["amount"] / 100000, 1),

            "trips": data["trips"],

            "oldest_days": data["oldest_days"]

        })

    summary_rows.sort(
        key=lambda x: x["amount"],
        reverse=True
    )

    return {

        "summary": summary_rows,

        "details": details
    }
from openpyxl import Workbook

def get_pending_billing_details_excel():

    data = get_pending_billing()

    wb = Workbook()
    ws = wb.active

    ws.title = "Pending Billing"

    ws.append([
        "PARTY NAME",
        "LR NO",
        "LR DATE",
        "FROM",
        "TO",
        "VEHICLE NO",
        "BOOKING",
        "BILL NO",
        "AGE (DAYS)"
    ])

    for row in data["details"]:

        ws.append([
            row["party"],
            row["lr_no"],
            row["lr_date"],
            row["from"],
            row["to"],
            row["vehicle"],
            row["booking"],
            row["bill_no"],
            row["age_days"]
        ])

    file_name = "Pending_Billing.xlsx"
    wb.save(file_name)

    return file_name


  