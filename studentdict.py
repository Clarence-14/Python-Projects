# A program that stores student names and scores in a dictionary, calculates the average score, and identifies the top student.

def student_dict(students, scores):
    student_scores = dict(zip(students, scores))
    average_score = sum(scores) / len(scores) if scores else 0
    top_student = max(student_scores, key=student_scores.get) if students else None
    
    return student_scores, average_score, top_student

if __name__ == "__main__":
    student_names = input("Enter student names separated by spaces: ").split()
    student_scores_input = input("Enter corresponding scores separated by spaces: ").split()
    
    student_scores = [int(score) for score in student_scores_input]
    
    scores_dict, avg_score, top_student = student_dict(student_names, student_scores)
    
    print(f"Student Scores: {scores_dict}")
    print(f"Average Score: {avg_score}")
    print(f"Top Student: {top_student} with a score of {scores_dict[top_student]}")

    