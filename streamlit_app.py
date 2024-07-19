import streamlit as st

st.title("🎈 こんにちは！ようこそ！")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

age = st.slider('年齢を選択してください', 0, 100, 25)
st.write(f'あなたの年齢は {age} 歳です')
