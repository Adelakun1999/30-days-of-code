from email import message
import joblib
import streamlit as st

model=joblib.load('C:/Users/Adekunle/Desktop/python/spam.pkl')

def main():
    st.title('SPAM DETECTION')

    #input variable

    message=st.text_input('MESSAGE')

    #prediction

    if st.button('PREDICT'):
        makepredict=model.predict([message])
        output=makepredict[0]
        st.success('The message is {}'.format(output))

if __name__=='__main__':
    main()