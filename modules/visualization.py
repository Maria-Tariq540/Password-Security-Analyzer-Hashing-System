import matplotlib.pyplot as plt
import os


class Visualization:

    @staticmethod
    def create_score_chart(score):

        os.makedirs(
            "static/charts",
            exist_ok=True
        )

        plt.figure(figsize=(5, 3))

        plt.bar(
            ["Security Score"],
            [score]
        )

        plt.ylim(0, 100)

        chart_path = (
            "static/charts/security_score.png"
        )

        plt.savefig(chart_path)

        plt.close()

        return chart_path