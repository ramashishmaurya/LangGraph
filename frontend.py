import streamlit as st 

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []  

# loading the conversation history
    
for message in st.session_state['message_history']:
    st.chat_message(message['role'])
    st.text(message['content'])


user_input = st.chat_input("Enter the query")

if user_input:
    st.session_state['message_history'].append({'role':'user' , 'content':user_input})
    with st.chat_message('user'): # has to make sense as followed right okay to make sense as followed right bhai how i can do better okay to make sense as i do bhai how thos is beteter ways to make money to make sense how i willable to maek sense a followed right okay to make sense as followed right okat bhao how this is main focus thight to make sense as followd right okya bhaohow this is mafe sure right bha 
        st.text(user_input) 
        
    st.session_state['message_history'].append({'role':'assistant' , 'content': user_input})
    with st.chat_message('assistance'):
        st.text_input(user_input)

