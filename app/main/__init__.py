from flask import Blueprint

main = Blueprint('main', __name__)

# Must be at the bottom to avoid circular dependencies
from . import views, errors
