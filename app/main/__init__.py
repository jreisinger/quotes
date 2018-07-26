"""
`main` directory is a subpackage inside the `app` package. `main` subpackage
containes blueprints.

A blueprint is similar to an application in that it can also define routes
and error handlers. But they are dormant until the blueprint is registered
with an application. Then they become part of the app.
"""

"""
main blueprint creation
"""

from flask import Blueprint

# instantiate an object of class Blueprint(<blueprint-name>, <module-or-package>)
main = Blueprint('main', __name__)

# Must be at the bottom to avoid circular dependencies
from . import views, errors
