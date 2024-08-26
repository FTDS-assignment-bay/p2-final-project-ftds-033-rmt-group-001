from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import contractions
import re
import string
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

# Tokenization and Stopwords Removal
stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()


# preprocess text
def preprocess_and_clean_text(text):
    text = str(text)

    text = re.sub(r'(DIV>)+', '', text) # remove DIV tags

    text = contractions.fix(text)  # Expand contractions (e.g., "don't" -> "do not")

    # Preprocessing
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\[.*?\]', '', text)  # Remove text in square brackets
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove links
    text = re.sub(r'<.*?>+', '', text)  # Remove HTML tags
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
    text = re.sub(r'\n', '', text)  # Remove newlines
    text = re.sub(r'\w*\d\w*', '', text)  # Remove words containing numbers
    text = text.strip()  # Remove extra whitespace
    text = text.lower()  # Lowercase text
    text = re.sub(r'[^\x00-\x7f]', r'', text)  # Remove non-ASCII characters

    print(text)
    return text


# Tokenization, Stopwords Removal, and Lemmatization
def remove_stopwords_and_lemmatize(text):
    text = word_tokenize(text)
    text = [lemmatizer.lemmatize(word) for word in text if word not in stop_words]
    return ' '.join(text)


# Preprocess and clean text
def preprocess_text(text):
    text = preprocess_and_clean_text(text)
    text = remove_stopwords_and_lemmatize(text)
    return text


# Test the function
tx = "<div style='background-color:'><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV><DIV class=RTE><DIV><DIV><EM><FONT size=3><BR>&nbsp;</DIV><DIV><DIV><DIV><STRONG><FONT color=#333333 size=3><EM>Hello,<BR></EM></FONT></STRONG></DIV><DIV><STRONG><FONT color=#333333 size=3><EM>&nbsp;&nbsp;&nbsp;</EM></FONT></STRONG></DIV><DIV><STRONG><FONT color=#333333 size=3><EM>&nbsp;&nbsp; &nbsp;Do accept my sincere apologies if my mail does not meet your personal ethics. I will introduce myself as Mr.Willford Breeks, a staff in the accounts management section of the Bank Of Africa here in&nbsp; ouagadougou,Burkina Faso. One of our accounts with holding balance of $18,000,000(Eighteen Million US Dollars) has been dormant and has not been operated for the past four (4) years.<BR></EM></FONT></DIV></STRONG><DIV><STRONG><FONT color=#333333 size=3><EM>&nbsp;&nbsp;</EM></FONT></STRONG></DIV><DIV><FONT size=3><FONT color=#333333><EM><STRONG>&nbsp;&nbsp; </STRONG><STRONG>From my investigations and confirmations, the owner of this account&nbsp;is&nbsp;a foreigner by name Kurt Kahle died in July, 2000 </STRONG><STRONG>and since then nobody has done anything as regards to the claiming of this fund as he died alogside with the next of kin. And he has no other family members who are aware of the existence of this account nor the funds. Visite the because the wife was the next of kin.&nbsp;&nbsp; </STRONG></EM></FONT><STRONG><FONT color=#333333><EM>website:&nbsp;&nbsp;</EM></FONT></STRONG><STRONG><FONT color=#333333><EM>&nbsp;&nbsp;&nbsp;</EM></FONT></STRONG></FONT></DIV><DIV><A><STRONG><FONT color=#333333 size=3><EM>http:/ews.bbc.co.uk/1/hi/world/europe/859479.stm</EM></FONT></STRONG></A><BR><BR><STRONG><FONT color=#333333><EM><FONT size=3>&nbsp;&nbsp;&nbsp; I have secretly&nbsp;decided that I will disclose this matter to any freliable foreigner who will assist&nbsp;in&nbsp;standing&nbsp; as the next of kin&nbsp;to this funds.With accurate informations&nbsp;from me as a worker in the institution,the deceased&nbsp; funds will be released into your account for both of us after due processes have been followed.<BR></FONT></DIV></EM></FONT></STRONG><DIV><STRONG><FONT color=#333333 size=3><EM>&nbsp;&nbsp;&nbsp;</EM></FONT></STRONG></DIV><DIV><STRONG><FONT color=#333333 size=3><EM>&nbsp;&nbsp;&nbsp;This transaction is totally free of risk and troubles as the fund is legitimate and does not originate from drug, money laundry, terrorism or any other illegal act. On receipt of your positive response, I will furnish you with detailed clarification as it relates to this mutual benefit transaction. I look forward to hearing from you as soon as possible if you are interested.</EM></FONT></STRONG></DIV><DIV><STRONG><FONT color=#333333 size=3><EM>&nbsp; </EM></FONT></STRONG></DIV><DIV><STRONG><FONT color=#333333 size=3><EM>&nbsp;&nbsp;&nbsp; A bank account in any part of the world that you will provide will then facilitate the transfer of this money to you as the beneficiaryext of kin. The money will be paid into your account for both of us to share in the ratio of 60% for me and 30% for you and 10% for the expence.</EM></FONT></STRONG></DIV><DIV><FONT color=#333333 size=3><EM></EM></FONT>&nbsp;</DIV><DIV><FONT color=#333333 size=3><EM></EM></FONT>&nbsp;</DIV><DIV><STRONG><FONT color=#333333 size=3><EM>Thanks and regards,</EM></FONT></STRONG></DIV><DIV><EM><FONT size=3><STRONG><FONT color=#333333>Mr.Willford Breeks</FONT></STRONG><BR></FONT></EM></DIV></DIV></FONT></EM></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></DIV></div><br clear=all><hr>MSN Messenger  <a href=""http://g.msn.com/8HMBFR/2734??PS=47575"" target=""_top"">: appels gratuits de PC � PC partout dans le monde !</a> </html>"
print(preprocess_text(tx))
print(preprocess_text("Pretoria (FCT),=20South Africa.=20                    =20 "))
print(preprocess_text("HELP IN THE CONTEXT BELOW=2EI"))
print(preprocess_text("DIV><DIV><DIV><DIV><DIV><DIV><DIV> yes"))
# output: 'like'
# output: 'pretoria fct south africa'
# output: 'help context'
# output: 'yes'