from flask import Blueprint, render_template

from api.dashboard_api import (
    get_dashboard_data,
    get_company_data
)

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/")
def dashboard():

    data = get_dashboard_data()

    companies = get_company_data()

    return render_template(
        "dashboard/dashboard.html",
        data=data,
        companies=companies
    )