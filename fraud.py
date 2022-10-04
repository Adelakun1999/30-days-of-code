import joblib
import streamlit as st

model=joblib.load('C:/Users/Adekunle/Desktop/python/rf_model.pkl')

def main():
    st.title('Payment Fraud')

    #input variable
    accountAgeDays=st.text_input('accountAgeDays')
    numitems=st.text_input('numitems')
    localTime=st.text_input('localTime')
    paymentMethodAgeDays=st.text_input('paymentMethodAgeDays')
    paymentMethod_creditcard=st.text_input('paymentMethod_creditcard')
    paymentMethod_paypal=st.text_input('paymentMethod_paypal')
    paymentMethod_storecredit=st.text_input('paymentMethod_storecredit')

    #prediction
    if st.button('prediction outcome'):
        makeprediction=model.predict([[accountAgeDays,numitems,localTime,paymentMethodAgeDays,
        paymentMethod_creditcard,paymentMethod_paypal,paymentMethod_storecredit]])
        output=makeprediction[0]

        st.success(f"The payment transaction is {output}")
if __name__=='__main__':
    main()
