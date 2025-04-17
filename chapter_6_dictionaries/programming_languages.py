# Extensions
programming_languages = {
    "jane": ["Python", "JavaScript"],
    "mark": ["C++"],
    "elena": ["Python", "Rust", "Go"],
    "tony": ["Java", "C#", "SQL", "HTML"],
    "lisa": ["R"],
}

for name, languages in programming_languages.items():
    languages_string = ", ".join(language for language in languages)
    print(f"{name.title()} knows: {languages_string}")
