# Lecture 03 - Exercise 04

# السؤال الرابع:
# اطلب من المستخدم إدخال اسمه الكامل.
# ثم استخدم split() لتقسيم الاسم إلى كلمات.
# واطبع القائمة الناتجة.

# Question 04:
# Ask the user to enter their full name.
# Use split() to separate the name into words.
# Print the resulting list.

# Solution | الحل:

full_name = input("Enter your full name: ")

name_parts = full_name.split()

print("Name Parts:", name_parts)
