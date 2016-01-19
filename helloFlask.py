from flask import Flask, request,jsonify

import rethinkdb as r
import tabulate


app = Flask(__name__)

@app.route("/")
def hello():
    r.connect().repl()
    results = r.table("authors").filter(r.row["username"]=="xyz").order_by(r.desc("score")).limit(3).run()

    resultsList=[["Name","Score"]]
    for result in results:
        resultsList.append([result['username'],result['score']])



    return str(tabulate.tabulate(resultsList,headers="firstrow"))


@app.route('/json', methods=['POST'])
def json():
		
    data=request.get_json()
    print data
    r.connect().repl()
    try:
        r.db("test").table_create("authors").run()
    except r.ReqlOpFailedError:
        pass

    r.table("authors").insert(data).run()
	
    return jsonify(data)



if __name__ == "__main__":
    #r.connect().repl()
    #r.db("test").table_create("authors").run()
    app.debug = True
    app.run()