from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from blueprints.EdekaTop4_bp import edeka_angebot_bp




app = Flask(__name__)
CORS(app, resources={

})


app.register_blueprint(edeka_angebot_bp)



if __name__ == "__main__":
    app.run(debug = True)