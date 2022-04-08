import streamlit_book as stb


def st_show():
    stb.set_book_config(
        menu_title="Training Pipeline",
        menu_icon="book",
        options=[
            "Classifying Cats and Dogs",
            "The Training scripts",
            "The Training Pipeline",
        ],
        paths=[
            "pages/dvc_training_pipeline/introducing_the_problem.py",
            "pages/dvc_training_pipeline/introducing_the_scripts.py",
            "pages/dvc_training_pipeline/introducing_the_training_pipeline.py",
        ],
        save_answers=False,
        orientation="vertical",
    )
