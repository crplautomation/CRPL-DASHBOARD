from flask import Flask

from routes.dashboard import dashboard_bp
from routes.operations import operations_bp
from routes.billing import billing_bp
from routes.pod import pod_bp
from routes.photo import photo_bp

app = Flask(__name__)

app.register_blueprint(dashboard_bp)
app.register_blueprint(operations_bp)
app.register_blueprint(billing_bp)
app.register_blueprint(pod_bp)
app.register_blueprint(photo_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)