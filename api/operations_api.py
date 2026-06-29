def get_operations_summary():

    return {

        "today_trips":156,

        "running":42,

        "pending_pod":18,

        "pending_tracking":12,

        "pending_photos":7,

        "delivered":124

    }


def get_recent_trips():

    return [

        {
            "vehicle":"TS08AB1234",
            "from":"Kothur",
            "to":"Pune",
            "status":"Running"
        },

        {
            "vehicle":"TS09XY5678",
            "from":"Hyderabad",
            "to":"Chennai",
            "status":"Delivered"
        },

        {
            "vehicle":"TS10CD4567",
            "from":"Maheshwaram",
            "to":"Mumbai",
            "status":"POD Pending"
        }

    ]