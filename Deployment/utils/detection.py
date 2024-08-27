import streamlit as st
import tensorflow as tf
from utils.cleaningData import preprocess_text
import pandas as pd

def run():
    #function main program 
    st.title("Fraud Email Detection")
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1.5, 1, 1.5, 1, 1.5, 1, 1.5])
    with col1: 
        st.image('images/thief.png', use_column_width=True)
    with col2:
        st.write(' ')
    with col3:
        st.image('images/mail.png', use_column_width=True)
    with col4:
        st.write(' ')
    with col5: 
        st.image('images/search.png', use_column_width=True)
    with col6:
        st.write(' ')
    with col7:
        st.image('images/fine.png', use_column_width=True)

    model = tf.keras.models.load_model('lstm_bidirectional')
    data = st.text_input('Must Be Containt English Language', value= '')
    data = pd.Series(data)

    #prep data
    data_clean = data.apply(preprocess_text)

    if st.button('predict'):
        if data_clean.iloc[0].strip() == '':  # Check if the input is empty after preprocessing
            st.write('Input your text only in english')
        else:
            pred = model.predict(data_clean)
            pred_cls = (pred > 0.5).astype(int)
            if pred_cls == 0:
                st.write('Not Fraud')
            else:
                st.write('Fraud')

# Run the app
if __name__ == '__main__':
    run()