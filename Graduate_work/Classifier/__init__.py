from flask import Blueprint

Classifier = Blueprint('Classifier', __name__)

from . import *
