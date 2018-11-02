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
        state = request.args["opt-seler"]
        state_counties = dfx.getCounties(state, counties)
        try:
            county = request.args["opt-seler2"]
            return render_template('states.html', opts = states, ff_num=dfx.total_foreign_born(state,counties), state=state, opts2=state_counties, county=county, ff_num2=dfx.getVeterans(county,state,counties))
        except:
            return render_template('states.html', opts = states, ff_num=dfx.total_foreign_born(state,counties), state=state, opts2=state_counties, county="", ff_num2 = -1)
    except:
        return render_template('states.html', opts = states, ff_num=-1, ff_num2=-1, opts2=[], state="")



if __name__=="__main__":
    app.run(debug=False, port=54321)
