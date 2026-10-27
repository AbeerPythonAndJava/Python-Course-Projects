# Lecture 03 - Exercise 06

# السؤال السادس:
# اكتب برنامجًا يطلب من الطالب إدخال اسمه الكامل.
# ثم ينفذ العمليات التالية:
#
# 1. حذف المسافات الزائدة من البداية والنهاية.
# 2. تحويل الاسم إلى حروف كبيرة.
# 3. تحويل الاسم إلى حروف صغيرة.
# 4. حساب طول الاسم بعد التنظيف.
# 5. تقسيم الاسم إلى كلمات.
#
# اطبع جميع النتائج.

# Question 06:
# Write a program that asks a student
# to enter their full name.
#
# 1. Remove leading and trailing spaces.
# 2. Convert the name to uppercase.
# 3. Convert the name to lowercase.
# 4. Calculate the cleaned name's length.
# 5. Split the name into words.
#
# Display all results.

# Solution | الحل:

full_name = input("Enter your full name: ")

clean_name = full_name.strip()

print("Clean Name:", clean_name)
print("Uppercase:", clean_name.upper())
print("Lowercase:", clean_name.lower())
print("Length:", len(clean_name))
print("Name Parts:", clean_name.split())
