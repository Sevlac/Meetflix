import streamlit as st
import psutil

st.set_page_config(
    page_title="Recommandation de Film",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Définir les pages pour la navigation
pages = [
    st.Page("project.py", title="Le projet", icon="🔥"),
    st.Page("team.py", title="L'équipe", icon="🤹‍♀️"),
    st.Page("analyse.py", title="Analyse", icon="📊"),
    st.Page("conclusion.py", title="Conclusion", icon="🏁"),
    st.Page("intro.py", title="Intro", icon="🎭"),
    st.Page("reco.py", title="Recommandation", icon="🏠"),
    st.Page("search_movies.py", title="Rechercher", icon="🎬"),
    st.Page("movie.py", title="Les films", icon="🎬"),
    st.Page("actor.py", title="Les acteurs", icon="🎭"),
]

# Activer la navigation
pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()

st.sidebar.markdown("---")
st.sidebar.write(f"🔍 RAM utilisée : {psutil.Process().memory_info().rss / 1e6:.2f} Mo")
