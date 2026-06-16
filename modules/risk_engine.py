class RiskEngine:

    @staticmethod
    def calculate(score):

        if score >= 80:
            return "Low Risk"

        if score >= 50:
            return "Medium Risk"

        return "High Risk"