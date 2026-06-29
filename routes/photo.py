from flask import Blueprint, jsonify, send_file
from datetime import datetime

from api.photo_api import pending_photos_api
from services.photo_service import get_pending_photos_excel

photo_bp = Blueprint(
    "photo",
    __name__
)


@photo_bp.route("/api/pending-photos")
def pending_photos():

    return jsonify(
        pending_photos_api()
    )


@photo_bp.route("/api/pending-photos/export")
def export_pending_photos():

    file_path = get_pending_photos_excel()

    today = datetime.now().strftime("%d-%m-%Y")

    return send_file(
        file_path,
        as_attachment=True,
        download_name=f"Pending_Photos_{today}.xlsx"
    )