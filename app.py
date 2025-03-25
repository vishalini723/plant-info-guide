# from flask import Flask, render_template, jsonify, request
# import json

# app = Flask(__name__)

# # Load plant data
# with open("plants.json", "r") as file:
#     plants = json.load(file)

# # Home route
# @app.route('/')
# def home():
#     return render_template('index.html', plants=plants)

# # API route to get plant details
# @app.route('/get_details', methods=['POST'])
# def get_details():
#     plant_name = request.json.get("plant")
#     plant_data = plants.get(plant_name, {})
#     return jsonify(plant_data)

# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load plant data
with open("plants.json", "r") as file:
    plants = json.load(file)

@app.route('/')
def home():
    return render_template('index.html', plants=list(plants.keys()))

@app.route('/get_details', methods=['POST'])
def get_details():
    data = request.get_json()
    selected_plant = data.get('plant')
    plant_data = plants.get(selected_plant, {})

    if not plant_data:
        return jsonify({"error": "Plant not found!"})

    return jsonify({
        "category": plant_data.get('category', 'Unknown'),
        "benefits": plant_data.get('benefits', []),
        "precautions": plant_data.get('precautions', ["None"]),
        "image": f"/static/images/{plant_data.get('image', 'default.png')}"
    })

if __name__ == "__main__":
    app.run(debug=True)
