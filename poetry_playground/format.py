def format_ascii_table(data, columns=None, header=True, min_col_width=5, padding=1):
    """Format a Pandas DataFrame into an ASCII table.

    Args:
        data (pd.DataFrame): The input DataFrame to format.
        columns (list): The columns to include in the table. If None, all columns will be included.
        header (bool): If True, include the header row in the output.
        min_col_width (int): The minimum width for each column.
        padding (int): The number of spaces to add on either side of each cell.

    Returns:
        str: The formatted ASCII table.
    """

    # If no specific columns provided, use all columns
    if columns is None:
        columns = data.columns

    # Calculate column widths based on content
    col_widths = [
        max(min_col_width, max(len(str(x)) for x in data[col].values) + 2 * padding, len(col) + 2 * padding)
        for col in columns
    ]

    # Function to create a row separator
    def row_separator(char="-"):
        return "+" + "+".join([char * width for width in col_widths]) + "+"

    # Format header row
    if header:
        header_row = "|{}|".format("|".join([f"{col:^{col_widths[i]}}" for i, col in enumerate(columns)]))
    else:
        header_row = ""

    # Format data rows
    data_rows = []
    for _, row in data.iterrows():
        formatted_row = "|{}|".format("|".join([f"{str(row[col]):^{col_widths[i]}}" for i, col in enumerate(columns)]))
        data_rows.append(formatted_row)

    # Combine header and data rows
    formatted_table = row_separator("+") + "\n"
    if header:
        formatted_table += header_row + "\n"
        formatted_table += row_separator("+") + "\n"
    formatted_table += "\n".join(data_rows) + "\n"
    formatted_table += row_separator("-")

    return formatted_table