import re
import math
from collections import Counter

def check_length(password):
    """Check if password meets minimum length requirement."""
    return len(password) >= 8

def check_character_types(password):
    """Check for presence of uppercase, lowercase, digits, and special characters."""
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    return has_upper, has_lower, has_digit, has_special

def calculate_entropy(password):
    """Calculate Shannon entropy of the password."""
    if not password:
        return 0
    freq = Counter(password)
    total_chars = len(password)
    entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in freq.values())
    return entropy

def evaluate_password(password):
    """Evaluate password strength based on length, character types, and entropy."""
    length_ok = check_length(password)
    has_upper, has_lower, has_digit, has_special = check_character_types(password)
    entropy = calculate_entropy(password)

    # Scoring system
    score = 0
    if length_ok:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if entropy > 3.5:  # Threshold for strong entropy
        score += 1

    # Classify strength
    if score <= 2:
        return "Weak", score
    elif score == 3:
        return "Medium", score
    else:
        return "Strong", score

def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Enter your password to evaluate: ")
    strength, score = evaluate_password(password)
    print(f"Password Strength: {strength} (Score: {score}/5)")

# Run the program
if __name__ == "__main__":
    main()
