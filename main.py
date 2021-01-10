from flask import Flask, session, request, jsonify
app = Flask(__name__)

heater_on = False


@app.route('/')
def hello_world():
    return "Hi, this is Dave's Workshop"

@app.route('/heater', methods=["GET", "POST"])
def heater():
  global heater_on
  if request.method == "POST":
    heater_on = not heater_on
  return jsonify({"heater": heater_on})
    

if __name__ == "__main__":
  app.run(host='0.0.0.0', port= 8090)
