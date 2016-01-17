from flask import Flask, request,jsonify

import rethinkdb as r

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/json', methods=['POST'])
def json():
		
	data=request.get_json()
	print data
		
	r.table("authors").insert(jsonify(data)).run(5000)
	
	return jsonify(data)    


if __name__ == "__main__":
    r.connect().repl()
    #r.db("test").table_create("authors").run()
    app.debug = True
    app.run()