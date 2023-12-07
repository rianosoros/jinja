"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts,
    and the text of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "beach",
    "A Seaside Adventure",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a sun-kissed {place}, there lived a
       whimsical {adjective} {noun}. It loved to {verb} with {plural_noun}
       along the sandy shores, creating magical moments under the glistening sun."""
)

story3 = Story(
    "doctor",
    "A Medical Marvel",
    ["noun", "verb", "adverb", "plural_noun"],
    """Oh my goodness! I adore visiting the {noun} and {verb} with the skilled
       medical {plural_noun}. It's always an intriguing experience filled with
       health insights and a {adverb} of healing magic."""
)


stories = {s.code: s for s in [story1, story2, story3]}
