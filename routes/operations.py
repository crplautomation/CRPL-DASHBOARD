from flask import Blueprint, render_template

from api.operations_api import (
    get_operations_summary,
    get_recent_trips
)

operations_bp = Blueprint(
    "operations",
    __name__,
    url_prefix="/operations"
)

@operations_bp.route("/")
def operations():

    summary = get_operations_summary()

    trips = get_recent_trips()

    return render_template(
        "operations/operations.html",
        summary=summary,
        trips=trips
    )