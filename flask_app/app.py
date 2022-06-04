from flask import Flask,render_template,request,jsonify,redirect,url_for
import pickle
from flask_cors import cross_origin

app = Flask(__name__)

@cross_origin()
@app.route('/')
@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        if request.method == 'POST':

            airline = request.form['airline']
            source = request.form['source']
            dest = request.form['dest']
            stops = request.form['stops']
            date = request.form['date']

            #print(request.form)
            #print(airline,source,dest,stops,date)
            data = preprocessing(airline, stops, source, dest, date)
            #print(data)
            #print(len(data[0]))
            predict = round(price_predict(data)[0],2)
            #print(predict)
            return render_template('home.html',result=predict)
    except Exception as e:
        print("Error: ",e)
        return redirect(url_for('home'))


@app.route('/api',methods=['POST'])
def api():
    try:
        airline = request.json['airline']
        source = request.json['source']
        dest = request.json['dest']
        stops = request.json['stops']
        date = request.json['date']

        # print(request.form)
        # print(airline,source,dest,stops,date)
        data = preprocessing(airline, stops, source, dest, date)
        # print(data)
        # print(len(data[0]))
        predict = round(price_predict(data)[0], 2)
        # print(predict)
        return jsonify(Price=predict)
    except Exception as e:
        print(e)
        return jsonify(message="Value Error")



def preprocessing(airline,stops,source,dest,date):
    if stops == 'Non Stop':
        stops = 0
    else:
        stops = int(stops)
        if stops < 0 or stops > 4:
            return [[]]
    s_chennai = 0
    s_delhi = 0
    s_kolkata = 0
    s_mumbai = 0
    if source == 'Chennai':
        s_chennai = 1
    elif source == 'Delhi':
        s_delhi = 1
    elif source == 'Kolkata':
        s_kolkata = 1
    elif source == "Mumbai":
        s_mumbai = 1

    d_cochin = 0
    d_newdelhi = 0
    d_delhi = 0
    d_kolkata = 0
    d_hyderabad = 0

    if dest == 'Cochin':
        d_cochin = 1
    elif dest == 'New Delhi':
        d_newdelhi = 1
    elif dest == 'Kolkata':
        d_kolkata = 1
    elif dest == 'Hyderabad':
        d_hyderabad = 1
    elif dest == 'Delhi':
        d_delhi = 1
    indigo = 0
    airindia = 0
    jet = 0
    spice = 0
    goair = 0
    jetbuss = 0
    mult_carr = 0
    mult_carr_prem_eco = 0
    truject = 0
    vistara = 0
    vistara_prem_eco = 0

    if airline == 'Air India':
        airindia = 1
    elif airline == 'IndiGo':
        indigo = 1
    elif airline == 'Jet Airways':
        jet = 1
    elif airline == 'Jet Airways Business':
        jetbuss = 1
    elif airline == 'Multiple carriers':
        mult_carr = 1
    elif airline == 'Multiple carriers Premium economy':
        mult_carr_prem_eco = 1
    elif airline == 'SpiceJet':
        spice = 1
    elif airline == 'Trujet':
        truject = 1
    elif airline == 'Vistara':
        vistara = 1
    elif airline == 'Vistara Premium economy':
        vistara_prem_eco = 1
    elif airline == 'GoAir':
        goair = 1
    month = int(date.split('-')[1])
    day = int(date.split('-')[-1])
    data = [[stops, day, month, airindia, goair, indigo, jet, jetbuss, mult_carr, mult_carr_prem_eco, spice, truject,
             vistara, vistara_prem_eco, d_cochin, d_delhi, d_hyderabad, d_kolkata, d_newdelhi, s_chennai, s_delhi,
             s_kolkata, s_mumbai]]
    return data


def price_predict(data):
    model = pickle.load(open('rf_model.pickle','rb'))
    price = model.predict(data)
    return price

if __name__ == "__main__":

    app.run(debug=True)