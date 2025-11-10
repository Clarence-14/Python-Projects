# A program that counts the frequency of each word in a user-provided sentence using a dictionary.

def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    
    for word in words:
        word = word.lower()  # Normalize to lowercase
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

if __name__ == "__main__":
    user_sentence = input("Enter a sentence: ")
    freq_dict = word_frequency(user_sentence)
    
    print("Word Frequency:")
    for word, count in freq_dict.items():
        print(f"{word}: {count}")