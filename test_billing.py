from services.billing_service import get_pending_billing_summary

data = get_pending_billing_summary()

print("Total Pending :", data["total_pending"])
print("Total Pending (Lakh):", data["total_pending_lakh"])
print("Total Trips :", data["total_trips"])

print("\nParty Wise Summary\n")

for row in data["summary"]:
    print(row)