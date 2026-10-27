# Lecture 03 - Exercise 05

# السؤال الخامس:
# اطلب من المستخدم إدخال جملة.
# ثم اطلب منه إدخال كلمة يريد استبدالها
# وكلمة جديدة تحل محلها.
# اطبع الجملة بعد التعديل.

# Question 05:
# Ask the user to enter a sentence.
# Then ask for a word to replace
# and a new word to use instead.
# Display the updated sentence.

# Solution | الحل:

sentence = input("Enter a sentence: ")

old_word = input("Word to replace: ")
new_word = input("New word: ")

updated_sentence = sentence.replace(old_word, new_word)

print("Updated Sentence:", updated_sentence)
