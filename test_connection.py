from services.google_sheet_service import get_master

ws = get_master()

print(ws.title)

print(ws.row_count)

print(ws.col_count)