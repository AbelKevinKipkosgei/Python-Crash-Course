# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }

# for name, language in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite language is {language.title()}")

# # Looping through all the keys in a dictionary
# friends = ["sarah", "phil"]
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()} I see you love {language}.")

# if "erin" not in favorite_languages:
#     print(f"Erin, please take our poll!\n")

# # Looping through a dictionary's keys in a particular order
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# # Looping through all the values in a dictionary
# print(f"\nThe following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(f"{language.title()}")

# # Polling
# polling_list = ["jen", "sam", "john", "sheila", "edward"]
# print(f"\n** Polling station **")

# for name in polling_list:
#     if name in favorite_languages:
#         print(f"Thank you for taking the poll, {name.title()}.")
#     elif name not in favorite_languages:
#         print(f"You are invited to take the poll, {name.title()}.")

favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are: ")
    elif len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is: ")
    for language in languages:
        print(f"\t{language.title()}")
