'''
@author: tahacolak
'''

import random, string

# 1. Choose 5 letters and assign 3 replacement characters to each

letter_replacements = {}
all_replacements = set()

for a in range(0, 5, 1):
    while True:
        # That is a good point, string method's ascii attribute is being used
        letter = random.choice(string.ascii_lowercase)

        if letter not in letter_replacements:
            letter_replacements[letter] = []  # Doğru girintiyle oluşturuldu
            break  # Harf eklendikten sonra döngüden çık

    for a in range(3):  # Seçilen harf için 3 özel karakter ata
        while True:
            # Special characters and selection with .choice() method
            replacement = random.choice('!@#$%^&*()_+-=[]{}|;:,.<>?/')
            if replacement not in all_replacements:
                letter_replacements[letter].append(replacement)
                all_replacements.add(replacement)
                break  # Karakter eklenirse döngüden çık

# 2. Generate random passwords and apply replacements
passwords = []
for a in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

processed_passwords = []
for password in passwords:
    processed = list(password)
    for i, char in enumerate(processed):
        if char in letter_replacements:
            processed[i] = random.choice(letter_replacements[char])  # Harf değiştirme
    processed_passwords.append(''.join(processed))

# 3. Categorize passwords as "strong" or "weak"
categorized_passwords = {"STRONG PASSWORDS": [], "WEAK PASSWORDS": []}

for original, processed in zip(passwords, processed_passwords):
    replaced_count = sum(1 for orig, proc in zip(original, processed) if orig != proc)

    if replaced_count > 4:
        categorized_passwords["STRONG PASSWORDS"].append(processed)
    else:
        categorized_passwords["WEAK PASSWORDS"].append(processed)

# 4. Print out the categorized passwords
print("Generated Passwords:\t")
for category, pwd_list in categorized_passwords.items():
    print(f"{category}:")
    for pwd in pwd_list:
        print(pwd)

print("\nLetter replacements:\t")
for letter, replacements in letter_replacements.items():
    print(f"{letter}: {', '.join(replacements)}")
