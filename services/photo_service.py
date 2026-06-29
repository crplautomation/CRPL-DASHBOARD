from collections import defaultdict
import pandas as pd
from openpyxl import Workbook
from services.data_cache import get_master_df
from services.excel_formatter import format_excel

VALID_PARTIES = [
    "PEPPL",
    "PEIPL",
    "PEGPL",
    "PSPPL",
    "PEL",
    "SOLAR SQUARE"
]


def get_pending_photos():

df = get_master_df()

    # Remove duplicate LRs
    if "LR NO".upper() in df.columns:
        df = df.drop_duplicates(subset=["LR NO"], keep="last")

    # Convert every column to string
    for col in df.columns:
        df[col] = df[col].astype(str)

    # SAME FILTER AS YOUR OLD SCRIPT
    filtered = df[
        (df["PARTY NAME"].str.strip().isin(VALID_PARTIES))
        & (df["BILL DATE"].str.strip() == "")
        & (df["POD STATUS"].str.upper().str.strip() == "POD NOT RECEIVED")
        & (df["STATUS"].str.upper().str.strip() == "UNLOADED")
        & (df["MARKET PE NO."].str.strip() != "")
        & (~df["TYPE OF VEHICLE"].str.upper().str.contains("LOCAL", na=False))
    ]

    summary = (
        filtered.groupby("PARTY NAME")
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    summary_rows = summary.to_dict("records")

    details = []

    for _, r in filtered.iterrows():

        details.append({

            "lr_no": r["LR NO"],
            "lr_date": r["LR DATE"],
            "from": r["FROM"],
            "to": r["TO"],
            "vehicle": r["VEHICLE NO"],
            "broker": r["BROKER NAME"],
            "driver": r["DRIVER NO"],
            "party": r["PARTY NAME"]

        })

    return {

        "count": len(filtered),

        "summary": summary_rows,

        "details": details

    }


def get_pending_photos_excel():

    data = get_pending_photos()

    wb = Workbook()

    ws = wb.active

    ws.title = "Pending Photos"

    ws.append([
        "LR NO",
        "LR DATE",
        "FROM",
        "TO",
        "VEHICLE NO",
        "BROKER NAME",
        "DRIVER NO",
        "PARTY NAME"
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
            row["party"]
        ])

    format_excel(ws)

    file_name = "Pending_Photos.xlsx"

    wb.save(file_name)

    return file_name