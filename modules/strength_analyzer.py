import re


class StrengthAnalyzer:

    @staticmethod
    def analyze(password):

        score = 0

        if len(password) >= 8:
            score += 20

        if len(password) >= 12:
            score += 20

        if re.search(r"[A-Z]", password):
            score += 15

        if re.search(r"[a-z]", password):
            score += 15

        if re.search(r"\d", password):
            score += 15

        if re.search(r"[!@#$%^&*()_+=-]", password):
            score += 15

        if len(set(password)) > 8:
            score += 10

        score = min(score, 100)

        if score >= 80:
            level = "Strong"
        elif score >= 50:
            level = "Moderate"
        else:
            level = "Weak"

        return {
            "score": score,
            "level": level
        }