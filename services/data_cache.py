import time
import pandas as pd

from services.google_sheet_service import get_master

_cache_df = None
_cache_time = 0

CACHE_SECONDS = 60


def get_master_df(force_refresh=False):

    global _cache_df
    global _cache_time

    now = time.time()

    if (
        force_refresh
        or _cache_df is None
        or (now - _cache_time) > CACHE_SECONDS
    ):

        print("🔄 Refreshing Google Sheet Cache...")

        ws = get_master()

        rows = ws.get_all_records()

        df = pd.DataFrame(rows)

        df.columns = df.columns.str.strip().str.upper()

        for col in df.columns:
            df[col] = df[col].astype(str)

        _cache_df = df

        _cache_time = now

    else:

        print("⚡ Using Cached DataFrame")

    return _cache_df.copy()