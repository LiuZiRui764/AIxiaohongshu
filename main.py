import streamlit as st
from utils import generate_xiaohongshu
st.title("✍ Popular Xiaohongshu AI Writing Assistant")
with st.sidebar:
    api_key = st.text_input("Please input your api key:",type="password")
    no_api_key = st.checkbox("I have no api_key")
    if no_api_key:
        st.write("https://api.aigc369.com/register?aff=87kh")
        st.stop()
Topics = st.text_input("📃 Topics")
submit = st.button("Submit")
if not api_key and submit:
    st.write("🔑 No api keys! Please write down api keys in the blanks")
if not Topics and submit:
    st.write("❗ No Topics! Please write down Topics in the blanks")
if submit and api_key and Topics:
    with st.spinner("🔎 AI is accelerating processing......"):
        theme = generate_xiaohongshu(Topics,api_key)
        with st.expander("💡 The theme of xiaohongshu"):
            for i in range(0,5):
                st.subheader(f"# theme {i+1}")
                st.write(theme.titles[i])
        with st.expander("✏ The content of xiaohongshu"):
                st.write(f"# content")
                st.write(theme.content)

