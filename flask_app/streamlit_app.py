import streamlit as st
import pickle


def price_predict(data):
    model = pickle.load(open('rf_model.pickle','rb'))
    price = model.predict(data)
    return price

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

def main():
    st.title("Airline Price Prediction")
    pass


if __name__ == '__main__':

    main()