"""
QuickVoiceApp - App that clones your voice with AI
Built with AI Trend App Builder
"""

from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(____name____)

@app.route('/')
def home():
    return jsonify({
        'app': 'QuickVoiceApp',
        'description': 'App that clones your voice with AI',
        'status': 'running',
        'built_at': '2026-03-23 09:00:01'
    })

@app.route('/api/trend')
def get_trend():
    return jsonify({
        'topic': 'Voice AI Clone',
        'keywords': ["voice clone","AI voice","speech synthesis"]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
