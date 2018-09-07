from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "Thisissecret"

@app.route('/')
def index():
    if "totalcoins" not in session:
        session["totalcoins"] = 0

    if "log" not in session:
        session["log"] = []

    loglength = len(session["log"])
    revList = list(reversed(session["log"]))
    return render_template("index.html", totalcoins = session["totalcoins"], log = revList, loglength = loglength)

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form["place"] == "Farm":
        farmMoney = random.randrange(10,21)
        session["totalcoins"] += farmMoney
        myStr = "Found " + str(farmMoney) + " gold at the farm"
        

    if request.form["place"] == "Cave":
        caveMoney = random.randrange(5,11)
        session["totalcoins"] += caveMoney
        myStr = "Found " + str(caveMoney) + " gold at the cave"
       

    if request.form["place"] == "House":
        houseMoney = random.randrange(2,6)
        session["totalcoins"] += houseMoney
        myStr = "Found " + str(houseMoney) + " gold at the House"
       

    if request.form["place"] == "Casino":
        casinoMoney = random.randrange(-50,51)
        session["totalcoins"] += casinoMoney
        if casinoMoney < 0:
            myStr = "Lost " + str(abs(casinoMoney)) + " gold at the Casino"
        else:
            myStr = "Won " + str(casinoMoney) + " gold at the Casino"

    session["log"].append(myStr)

    return redirect('/')

@app.route('/newgame')
def newgame():
    session.clear()
    return redirect('/')


app.run(debug=True)