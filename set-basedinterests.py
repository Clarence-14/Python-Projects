# A program that takes two people’s interests (as space-separated strings) and finds common and unique interests using sets.

def set_based_interests(interests1, interests2):
    set1 = set(interests1.split())
    set2 = set(interests2.split())
    
    common_interests = set1.intersection(set2)
    unique_to_person1 = set1.difference(set2)
    unique_to_person2 = set2.difference(set1)
    
    return common_interests, unique_to_person1, unique_to_person2

if __name__ == "__main__":
    person1_interests = input("Enter interests for person 1 (space-separated): ")
    person2_interests = input("Enter interests for person 2 (space-separated): ")
    
    common, unique1, unique2 = set_based_interests(person1_interests, person2_interests)
    
    print(f"Common Interests: {common}")
    print(f"Unique to Person 1: {unique1}")
    print(f"Unique to Person 2: {unique2}")

    