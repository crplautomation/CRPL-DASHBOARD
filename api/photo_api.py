from services.photo_service import get_pending_photos


def pending_photos_api():
    return get_pending_photos()