import os
from app import create_app, db

# Add this when models are created
# from app.models import User, Role 


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


# Add this when models are created
# @app.shell_context_processor
# def make_shell_context():
    # return dict(db=db, User=User, Role=Role)