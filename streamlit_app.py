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


options = st.multiselect(
    '好きな色を選んでください',
    ['赤', '青', '緑', '黄色', '黒', '白']
)
st.write(f'あなたの選んだ色: {", ".join(options)}')

genre = st.radio(
    '好きな音楽ジャンルを選んでください',
    ['ロック', 'ポップ', 'ジャズ', 'クラシック']
)
st.write(f'あなたの好きなジャンルは {genre} です')


name = st.text_input('名前を入力してください')
st.write(f'こんにちは、{name}さん！')


message = st.text_area('メッセージを入力してください')
st.write(f'あなたのメッセージ: {message}')


number = st.number_input('数値を入力してください', value=0)
st.write(f'入力された数値は {number} です')

import datetime

d = st.date_input(
    "日付を選んでください",
    datetime.date(2023, 7, 19))
st.write('選択した日付:', d)


t = st.time_input('時間を選んでください', datetime.time(8, 45))
st.write('選択した時間:', t)


color = st.color_picker('色を選んでください', '#00f900')
st.write('選択した色は', color)

uploaded_file = st.file_uploader("ファイルを選択してください")
if uploaded_file is not None:
    st.write('ファイルがアップロードされました:', uploaded_file.name)

import time

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

import time

with st.spinner('処理中...'):
    time.sleep(5)
st.success('完了!')




import streamlit as st

# フォームのタイトル
st.title("お問い合わせフォーム")

# 問い合わせの種類を選択するセレクトボックス
query_type = st.selectbox(
    "お問い合わせの種類を選択してください",
    ["技術的な問題", "販売に関する問い合わせ", "その他"]
)

# 共通の入力フィールド
name = st.text_input("お名前")
email = st.text_input("メールアドレス")

# 問い合わせの種類に応じて追加の入力フィールドを表示
if query_type == "技術的な問題":
    problem_description = st.text_area("問題の詳細を記入してください")
    screenshot = st.file_uploader("スクリーンショットをアップロード（任意）")

elif query_type == "販売に関する問い合わせ":
    product = st.text_input("製品名")
    purchase_date = st.date_input("購入日")

elif query_type == "その他":
    other_query = st.text_area("お問い合わせ内容を記入してください")

# 送信ボタン
if st.button("送信"):
    if query_type == "技術的な問題":
        st.write("技術的な問題として受け付けました。")
        st.write("お名前:", name)
        st.write("メールアドレス:", email)
        st.write("問題の詳細:", problem_description)
        if screenshot is not None:
            st.write("スクリーンショットがアップロードされました。")
        
    elif query_type == "販売に関する問い合わせ":
        st.write("販売に関する問い合わせとして受け付けました。")
        st.write("お名前:", name)
        st.write("メールアドレス:", email)
        st.write("製品名:", product)
        st.write("購入日:", purchase_date)
        
    elif query_type == "その他":
        st.write("その他のお問い合わせとして受け付けました。")
        st.write("お名前:", name)
        st.write("メールアドレス:", email)
        st.write("お問い合わせ内容:", other_query)

    st.success("お問い合わせありがとうございます。")

