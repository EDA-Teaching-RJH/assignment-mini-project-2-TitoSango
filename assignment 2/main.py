from utils import read_students, calculate_average, write_report, grade_summary

def main():
    students = read_students("students.csv")

    print("\nStudent Grades:")
    for s in students:
        print(f"{s.name}: {s.get_grade()}")

    avg = calculate_average(students)
    print(f"\nAverage Mark: {avg:.2f}")

    summary = grade_summary(students)
    print("\nGrade Summary:")
    for grade, count in summary.items():
        print(f"{grade}: {count}")

    write_report(students, "output.txt")
    print("\nReport written to output.txt")


if __name__ == "__main__":
    main()