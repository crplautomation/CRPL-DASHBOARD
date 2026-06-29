from collections import defaultdict
from datetime import datetime, timedelta
from services.excel_formatter import format_excel
from services.google_sheet_service import get_master

EXCLUDE_PARTIES = {
    "PEPPL",
    "PEIPL",
    "PEGPL",
    "PSPPL",
    "PEL"
}


def parse_date(date_str):

    for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"):

        try:
            return datetime.strptime(str(date_str), fmt).date()
        except:
            pass

    return None


def get_pending_pod():

    ws = get_master()

    rows = ws.get_all_records()

    today = datetime.today().date()

    cutoff = today - timedelta(days=2)

    summary = defaultdict(int)

    details = []

    total_count = 0

    for row in rows:

        party = str(row.get("PARTY NAME", "")).strip().upper()

        bill_no = str(row.get("BILL NO", "")).strip()

        pod_status = str(row.get("POD STATUS", "")).strip().upper()

        lr_date = parse_date(row.get("LR DATE", ""))

        if party in EXCLUDE_PARTIES:
            continue

        if bill_no != "":
            continue

        if pod_status != "POD NOT RECEIVED":
            continue

        if lr_date is None:
            continue

        if lr_date >= cutoff:
            continue

        summary[party] += 1

        total_count += 1

        details.append({

            "lr_no": row.get("LR NO", ""),

            "lr_date": row.get("LR DATE", ""),

            "from": row.get("FROM ", ""),

            "to": row.get("TO", ""),

            "vehicle": row.get("VEHICLE NO", ""),

            "broker": row.get("BROKER NAME", ""),

            "driver": row.get("DRIVER NO", ""),

            "party": row.get("PARTY NAME", ""),

            "state": row.get("STATE", "")

        })

    summary_rows = []

    for party, count in summary.items():

        summary_rows.append({

            "party": party,

            "count": count

        })

    summary_rows.sort(
        key=lambda x: x["count"],
        reverse=True
    )

    return {

        "count": total_count,

        "summary": summary_rows,

        "details": details

    }
from openpyxl import Workbook

def get_pending_pod_excel():

    data = get_pending_pod()

    wb = Workbook()
    ws = wb.active

    ws.title = "Pending POD"

    ws.append([
        "LR NO",
        "LR DATE",
        "FROM",
        "TO",
        "VEHICLE NO",
        "BROKER NAME",
        "DRIVER NO",
        "PARTY NAME",
        "STATE"
    ])

    for row in data["details"]:

        ws.append([
            row["lr_no"],
            row["lr_date"],
            row["from"],
            row["to"],
            row["vehicle"],
            row["broker"],
            row["driver"],
            row["party"],
            row["state"]
        ])

    file_name = "Pending_POD.xlsx"
    format_excel(ws) 
    wb.save(file_name)

    return file_name