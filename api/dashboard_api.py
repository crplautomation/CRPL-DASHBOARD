from services.dashboard_service import (
    get_dashboard_summary,
    get_company_summary
)


def get_dashboard_data():
    return get_dashboard_summary()


def get_company_data():
    return get_company_summary()