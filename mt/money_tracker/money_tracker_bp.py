# Praise Ye The Lord

# Import libraries
from flask import render_template, Blueprint, request

# Instantiate the Blueprint
money_tracker_bp = Blueprint("money_tracker", __name__, template_folder="templates")

# Create the views
@money_tracker_bp.route("/")
def home():
    return render_template("money_tracker/index.html")
