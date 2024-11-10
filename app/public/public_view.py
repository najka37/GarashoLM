from app import app
from flask import Flask, render_template, request, jsonify

@app.route('/')
def index():
    return render_template('public/index.html')
