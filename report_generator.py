def save_final_report(merged_df, output_path):
    columns_to_save = ['student_id', 'name', 'average', 'letter_grade']
    merged_df[columns_to_save].to_csv(output_path, index=False)
