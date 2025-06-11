import pandas as pd

def compute_final_grades(merged_df):
    merged_df['average'] = merged_df[['homework', 'quizzes', 'exams']].mean(axis=1)
    merged_df['letter_grade'] = merged_df['average'].apply(assign_letter_grade)
    return merged_df

def assign_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
