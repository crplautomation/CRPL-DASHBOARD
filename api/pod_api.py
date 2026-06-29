from services.pod_service import get_pending_pod


def pending_pod_api():
    return get_pending_pod()