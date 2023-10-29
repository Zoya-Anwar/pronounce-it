from pymongo.mongo_client import MongoClient
from levels_enum import get_skill_level_value
uri = "mongodb+srv://ddos:Xa8HEaFGXvn62DhT@cluster0.podbcvn.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Access the database
db = client["phoneme_db"]

# Create or access the "users" collection
users_collection = db["users"]


# Function to create a new user
def create_user(username, level):
    user_data = {
        "username": username,
        "level": level,
        "phonemes": [],
    }
    result = users_collection.insert_one(user_data)
    if result.inserted_id:
        print(f"User '{username}' created successfully.")
    else:
        print("Failed to create user.")


# Function to get the user level
def get_user_level(username):
    user = users_collection.find_one({"username": username})
    if user:
        return user["level"]
    else:
        return None

def get_user_level_value(username):
    level = get_user_level(username)
    return get_skill_level_value(level)

def len_words_for_phoneme(username, phoneme):
    user = users_collection.find_one({"username": username})
    if user:
        phoneme_data = next((p for p in user["phonemes"] if p["phoneme"] == phoneme), None)
        if phoneme_data:
            return len(phoneme_data["right_words"]) + len(phoneme_data["wrong_words"])
        else:
            return 0
    else:
        return -1


# Function to retrieve the top 10 lowest phoneme scores and their associated data for a specific user
def get_top_10_lowest_phoneme(username):
    user = users_collection.find_one({"username": username})
    if user:
        # Sort the phonemes by score in ascending order
        sorted_phonemes = sorted(user["phonemes"], key=lambda x: x["score"])
        # Get the top 10 lowest phoneme scores
        lowest_scores = sorted_phonemes[:10]
        result = []
        for phoneme_data in lowest_scores:
            phoneme = phoneme_data["phoneme"]
            wrong_words = phoneme_data["wrong_words"]
            score = phoneme_data["score"]
            result.append({"phoneme": phoneme, "score": score, "wrong_words": wrong_words})
        return result
    else:
        return None


def get_average_score_for_phoneme_user(username, phoneme):
    user = users_collection.find_one({"username": username})
    if user:
        phoneme_data = next((p for p in user["phonemes"] if p["phoneme"] == phoneme), None)
        if phoneme_data:
            return phoneme_data["score"]
        else:
            return None
    else:
        return None


# Function to get the average score for a specific phoneme across all users
def get_average_score_for_phoneme_across_users(phoneme):
    total_score = 0
    total_users = 0

    # Iterate through all users
    for user in users_collection.find():
        phoneme_data = next((p for p in user["phonemes"] if p["phoneme"] == phoneme), None)
        if phoneme_data:
            total_score += phoneme_data["score"]
            total_users += 1

    if total_users > 0:
        average_score = total_score / total_users
        return average_score
    else:
        return None


# Function to add a phoneme test result for a user
def add_phoneme_test_result(username, phoneme, score, word):
    user = users_collection.find_one({"username": username})
    is_correct = score >= get_skill_level_value(get_user_level(username))
    if user:
        # Check if the phoneme already exists for the user
        phoneme_data = next((p for p in user["phonemes"] if p["phoneme"] == phoneme), None)
        if phoneme_data:
            words_size = len_words_for_phoneme(username, phoneme)
            phoneme_data["score"] = (phoneme_data["score"] * words_size + score) / (words_size + 1)
            if score == is_correct:
                phoneme_data["right_words"].append(word)
            else:
                phoneme_data["wrong_words"].append(word)
        else:
            new_phoneme = {
                "phoneme": phoneme,
                "score": score,
                "right_words": [word] if is_correct else [],
                "wrong_words": [word] if not is_correct else [],
            }
            user["phonemes"].append(new_phoneme)
        users_collection.update_one({"_id": user["_id"]}, {"$set": {"phonemes": user["phonemes"]}})
        print(f"Phoneme test result added for user '{username}'.")
    else:
        print(f"User '{username}' not found.")

if __name__ == "__main__":
    username = "Eva"  # Replace with the user's username
    phoneme = "h"  # Replace with the desired phoneme
    level = "begInner"
    score = 1  # Replace with the desired score
    print(get_top_10_lowest_phoneme(username))