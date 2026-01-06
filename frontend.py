import streamlit as st
from backend import get_agent
from langgraph.types import Command

st.set_page_config(
    page_title="Story Generator",
    page_icon="📖"
)

st.markdown("""
    <style>
    /* Main title styling */
    .main-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
        padding: 1rem;
    }
    
    /* Story container */
    .story-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        border-left: 4px solid #4ECDC4;
    }
    
    /* Chat input styling */
    .stChatInput {
        border-radius: 20px;
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        font-weight: bold;
        border: none;
    }
    
    .stButton>button:hover {
        background: linear-gradient(45deg, #4ECDC4, #FF6B6B);
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📖 Story Generator ✨</h1>', unsafe_allow_html=True)

with st.sidebar:
    st.title("🔑 Configuration")
    
    api_key = st.text_input(
        "Groq API Key",
        type="password",  
        help="Get your API key from https://console.groq.com"
    )
    
    if api_key:
        st.success("✅ API Key provided")
    else:
        st.warning("⚠️ Please enter your API key")
    
    st.markdown("---")
    st.caption("Your API key is never stored")

if 'interrupt' not in st.session_state:
    st.session_state['interrupt']= []

if 'story' not in st.session_state:
    st.session_state['story']=[]

if 'input_flag' not in st.session_state:
    st.session_state['input_flag']= True

if 'topic' not in st.session_state:
    st.session_state['topic']=None

if 'end_story' not in st.session_state:
    st.session_state['end_story']= False

if 'agent' not in st.session_state:
    st.session_state['agent'] = None

if not api_key:
    st.info("👈 Please enter your Groq API key in the sidebar to get started")
    st.stop()

if st.session_state['agent'] is None:
    try:
        st.session_state['agent'] = get_agent(api_key)
        st.rerun()
    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.stop()


CONFIG= {'configurable': {'thread_id': 'thread-1'}}

if st.session_state['input_flag']:

    user_input= st.chat_input("Enter Topic")

    if user_input:
        with st.spinner("✨ Generating your story..."):
            st.session_state['input_flag']= False
            st.session_state['topic']= user_input
            initial_state= {'topic':st.session_state['topic'], 'messages':[], 'story':[]}
            response= st.session_state['agent'].invoke(initial_state, config=CONFIG)
            st.session_state['story'].append(response['story'][0])
            st.session_state['interrupt'].append(response['__interrupt__'][0].value['options'])
        st.rerun()

if st.session_state['topic']!= None:
            
            
    with st.chat_message('assistant', avatar="📖"):
        for i in st.session_state['story']:
            st.write(i)
            
    if st.session_state['end_story']:
        st.success("🎬 **The End** - Thank you for experiencing this story!")
                
        if st.button("Start a New Story 🔄"):
            st.session_state['interrupt'] = []
            st.session_state['story'] = []
            st.session_state['input_flag'] = True
            st.session_state['topic'] = None
            st.session_state['story_ended'] = False
            st.rerun()

    if st.session_state['interrupt'] and not st.session_state['end_story']:
        st.markdown("### 🎯 What happens next?")
        option1 = st.checkbox(st.session_state['interrupt'][-1][0])
        option2 = st.checkbox(st.session_state['interrupt'][-1][1])
        option3 = st.checkbox(st.session_state['interrupt'][-1][2])
        option4 = st.checkbox("END STORY")
            
    if not st.session_state['end_story']:
        if option1 or option2 or option3 or option4 :
            with st.spinner("✨ Generating your story..."):
                if option1:
                    response2= st.session_state['agent'].invoke(
                        Command(resume=st.session_state['interrupt'][-1][0]),
                        config=CONFIG
                    )
                elif option2:
                    response2= st.session_state['agent'].invoke(
                        Command(resume=st.session_state['interrupt'][-1][1]),
                        config=CONFIG
                    )
                elif option3:
                    response2= st.session_state['agent'].invoke(
                        Command(resume=st.session_state['interrupt'][-1][2]),
                        config=CONFIG
                    )
                elif option4:
                    response2= st.session_state['agent'].invoke(
                        Command(resume="end"),
                        config=CONFIG
                    )
                    st.session_state['end_story']=True
                    st.session_state['story']= response2['story']
                    st.rerun()
                    
                if not st.session_state['end_story']:
                    st.session_state['story']= response2['story']
                    st.session_state['interrupt'].append(response2['__interrupt__'][0].value['options'])
                    st.rerun()


