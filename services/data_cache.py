import time

from services.google_sheet_service import get_master

# Cache variables
_cache = None
_cache_time = 0

# Refresh every 60 seconds
CACHE_SECONDS = 60


def get_master_rows(force_refresh=False):
    """
    Returns Google Sheet data.
    Downloads only once every CACHE_SECONDS.
    """

    global _cache
    global _cache_time

    now = time.time()

    if (
        force_refresh
        or _cache is None
        or (now - _cache_time) > CACHE_SECONDS
    ):

        print("🔄 Refreshing Google Sheet Cache...")

        ws = get_master()

        _cache = ws.get_all_records()

        _cache_time = now

    else:

        print("⚡ Using Cached Google Sheet")

    return _cache