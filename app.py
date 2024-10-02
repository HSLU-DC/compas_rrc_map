from flask import Flask, render_template, jsonify, url_for, send_file
import os
import json
from flask_frozen import Freezer
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
freezer = Freezer(app)
# Load company data from config files
def load_company_data():
    companies = {}
    companies_dir = os.path.join(os.path.dirname(__file__), 'templates/company')
    
    for company in os.listdir(companies_dir):
        config_file = os.path.join(companies_dir, company, 'config.json')
        if os.path.isfile(config_file):
            with open(config_file) as f:
                company_data = json.load(f)
                companies[str(company)] = company_data
    
    return companies

# URL generator for Flask-Frozen
@freezer.register_generator
def company_info_urls():
    companies = load_company_data()
    if not companies:
        raise ValueError("No companies found. Check your 'load_company_data()' function.")
        
    for company in companies.keys():
        icon_url = url_for('company_icon', name=company)
        icon_bg_url = url_for('company_icon_bg', name=company)
        print(f"Generated URL: {icon_url}")
        print(f"Generated URL: {icon_bg_url}")
        yield "/company/" + company + "/icon.png"
        yield "/company/" + company + "/icon_bg.png"
        yield "/static/css/style.css"
        yield "/static/js/map.js"



@app.route('/')
def index():
    companies = load_company_data()
    return render_template('index.html', companies=companies)

# @app.route('/company/<name>')
# def company_info(name):
#     # Ensure you're looking for .json files
#     company_dir = os.path.join(os.path.dirname(__file__), 'templates/companies', name)
#     config_file = os.path.join(company_dir, 'config.json')  # Expecting .json files
    
#     if os.path.isfile(config_file):
#         with open(config_file) as f:
#             company_data = json.load(f)
#         return jsonify(company_data)
    
#     return "Company not found", 404

@app.route('/company/<name>/icon.png')
def company_icon(name):
    company_dir = os.path.join(os.path.dirname(__file__), 'templates/company', name)
    marker_file = os.path.join(company_dir, 'icon.png')
    if os.path.isfile(marker_file):
        print('found')
        return send_file(marker_file, mimetype='image/png')
    
    return "Marker not found", 404

@app.route('/company/<name>/icon_bg.png')
def company_icon_bg(name):
    company_dir = os.path.join(os.path.dirname(__file__), 'templates/company', name)
    marker_file = os.path.join(company_dir, 'icon_bg.png')
    
    if os.path.isfile(marker_file):
        print('found')
        return send_file(marker_file, mimetype='image/png')
    
    return "Marker not found", 404

if __name__ == '__main__':
    # Run the URL generator
    # app.config['FREEZER_STATIC_IGNORE'] = ['*.png']  # Ignore static files like PNGs
    # app.config['FREEZER_RELATIVE_URLS'] = True
    # app.config['FREEZER_DESTINATION'] = 'build'
    freezer.freeze()
    # app.run(debug=True, port=8080)
    # app.run(debug=True, port=8080)
