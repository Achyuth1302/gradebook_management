import pandas as pd

def load_data(roster_path, grades_path):
    roster_df = pd.read_csv(roster_path)
    grades_df = pd.read_csv(grades_path)
    return roster_df, grades_df

def clean_data(roster_df, grades_df):
    roster_df.dropna(subset=['student_id'], inplace=True)
    grades_df.fillna(0, inplace=True)  # or another imputation strategy
    return roster_df, grades_df
