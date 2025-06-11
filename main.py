import os
from src.data_loader import load_data, clean_data
from src.grade_calculator import compute_final_grades
from src.visualizer import plot_grade_distribution
from src.report_generator import save_final_report

def main():
    # Ensure folders exist
    os.makedirs("reports", exist_ok=True)
    os.makedirs("visuals", exist_ok=True)

    roster_path = "data/student_roster.csv"
    grades_path = "data/grades.csv"
    report_path = "reports/final_grades_report.csv"
    plot_path = "visuals/grade_distribution.png"

    roster_df, grades_df = load_data(roster_path, grades_path)
    roster_df, grades_df = clean_data(roster_df, grades_df)

    merged_df = roster_df.merge(grades_df, on="student_id")
    merged_df = compute_final_grades(merged_df)

    plot_grade_distribution(merged_df, plot_path)
    save_final_report(merged_df, report_path)
    print("Gradebook processing complete.")

if __name__ == "__main__":
    main()
