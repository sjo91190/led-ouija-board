from flask import Blueprint
ouija = Blueprint('ouija', __name__)
from app.ouija_board import views

