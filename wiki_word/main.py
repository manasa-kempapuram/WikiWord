import wikipedia
import random
import timer
import threading

# Function to clean article titles (remove special characters, ensure single word)
def clean_article_title(title):
    """Removes special characters and ensures it's a single word."""
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cleaned_title = "".join(char for char in title if char in allowed_chars)
    return cleaned_title if cleaned_title and " " not in cleaned_title and len(cleaned_title) <= 10 else None


# Function to fetch a valid single-word Wikipedia article
def get_random_article():
    """Fetches a valid single-word Wikipedia article with no special characters."""
    while True:
        try:
            article = wikipedia.random(1)
            clean_title = clean_article_title(article)
            if clean_title:
                return clean_title  # Return valid title
        except Exception:
            return "Error"  # Handle API issues


# Function to check if a word exists on Wikipedia
def check_wikipedia_page(word):
    """Checks if the given word exists as a Wikipedia page."""
    try:
        results = wikipedia.search(word)
        if results:
            print(f"✅ The word '{word}' exists on Wikipedia!")
            return True  # Valid Wikipedia word
    except wikipedia.exceptions.PageError:
        print(f"❌ Sorry, '{word}' does not exist on Wikipedia.")
    return False


# Function to check if a word starts with the last letter of another word
def starts_with_last_letter(previous, current):
    return current.casefold().startswith(previous[-1].casefold())


# Function to check for forbidden letters
def contains_forbidden_letters(word, forbidden_letters):
    return any(letter in word.casefold() for letter in forbidden_letters)


# Timer Function
def time_up():
    print("\n⏰ Time's up!")


# Beginner Level
def beginner_level():
    print("\n🔹 Beginner Level 🔹")
    random_article = get_random_article()

    if random_article == "Error":
        print("⚠️ Error fetching the starting article. Skipping level.")
        return

    print(f"🎲 Starting Article: {random_article}")

    for _ in range(5):  # 5 rounds per level
        timer = threading.Timer(10, time_up)  # Set timer for 10 seconds
        timer.start()

        print("You have 10 seconds to enter something...")  # Message for time limit
        user_input = input(f"Your word (starts with '{random_article[-1]}'): ")

        timer.cancel()

        if starts_with_last_letter(random_article, user_input) and check_wikipedia_page(user_input):
            print("✅ Valid!")
            random_article = user_input  # Update for the next round
        else:
            print("❌ Invalid! Word does not start with the correct letter or is not on Wikipedia.")


# Intermediate Level (Forbidden Letters Challenge)
def intermediate_level():
    print("\n🔹 Intermediate Level: Forbidden Letters Challenge 🔹")

    random_article = get_random_article()
    if random_article == "Error":
        print("⚠️ Error fetching the starting article. Skipping level.")
        return

    print(f"🎲 Starting Article: {random_article}")

    for _ in range(5):  # 5 rounds per level
        last_letter = random_article[-1].lower()

        # Generate forbidden letters, ensuring last_letter is NOT included
        all_letters = list("abcdefghijklmnopqrstuvwxyz")
        all_letters.remove(last_letter)  # Remove last letter to avoid impossible words
        forbidden_letters = random.sample(all_letters, 5)  # Pick 5 forbidden letters

        print(f"🚫 Forbidden Letters: {', '.join(forbidden_letters)}")

        timer = threading.Timer(10, time_up)  # Set timer for 10 seconds
        timer.start()

        print("You have 10 seconds to enter something...")  # Message for time limit
        user_input = input(f"Your word (starts with '{last_letter}' and avoids forbidden letters): ")

        timer.cancel()

        # Validation checks
        if not starts_with_last_letter(random_article, user_input):
            print("❌ Invalid! Word does not start with the correct letter.")
        elif contains_forbidden_letters(user_input, forbidden_letters):
            print(f"❌ Invalid! Word contains one of the forbidden letters: {', '.join(forbidden_letters)}.")
        elif check_wikipedia_page(user_input):
            print("✅ Valid!")
            random_article = user_input  # Update for the next round
        else:
            print("❌ Invalid! The word is not on Wikipedia.")


# Advanced Level (No Repeated Letters)
def advanced_level():
    print("\n🔹 Advanced Level: No Repeated Letters Challenge 🔹")

    # Fetch a valid single-word Wikipedia article with at least 5 characters
    while True:
        random_article = get_random_article()
        if random_article != "Error" and len(random_article) >= 5:
            break

    print(f"🎲 Starting Article: {random_article}")
    used_words = [random_article]  # Track used words

    for _ in range(5):  # 5 rounds per level
        timer = threading.Timer(10, time_up)  # Set timer for 5 seconds
        timer.start()

        print("You have 10 seconds to enter something...")  # Message for time limit
        user_input = input(f"Your word (starts with '{random_article[-1]}' and no repeated letters): ")

        timer.cancel()

        # Validation checks
        if user_input in used_words:
            print("❌ Invalid! Word has already been used.")
        elif not starts_with_last_letter(random_article, user_input):
            print("❌ Invalid! Word does not start with the correct letter.")
        elif len(set(user_input.casefold()) & set(random_article.casefold())) > 1:
            print("❌ Invalid! Word shares too many letters with the previous word.")
        elif check_wikipedia_page(user_input):
            print("✅ Valid!")
            random_article = user_input  # Update for next round
            used_words.append(user_input)
        else:
            print("❌ Invalid! The word is not on Wikipedia.")


# Main Function
def main():
    print("🎮 Welcome to the Wiki Word Chain Game!")
    beginner_level()
    intermediate_level()
    advanced_level()
    print("\n🏆 Game Over! Thanks for playing!")


if __name__ == "__main__":
    main()