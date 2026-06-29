from flask import Blueprint, jsonify, send_file
from datetime import datetime

from api.pod_api import pending_pod_api
from services.pod_service import get_pending_pod_excel

pod_bp = Blueprint(
    "pod",
    __name__
)


@pod_bp.route("/api/pending-pod")
def pending_pod():

    return jsonify(
        pending_pod_api()
    )


@pod_bp.route("/api/pending-pod/export")
def export_pending_pod():

    file_path = get_pending_pod_excel()

    today = datetime.now().strftime("%d-%m-%Y")

    return send_file(
        file_path,
        as_attachment=True,
        download_name=f"Pending_POD_{today}.xlsx"
    )