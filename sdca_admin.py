import re
import sys
from pathlib import Path

import pandas as pd


def filter_cpr(filename=sys.argv[1]):
    """
    Keeps rows containing valid CPR numbers and write them to an excel file

    Parameters
    ----------
    filename : str
        Path to excel file with CPR candidates

    Returns
    -------
    None

    """
    # print("hey")

    def validate_cpr(text):
        """Check if any 10-digit number in a string matches the CPR criteria"""
        for ten_digit_number in re.findall('\d{10}', text):
            # Whatever your condition is goes here
            if int(ten_digit_number) > 1_111_111_111:
                return True
        return False

    # Filter and write excel file
    pd.read_excel(
        filename,
        # Apparently this column is a mix of str and int in excel
        dtype={'Linjeindhold for 1. fund': str}
    ).query(
        '`Linjeindhold for 1. fund`.apply(@validate_cpr)'
    ).to_excel(
        Path.cwd() / 'cpr-records.xlsx'
    )
    return
