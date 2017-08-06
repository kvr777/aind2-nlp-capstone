import os
import codecs


def load_data(path):
    """
    Load dataset
    """
    input_file = os.path.join(path)
    with codecs.open(input_file, "rb", "utf-8") as f:
        data = f.read()

    return data.split('\n')
