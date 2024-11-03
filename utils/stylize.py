

def stylize(s, bold=True, color=None, c = None):
    """
    Format a string with ANSI escape codes for bold and color.
    
    Args:
    s (str): The string to format
    bold (bool): Whether to make the string bold
    color (str): The color to use. Can be 'blue', 'green', or 'red'
    c (str): Alternative parameter for color. Can be 'b', 'g', or 'r'

    Returns:
    str: The formatted string
    """
    format_codes = []
    
    if bold:
        format_codes.append('1')
    
    # Use color if provided, otherwise use c if provided
    color_param = color or c

    # If color_param is None, default to green
    if color_param is None:
        color_param = 'g'

    if color_param:
        # Mapping of color names to ANSI codes
        color_codes = {
            'red': '31', 'r':'31',
            'green': '32', 'g': '32',
            'yellow': '33', 'y': '33',
            'blue': '34', 'b': '34',
            'magenta': '35', 'm': '35',
            'cyan': '36', 'c': '36',
             # Extended color codes
            'orange': '38;5;208', 'o': '38;5;208',
            'pink': '38;5;213', 'p': '38;5;213'
        }
        if color_param in color_codes:
            format_codes.append(color_codes[color_param])
    
    if format_codes:
        return f"\033[{';'.join(format_codes)}m{s}\033[0m"
    else:
        return s

if __name__ == "__main__":
    s = "generated_llm_output"
    print(stylize(s, bold=True) + ": This is a non-styled string")
    print(stylize(s, bold=False) + ": This is a non-styled string")
    print(stylize(s, color='blue'))
    print(stylize(s, c='b', bold=False))
    print(stylize(s, bold=True, color='green'))
    print(stylize(s, color="pink"))