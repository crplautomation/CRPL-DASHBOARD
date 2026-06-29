from flask import Blueprint, jsonify, send_file
from datetime import datetime

from api.billing_api import pending_billing_api
from services.billing_service import get_pending_billing_details_excel

billing_bp = Blueprint(
    "billing",
    __name__
)


@billing_bp.route("/api/pending-billing")
def pending_billing():
    return jsonify(
        pending_billing_api()
    )


@billing_bp.route("/api/pending-billing/export")
def export_pending_billing():

    file_path = get_pending_billing_details_excel()

    today = datetime.now().strftime("%d-%m-%Y")

    return send_file(
        file_path,
        as_attachment=True,
        download_name=f"Pending_Billing_{today}.xlsx"
    )