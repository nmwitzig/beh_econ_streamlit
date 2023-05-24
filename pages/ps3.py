import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="Problem Set 3",
        menu_icon="lightbulb",
        options=[
            "2-player Fehr Schmidt",
        ],
        paths=[
            "pages/ps3/fehr_schmidt.py",
        ],
        #icons=["person"],
        save_answers=False,
        orientation="vertical",
    )
