import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="Problem Set 2",
        menu_icon="lightbulb",
        options=[
            "Interactive Plot",
        ],
        paths=[
            "pages/ps2/interactive_plot.py",
        ],
        #icons=["person"],
        save_answers=False,
        orientation="vertical",
    )
