import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="Problem Set 1",
        menu_icon="lightbulb",
        options=[
            "Generate and Plot Data",
            "More Discount Functions",
            "Interactive Plots",
            "Per-Period Discounting and Discount Rates",
            "Interactive Plots 2",
        ],
        paths=[
            "pages/introduction/gen_data.py",
            "pages/introduction/more_fns.py",
            "pages/introduction/interactive_plots.py",
            "pages/introduction/per_period.py",
            "pages/introduction/interactive_plots2.py",
        ],
        #icons=["person"],
        save_answers=False,
        orientation="vertical",
    )
