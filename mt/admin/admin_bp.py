# Praise Ye The Lord.

# Import libraries
from flask import Blueprint, render_template, request

# Instantiate the Blueprint.
admin_bp = Blueprint("admin",
            __name__, 
            template_folder="templates")

# Create the views.
@admin_bp.route("/admin")
def index():
        return render_template("admin/index.html")

