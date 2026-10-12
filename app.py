import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="CineMood - 무드별 영화 추천 앱",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    # Hide standard streamlit elements for clean fullscreen app experience
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container { padding: 0 !important; }
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Resolve path to htmls/index.html in the GitHub repository
    html_file_path = os.path.join("htmls", "index.html")

    if os.path.exists(html_file_path):
        try:
            with open(html_file_path, "r", encoding="utf-8") as f:
                html_content = f.read()
            
            components.html(html_content, height=880, scrolling=True)
        except Exception as e:
            st.error(f"HTML 파일을 읽는 중 오류가 발생했습니다: {e}")
    else:
        st.error(f"'{html_file_path}' 경로에서 index.html 파일을 찾을 수 없습니다. GitHub 저장소 구조를 확인해주세요.")

if __name__ == "__main__":
    main()
