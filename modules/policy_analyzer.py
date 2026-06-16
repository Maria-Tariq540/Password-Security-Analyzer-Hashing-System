class PolicyAnalyzer:

    @staticmethod
    def evaluate(password):

        return {
            "minimum_length": len(password) >= 12,
            "uppercase": any(
                c.isupper()
                for c in password
            ),
            "lowercase": any(
                c.islower()
                for c in password
            ),
            "digit": any(
                c.isdigit()
                for c in password
            ),
            "special_character": any(
                not c.isalnum()
                for c in password
            )
        }