import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS


# Main program
def run():
    ##
    st.title("Exploratory Data Analysis")

    # Load the dataset
    dataset_path = "fraud_email_clean_processed.csv"
    df = pd.read_csv(dataset_path)

    # Add image
    st.image("images/graphs.png") 


    #Function to Normal Wordcloud
    def normal_word_cloud(df, title):
        # Filter data for Fraud cases
        Normal_data = df[df['class'] == 0].astype(str)
        # Join all text data for Fraud cases
        normal_text = ' '.join(Normal_data['text'])
        
        # Generate Word Cloud for Fraud data
        wordcloud = WordCloud(
            width=1600,
            height=600,
            max_words=100,
            min_font_size=10,
            background_color='black',
            contour_color='black',
            colormap='plasma',
            repeat=False,
            stopwords=STOPWORDS
        ).generate(normal_text)

        # Plot the Word Cloud
        plt.figure(figsize=(12, 12))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title(title, fontsize=15, weight='bold')
        plt.axis('off')

        # Display Word Cloud using Streamlit
        st.pyplot(plt)
        st.write('''**Insight:** the "Normal" WordCloud highlights dominant words such as "said," "new," "one," and "president," indicating that this dataset is more general and covers social, political, and everyday conversation topics. Much of the discussion revolves around politics and broader societal issues, with words reflecting social interactions, public communication, and statements that commonly appear in normal contexts.''')
        
        
    # Function to Fraud Wordcloud
    def fraud_word_cloud(df, title):
        # Filter data for Fraud cases
        Fraud_data = df[df['class'] == 1].astype(str)
        # Join all text data for Fraud cases
        fraud_text = ' '.join(Fraud_data['text'])
        
        # Generate Word Cloud for Fraud data
        wordcloud = WordCloud(
            width=1600,
            height=600,
            max_words=100,
            min_font_size=10,
            background_color='black',
            contour_color='black',
            colormap='plasma',
            repeat=False,
            stopwords=STOPWORDS
        ).generate(fraud_text)

        # Plot the Word Cloud
        plt.figure(figsize=(12, 12))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title(title, fontsize=15, weight='bold')
        plt.axis('off')

        # Display Word Cloud using Streamlit
        st.pyplot(plt)
        st.write('''**Insight:** In the "Fraud" WordCloud, the prominent words relate to financial transactions, fraudulent communication, and specific scenarios like "united," "state," "security," "company," and "next of kin." This suggests that fraud often involves official-looking transactions and communications designed to deceive victims into handing over money or personal information. These themes are very specific and focused on financial manipulation.''')
        

    # Function to plot course level distribution
    def plot_course_level_distribution(df):
        df['Class Convert'] = df['class'].map({0:'Not Fraud', 1:'Fraud'})
        # Menghitung jumlah setiap kelas
        class_counts = df['Class Convert'].value_counts()

        # Membuat pie chart dengan Matplotlib
        fig, ax = plt.subplots()

        # Definisi explode untuk membuat efek explode pada slice 'Fraud'
        explode = (0.1, 0)  # 0.1 untuk 'Fraud' (explode), 0 untuk 'Not Fraud' (no explode)

        # Membuat pie chart
        ax.pie(class_counts, 
            labels=class_counts.index, 
            autopct='%1.1f%%',  # Menampilkan persentase 
            startangle=90,  # Memulai dari 90 derajat untuk rotasi
            colors=['#ff9999', '#66b3ff'],  # Warna untuk tiap slice
            explode=explode,  # Efek explode pada slice tertentu
            shadow=True)  # Menambahkan bayangan untuk efek visual

        # Menambahkan judul
        plt.title('Distribution of Fraud and Not Fraud Emails')

        # Menampilkan pie chart
        st.pyplot(plt)

    # Display raw data
    if st.checkbox("Show Data"):
        st.dataframe(df)

    # Select analysis
    analysis_type = st.selectbox("Select Analysis", ["Distribution Plots", "Word Cloud"])

    # Interface
    if analysis_type == "Distribution Plots":
        plot_course_level_distribution(df)    
    elif analysis_type == "Word Cloud":    
        
        tab1, tab2, = st.tabs(["Normal Wordcloud", "Fraud WordCloud"])
        with tab1: 
            st.subheader("Normal Word Cloud")
            normal_word_cloud(df, 'Top 100 Word on Normal')
        with tab2: 
            st.subheader("Fraud Word Cloud")
            fraud_word_cloud(df, 'Top 100 Word on Fraud')

     
    
# Run the app
if __name__ == '__main__':
    run()