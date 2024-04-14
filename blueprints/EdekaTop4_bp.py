import os
from flask import Blueprint, send_from_directory, request

edeka_angebot_bp = Blueprint("EdekaAngebot", __name__)

@edeka_angebot_bp.route("/EdekaAngebot", methods = ['GET'])
def get_EdekaAngebot(): 
    try:
        # Path to the edekaTop4.json file
        json_file_path = './AngebotDE/edekaTop4.json'  # Update this with the correct relative path

        # Check if the file exists
        if os.path.exists(json_file_path):
            # Serve the file as JSON
            return send_from_directory(os.path.dirname(json_file_path), 'edekaTop4.json', as_attachment=True)
        else:
            return "File not found", 404
    except Exception as e:
        # Log the error
        print(f"Error serving JSON file: {e}")

        # Return a 500 Internal Server Error response
        return "Internal Server Error", 500