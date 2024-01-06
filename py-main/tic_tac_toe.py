from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for,
    session
)

bp = Blueprint('tic-tac-toe', __name__, url_prefix='/ttt')

@bp.route('/')
def init():
    return render_template('tic-tac-toe/index.html')
