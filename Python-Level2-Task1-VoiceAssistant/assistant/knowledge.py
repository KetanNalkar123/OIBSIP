"""
Built-in knowledge service.
"""


class KnowledgeService:
    """Answer common knowledge questions."""

    def __init__(self):

        self.knowledge = {

            "python": (
                "Python is a high-level, general-purpose "
                "programming language known for its simple "
                "and readable syntax."
            ),

            "who created python": (
                "Python was created by Guido van Rossum "
                "and was first released in 1991."
            ),

            "guido van rossum": (
                "Guido van Rossum is the creator of Python."
            ),

            "artificial intelligence": (
                "Artificial Intelligence, or AI, is the field "
                "of computer science that focuses on creating "
                "systems that can perform tasks that normally "
                "require human intelligence."
            ),

            "machine learning": (
                "Machine Learning is a branch of AI in which "
                "computer systems learn patterns from data "
                "and use those patterns to make predictions "
                "or decisions."
            ),

            "deep learning": (
                "Deep Learning is a type of machine learning "
                "that uses neural networks with multiple layers "
                "to learn complex patterns from data."
            ),

            "data science": (
                "Data Science combines statistics, programming, "
                "machine learning and domain knowledge to "
                "extract useful insights from data."
            ),

            "github": (
                "GitHub is a platform used to host, manage "
                "and collaborate on software development "
                "projects using Git."
            ),

            "api": (
                "An API, or Application Programming Interface, "
                "allows different software applications to "
                "communicate with each other."
            ),

            "oop": (
                "Object-Oriented Programming is a programming "
                "approach based on objects and classes. "
                "Its common principles include encapsulation, "
                "inheritance, polymorphism and abstraction."
            )
        }

    # ==================================================
    # Answer
    # ==================================================

    def answer(self, question):

        if not question:

            return (
                "Please ask me a knowledge question."
            )

        question = question.lower().strip()

        # --------------------------------------------------
        # Specific Python creator question
        # --------------------------------------------------

        if (
            "who created python" in question
            or "who invented python" in question
            or "who developed python" in question
        ):

            return self.knowledge[
                "who created python"
            ]

        # --------------------------------------------------
        # Search knowledge keywords
        # --------------------------------------------------

        keyword_order = [
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "data science",
            "guido van rossum",
            "github",
            "object oriented programming",
            "oop",
            "api",
            "python"
        ]

        for keyword in keyword_order:

            if keyword in question:

                if (
                    keyword ==
                    "object oriented programming"
                ):

                    return self.knowledge["oop"]

                return self.knowledge.get(
                    keyword,
                    self.knowledge["python"]
                )

        return (
            "I do not have a built-in answer for "
            "that question yet."
        )