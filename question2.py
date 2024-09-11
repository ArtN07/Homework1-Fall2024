"""
ECE241 Fall 2024 - Homework1 Question2
"""

class Question2:
    @staticmethod
    def solveMonomial(a, b, c):
        """

        :param a:
        :param b:
        :param c:
        :return:
        """
        # fill in your logic here

        return -1

    @staticmethod
    def solvePolynomial(a, b, c):
        """

        :param a:
        :param b:
        :param c:
        :return:
        """
        # fill in your logic here

        return -1

    @staticmethod
    def autograder():
        monomial_result = "REPLACE_WITH_YOUR_RESULT_HERE"
        polynomial_result = "REPLACE_WITH_YOUR_RESULT_HERE"

        # Do NOT change the code below!
        return {
           "monomial": monomial_result,
            "polynomial": polynomial_result
        }


if __name__ == "__main__":
    a = int(input("Please input the value for a: "))
    b = int(input("Please input the value for b: "))
    c = int(input("Please input the value for c: "))
    print("Monomial:", Question2.solveMonomial(a, b, c))
    print("Polynomial:", Question2.solvePolynomial(a, b, c))

