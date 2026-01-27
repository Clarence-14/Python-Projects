def merit_system():
    reward_pool = 500
    student_records = {}
    unique_subjects = set()

    print("--- Kenyatta University High School Merit System ---")
    print(f"Starting Global Reward Pool: {reward_pool} points\n")

    while reward_pool > 0:
        name = input("Enter student name (or type 'exit' to finish): ").strip()
        
        if name.lower() == 'exit':
            break

        # Collect subjects and scores
        try:
            subject_input = input("Enter subjects separated by commas (e.g., Math, Physics): ")
            current_subjects = [s.strip() for s in subject_input.split(",") if s.strip()]
            
            # Update our unique subjects set
            unique_subjects.update(current_subjects)

            scores_input = input(f"Enter scores for {name} separated by commas: ")
            scores = [float(s.strip()) for s in scores_input.split(",")]

            if len(scores) == 0:
                print("No scores entered. Skipping student.")
                continue

            # Logic: Calculate Average
            average = sum(scores) / len(scores)
            
            # Logic: Determine Status and Points
            if average > 85:
                status, points = "Elite", 50
            elif 70 <= average <= 85:
                status, points = "Achiever", 20
            else:
                status, points = "Standard", 0

            # Check if pool can afford the reward
            if points > reward_pool:
                print(f"Insufficient pool points! Only {reward_pool} left. Awarding 0.")
                points = 0
                status = "Standard (Pool Empty)"

            # Deduct from pool and save record
            reward_pool -= points
            student_records[name] = {
                "average": round(average, 2),
                "points": points,
                "status": status
            }

            print(f"Processed {name}: {status} ({points} pts). Remaining Pool: {reward_pool}\n")

        except ValueError:
            print("Invalid input! Please ensure scores are numbers.")

    # Final Summary Table
    print("\n")
    print(f"{'Student Name':<15} | {'Average':<10} | {'Status':<15} | {'Points'}")
    print("-"*50)
    
    for name, data in student_records.items():
        print(f"{name:<15} | {data['average']:<10} | {data['status']:<15} | {data['points']}")
    
    print(f"Unique Subjects Covered: {', '.join(unique_subjects)}")
    print(f"Final Global Reward Pool Balance: {reward_pool}")
    

if __name__ == "__main__":
    merit_system()