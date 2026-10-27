# Lecture 03 - Exercise 03

# السؤال الثالث:
# اطلب من المستخدم إدخال اسمه مع مسافات زائدة.
# احذف المسافات من البداية والنهاية.
# ثم اطبع الاسم بعد التنظيف وعدد حروفه.

# Question 03:
# Ask the user to enter their name with extra spaces.
# Remove leading and trailing spaces.
# Then display the cleaned name and its length.

# Solution | الحل:

name = input("Enter your name: ")

clean_name = name.strip()

print("Clean Name:", clean_name)
print("Length:", len(clean_name))
