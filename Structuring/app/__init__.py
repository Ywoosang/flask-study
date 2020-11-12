from flask import Flask

app = Flask(__name__)

from app import views  #view 를 다른 파일로 분리 
from app import admin_views
