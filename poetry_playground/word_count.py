import pandas as pd
import re

from poetry_playground.format import format_ascii_table


def word_count():
    """
    Do a wordcount of the README.md file. This uses the Pandas library, which is a bit overkill for this, but we need
    to learn in small steps!
    """

    try:
        with open("README.md", "r") as f:
            text = f.read()
    except FileNotFoundError:
        print("The README.md file was not found. Please run this script from the root of the project.")
        exit()

    # Split words on whitespace and filter out unwanted characters
    words = re.findall(r'\b\w+\b', text)

    # Create a DataFrame and perform word count
    df = pd.DataFrame(words, columns=['word'])
    word_count = df['word'].value_counts().reset_index()
    word_count.columns = ['word', 'count']

    # Filter the top ten most frequent words
    top_ten_words = word_count.sort_values(by='count', ascending=False).head(10)

    # Format word_count DataFrame as an ASCII table
    ascii_table = format_ascii_table(top_ten_words)
    print(ascii_table)

