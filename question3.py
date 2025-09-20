text = input("Enter a string: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():  # ignore spaces and special characters
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")