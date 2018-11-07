from flask import Flask, url_for, render_template, request
# import converter as conv
import json
import demographics_fx as dfx

app = Flask(__name__)

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)

    states = dfx.getStates(counties)

    try:
        state = request.args["state-result"]

        return render_template("states.html", opts=states, state=state, display_mode=True)
    except:
        return render_template("states.html", opts=states, state="AL")

@app.route("/stateInfo")
def render_state_info():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)

    state = request.args["state"]

    sdata = dfx.getStateInfo(state, counties)

    stateCounties = dfx.getCounties(state,counties)

    try:
        county = request.args["county-result"]

        return render_template("stateInfo.html", sdata=sdata, state=state, state_name=dfx.getStateName(state), county=county, opts=stateCounties)
    except:
        return render_template("stateInfo.html", sdata=sdata, state=state, state_name=dfx.getStateName(state), county="nil", opts=stateCounties)

@app.route("/countyInfo")
def render_county_info():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)

    countyName = request.args["county-result"]

    county = dfx.getCounty(countyName, counties)

    return render_template("countyInfo.html", cdata=county)


if __name__=="__main__":
    app.run(debug=False, port=54321)
