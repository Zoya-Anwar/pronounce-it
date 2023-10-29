class SkillLevel:
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4

def get_skill_level_value(skill_level_text):
    skill_level_text = skill_level_text.lower()  # Convert input to lowercase for case-insensitivity
    if skill_level_text == "beginner":
        return SkillLevel.BEGINNER
    elif skill_level_text == "intermediate":
        return SkillLevel.INTERMEDIATE
    elif skill_level_text == "advanced":
        return SkillLevel.ADVANCED
    else:
        return None  # Handle the case where the input doesn't match any skill level
