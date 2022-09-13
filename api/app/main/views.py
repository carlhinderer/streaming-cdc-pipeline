from . import main


# For Docker health check
@main.route('/')
def index():
    return 'OK'
