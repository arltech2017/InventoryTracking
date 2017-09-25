from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "THE FUTURE SIGHT OF SOMETHING"

@app.route("/api", methods=['GET'])
def test():
    return "sucsess!"

@app.route("/api/warehouse", methods=['GET'])
def warehouse():
    return "warehouse"

@app.route("/api/warehouse/bin<int:bin_id>/", methods=['GET'])
def bin(bin_id):
    return str(bin_id) 

@app.route("/api/warehouse/bin<int:bin_id>/<string:sku>", methods=['GET'])
def sku(bin_id, sku):
    return str(bin_id) + ", " + sku
