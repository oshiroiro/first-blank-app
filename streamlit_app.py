import streamlit as st

st.title("🎈 こんにちは！ようこそ！")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

age = st.slider('年齢を選択してください', 0, 100, 25)
st.write(f'あなたの年齢は {age} 歳です')

option = st.selectbox(
    '好きなフルーツを選んでください',
    ['リンゴ', 'バナナ', 'オレンジ']
)
st.write(f'あなたの好きなフルーツは {option} です')


if st.checkbox('表示/非表示を切り替える'):
    st.write('チェックボックスがオンになっています')
else:
    st.write('チェックボックスがオフになっています')
    
import pandas as pd
import altair as alt

# サンプルデータの作成
data = pd.DataFrame({
    'カテゴリー': ['A', 'B', 'C', 'D'],
    '値': [10, 20, 30, 40]
})

# Altairを使ってグラフを作成
chart = alt.Chart(data).mark_bar().encode(
    x='カテゴリー',
    y='値'
)

# グラフを表示
st.altair_chart(chart, use_container_width=True)
