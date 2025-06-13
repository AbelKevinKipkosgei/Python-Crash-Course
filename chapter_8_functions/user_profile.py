def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info


user_profile = build_profile(
    "abel kevin", "kipkosgei", location="nairobi", field="artificial intelligence"
)
user_profile1 = build_profile(
    "sam", "wahinya", location="nairobi", field="data analysis"
)

print(user_profile)
print(user_profile1)
