from quiz import app,db,photos,search
from flask import redirect, render_template, url_for, flash, request,current_app,jsonify,session,make_response
import secrets,os
import pdfkit

@app.route('/',methods=['GET'])
def department():
    t = "make mindia websaite"
    return t