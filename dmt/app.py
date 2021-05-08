from flask import Flask, render_template
from dmt.match import start_match
from base.structures.data import MappingFeature


app = Flask(__name__)

@app.route('/')
def index():
    mappingfeatures = MappingFeature()
    mappingfeatures.join_features = {'product_title': 1}
    mappingfeatures.features_left = ['product_title']
    mappingfeatures.features_right = ['product_title']
    matcher = start_match(mappingfeatures)
    return render_template('index.html', matcher=matcher)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/themes')
def themes():
    return render_template('themes.html')

# @app.route('/match', methods=['POST'])
# def match():

if __name__ == '__main__':
   app.run(debug=True)