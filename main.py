from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=["GET"])
def home_page():
  return "Sparta-Trainee Management System"


@app.route('/spartan/add', methods = ['POST'])
def add_spartan():
    return



@app.route('/spartan/<spartan_id>', methods = ['GET'])
def get_spartan(spartan_id):
    return


@app.route('/sparta/remove', methods = ["POST"])
def del_spartan(spartan_id):
    return


@app.route('/spartan', methods = ["GET"])
def get_spartans(spartan_id):

    return


if __name__ == "__main__":
  app.run()