from services.billing_service import get_pending_billing

def pending_billing_api():
    return get_pending_billing()