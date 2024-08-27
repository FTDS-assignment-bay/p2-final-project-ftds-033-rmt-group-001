import utils.eda
import streamlit as st
import utils.detection

# Side bar
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Fraud Detection'])

st.sidebar.markdown('# PROTEGO')
st.sidebar.image('images/PROTEGO.png')
st.sidebar.write('')
        
# Introduction
st.sidebar.write('''This is a fraud email detection program. The program is used to detect whether an email is fraudulent or not.''')
# Tools
st.sidebar.write('''### Tools:
`Python`: For backend operations and model computations.    `Streamlit`: For creating this interactive web application.''')

def show_home():

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Dataset", "Objective", "Model", "Credit"])

    with tab1:
        # Home Page
            
        st.title('Welcome to PROTEGO')

        st.write("The function of an email fraud detection model is to automatically identify and filter suspicious or potentially harmful emails that aim to commit fraud or other malicious activities. Here are some of the key functions of an email fraud detection model:")
        st.write(" - Detecting Fraud - Reducing Fraud Risk - Managing Spam Emails ")  

        # Dataset section
                
       # Target Audience
        col1, col2 = st.columns([0.5, 2])
        with col1:
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.image('images/benefit.png', use_column_width=True)
        with col2:
            st.markdown("### Who's get benefit?")
            st.markdown(" - **Users**: The purpose of this model is to detect **fraud emails**, which will help prevent users from trusting emails that are actually fraudulent. By using this model, users can more easily distinguish between legitimate emails and potentially harmful ones, there by reducing the risk of fraud and protecting their personal information and digital security.")
            st.markdown("- **Scientist**: Data scientists benefit from the opportunity to develop and test new fraud detection algorithms, contributing to enhanced cybersecurity. With this model, they can explore machine learning and natural language processing (NLP) techniques, gain deep insights into fraud patterns, and drive innovation in developing more advanced and effective security solutions. ")
       
        st.markdown('---')
        
    with tab2:
        # Dataset section
        col1, col2 = st.columns([0.4, 2])
        with col1:
            st.write(' ')
            st.write(' ')
            st.image('images/csv.png', use_column_width=True)
        with col2:
            st.markdown('## Dataset')
            st.markdown('''The dataset is obtained from a credible source [aclwiki](https://aclweb.org/aclwiki/CLAIR_collection_of_fraud_email_(Repository)).''')
            st.markdown('''This dataset has meta data which contains a collection of emails from Nigeria that already have labels for fraud or normal conditions ''')
       
        st.write(''' ## **Key Feature**:''')
        st.write('''
        - **Email Content**: The text of the emails, which includes the subject and body. This is the primary source for text analysis and feature extraction.  
        - **Label**: A binary classification label indicating whether an email is fraudulent (1) or non-fraudulent (0). This serves as the target variable for machine learning models.  
        - **Data Size**: The dataset includes a significant number of emails, providing a robust sample size for training and evaluating machine learning models.  
        - **Data Format**: The data is provided in a tabular format, typically a CSV file, where each row represents an email and each column represents a feature (e.g., email content, label).  
        ''')

        st.markdown('---')
       

    with tab3:
        # Objective section
        st.write('')
        st.write('')
        st.write('')
        col1, col2 = st.columns([0.5, 2])
        with col1:
            st.image('images/objective.png', use_column_width=True)
        with col2:
            st.markdown('### Objective')
            st.markdown('''The main aim of Protego (The fraudulent email detector) is to detect phishing or fraudulent email. Moreover, Protego will analyze the content of email  based on user input and classify  its as fraud or not with accuracy as the metric. ''')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
            
        # Problem Statement section
        col3, col4 = st.columns([0.5, 2])
        with col3:
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.image('images/problem2.png', use_column_width=True)
        with col4:
            st.markdown('### Problem Statement')    
            st.markdown('''Based on [article](https://www.stationx.net/phishing-statistics/#:~:text=Phishing%20is%20the%20single%20most,trillion%20phishing%20emails%20per%20year), estimated 3.4 billion emails are sent by cyber criminals per day. Around 36% of all data breaches involve phishing. This is to say, an individual has risk to follow or click any dangerous sources. With in this data, Protege show up to the stage to filter whether email is a fraud.''')
            st.markdown('''**Protego** solved the problem by utilizing advanced natural Language Processing (NLP) techniques to quickly and accurately analyze email. By processing and understanding the content of the email, Protego able to determine fradulent email.''')
            
            st.markdown('---')

        # # Tools
        # st.write('''### Tools:
        # `Python`: For backend operations and model computations.    `Streamlit`: For creating this interactive web application.''')
            
    with tab4:
        st.write("In the development of the Fraud Email Detection Application, several stages are applied, including the implementation of the Deep Learning LSTM algorithm, as depicted in the image below.")
        # Dataset section
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("## Flow Chart Model")
            st.image('images/flow.png', use_column_width=True)
        with col2:
            st.write("## LSTM Model")
            st.image('images/lstm.png', use_column_width=True)
        
        st.write("With the information on this model architecture, it is expected to assist scientists in better understanding the model creation process and to aid in the further development of the project.")
                
        st.markdown('---')


    with tab5:
        col1, col2 = st.columns([2, 2])
        with col1:
            st.image('images/team.png', use_column_width=True)
        with col2:
            st.markdown(' ')
              
        st.markdown('### Meet Our Team')
        st.write('''We are a team of three professionals with strong expertise in data: a Data Engineer, Data Scientist, and Data Analyst. Combining our skills, we have developed an innovative fraud email detection program designed to help you protect critical information and safeguard data from the ever-evolving threats of cyber fraud. With a deep understanding of how data functions and how fraud schemes typically operate, we ensure that our solution is not only effective but also easily integrated into dynamic business environments. We are committed to delivering the best, allowing you to focus on growing your business without the worry of lurking fraud threats. ''')
        st.write('''
        - **Ahmad Junjung Sudrajad** [Linkedin](https://www.linkedin.com/in/ahmadjunjungsudrajad/)
        - **Ni Putu Wisma Ekawati** [Linkedin](https://www.linkedin.com/in/wismaeka)
        - **Muhammad Rozzaaq** [Linkedin](https://www.linkedin.com/in/muhammad-rozzaaq/)''')
        
        # st.write(" - Detecting Fraud - Reducing Fraud Risk - Managing Spam Emails ")  
   
if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    utils.eda.run()
elif navigation == 'Fraud Detection':
    utils.detection.run()
    ##aa