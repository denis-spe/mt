# Praise Ye The Lord.

# Import libraries.
from flask import Flask
from .admin.admin_bp import admin_bp
from .money_tracker.money_tracker_bp import money_tracker_bp


# Create the flask factory function.
def create_app(test_config=None):

    # Instantiate the Flask instance.
    app = Flask(__name__)

    # Register the blueprints to the app.
    app.register_blueprint(admin_bp)
    app.register_blueprint(money_tracker_bp)
    
    app.run(debug=True)

    # return app
