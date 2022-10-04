import joblib
import streamlit as st

model=joblib.load('C:/Users/Adekunle/Desktop/python/language_detection.pkl')

def main():
    st.title('Language Detector')

    #input variable
    Text=st.text_input('Text')

    #predict

    if st.button('Predict'):
        prediction=model.predict([Text])
        output=prediction[0]

        st.success(f"The language is {output}")

if __name__=='__main__':
    main()