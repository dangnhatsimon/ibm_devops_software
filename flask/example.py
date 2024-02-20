from flask import Flask, escape, request
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/")
def get_author():
    res = requests.get('https://openlibrary.org/search/authors.JSON?q=Michael Crichton')
    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 404:
        return {"message": "Something went wrong!"}, 404
    else:
        return {"message": "Server error!"}, 500
    
@app.route("/network/<uuid:uuid>")
def uuid(uuid):
    res = requests.get(f"https://anotherapi/getnetwork/{uuid}.JSON")
    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 404:
        return {"message": "Network not found"}, 404
    else:
        return {"message": "Something went wrong!"}, 500
    
@app.route("/")
def search_response():
    query = request.args.get("q")
    
    if not query:
        return {"error_message": "Input parameter missing"}, 422
    # fetch the resource from the database
    resource = fetch_from_database(query)
    
    if resource:
        return {"message": resource}
    else:
        return {"error_massage": "Resource not found"}, 404