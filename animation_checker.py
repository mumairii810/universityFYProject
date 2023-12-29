def check_animation(word):
    word_list = [
        "Hey", "Hello", "Assalam-o-Alaikum", "how", "you", "wrong", "change",
        "yourself", "why", "they", "happy", "what", "your", "age", "stay",
        "safe", "way", "learn", "wash", "hand", "who", "invent", "computer",
        "all", "glitters", "not", "gold", "great", "day", "love", "watch",
        "television", "keep", "distance", "finish", "work", "whole", "world",
        "beautiful", "welcome", "whose", "are", "talk", "with", "me", "good", "better",
        "bye", "engineer", "Before", "come", "walk", "fight", "with"
    ]

    if word in word_list:
        return True
    else:
        return False

entered_word = input("Enter a word: ")
if check_animation(entered_word):
    print("Animation is working!")
else:
    print("Please enter one of the specific words.")