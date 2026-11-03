def calculate_discount(homework_score, test_score):
    if 76 <= homework_score <= 80 and 80 <= test_score <= 100:
        return 5000
    elif 71 <= homework_score <= 75 and 80 <= test_score <= 100:
        return 4000
    elif 65 <= homework_score <= 70 and 80 <= test_score <= 100:
        return 3000
    elif 65 <= homework_score <= 80 and 50 <= test_score <= 79:
        return 2500
    elif 55 <= homework_score <= 64 and 80 <= test_score <= 100:
        return 2000
    elif 55 <= homework_score <= 64 and 50 <= test_score <= 79:
        return 1000
    else:
        return 0