# steam_dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#konfiguracja
st.set_page_config(
    page_title='Analiza Gier na Steamie',
    layout='wide'
)

st.title('Steam Games - analiza danych ')

df = pd.read_csv('dataset/steam_clean.csv')


st.sidebar.header('Filtry')

min_year = int(df['release_year'].min())
max_year = int(df['release_year'].max())

year_range = st.sidebar.slider(
    'Zakres lat wydania gry',
    min_year,
    max_year,
    (min_year, max_year)
)

max_price = st.sidebar.slider(
    'Maksymalna cena ($)',
   0,
    int(df['price'].max()),
    60
)

developer_filter = st.sidebar.multiselect(
    'Deweloper',
    options=sorted(df['developer'].unique())
)

publisher_filter = st.sidebar.multiselect(
    'Wydawca',
    options=sorted(df['publisher'].unique())
)

#filtrowane df
filtered_df = df[
    (df['release_year'].between(year_range[0], year_range[1])) &
    (df['price'] <= max_price) 
]

if developer_filter:
    filtered_df = filtered_df[filtered_df['developer'].isin(developer_filter)]

if publisher_filter:
    filtered_df = filtered_df[filtered_df['publisher'].isin(publisher_filter)]

st.write(f'Liczba gier: **{len(filtered_df)}**')

#metryki
col1, col2, col3, col4 = st.columns(4)

col1.metric('Średnia cena ($)', round(filtered_df['price'].mean(), 2))
col2.metric('Procent pozytywnych ocen (%)', round(filtered_df['user_score'].mean(), 2))
col3.metric('Średnia liczba recenzji', int(filtered_df['total_reviews'].mean()))
col4.metric('Średni czas gry (h)', round(filtered_df['average_playtime'].mean() / 60, 2))

#top dewelopery

st.subheader('Top deweloperzy (wg liczby recenzji)')

top_devs = (
    filtered_df
    .groupby('developer', as_index=False)
    .agg(
        games=('name', 'count'),
        avg_score=('user_score', 'mean'),
        reviews=('total_reviews', 'sum')
    )
    .sort_values('reviews', ascending=False)
    .head(10)
)

fig, ax = plt.subplots()
ax.barh(top_devs['developer'], top_devs['reviews'])
ax.set_xlabel('Łączna liczba recenzji')
ax.invert_yaxis()
st.pyplot(fig)

#top wydawcy
st.subheader('Top wydawcy (wg liczby recenzji)')

top_pubs = (
    filtered_df
    .groupby('publisher', as_index=False)
    .agg(
        games=('name', 'count'),
        avg_score=('user_score', 'mean'),
        reviews=('total_reviews', 'sum')
    )
    .sort_values('reviews', ascending=False)
    .head(10)
)

fig, ax = plt.subplots()
ax.barh(top_pubs['publisher'], top_pubs['reviews'])
ax.set_xlabel('Łączna liczba recenzji')
ax.invert_yaxis()
st.pyplot(fig)

#top gry
st.subheader( 'Top 10 gier (wg liczby recenzji)')

top_games = (
    filtered_df
    .sort_values('total_reviews', ascending=False)
    .head(10)[
        [
            'name',
            'developer',
            'publisher',
            'price',
            'total_reviews',
            'user_score',
            'average_playtime'
        ]
    ]
)

top_games['average_playtime'] = (top_games['average_playtime'] / 60).round(2)

st.dataframe(
    top_games.rename(columns={
        'name': 'Gra',
        'developer': 'Deweloper',
        'publisher': 'Wydawca',
        'price': 'Cena ($)',
        'total_reviews': 'Liczba recenzji',
        'user_score': 'Procent pozytywnych recenzji (%)',
        'average_playtime': 'Średni czas gry (h)'
    }),
    width='stretch'
)

st.subheader('Wnioski')

st.markdown('''
- Najwięksi **wydawcy** generują największą liczbę recenzji  
- Duża liczba recenzji ≠ wysoki procent pozytywnych ocen 
- Popularność nie zawsze idzie w parze z ceną
''')
