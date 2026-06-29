import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from config import SPREADSHEET_ID, MASTER_SHEET, SERVICE_ACCOUNT

# =====================================================
# GOOGLE SHEETS CONFIG
# =====================================================

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

_client = None
_spreadsheet = None


# =====================================================
# CONNECT
# =====================================================

def get_client():
    global _client

    if _client is None:

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            SERVICE_ACCOUNT,
            SCOPES
        )

        _client = gspread.authorize(creds)

    return _client


# =====================================================
# SPREADSHEET
# =====================================================

def get_spreadsheet():
    global _spreadsheet

    if _spreadsheet is None:

        _spreadsheet = get_client().open_by_key(
            SPREADSHEET_ID
        )

    return _spreadsheet


# =====================================================
# WORKSHEETS
# =====================================================

def get_master():
    return get_spreadsheet().worksheet(MASTER_SHEET)


def get_tracking():
    return get_spreadsheet().worksheet("Tracking")


def get_statement():
    return get_spreadsheet().worksheet("Statement")


def get_trip():
    return get_spreadsheet().worksheet("Trip")


def get_goods():
    return get_spreadsheet().worksheet("Goods")


def get_wallet():
    return get_spreadsheet().worksheet("Wallet")


def get_manual():
    return get_spreadsheet().worksheet("MANUAL")


def get_bank_statement():
    return get_spreadsheet().worksheet("Bank Statement")