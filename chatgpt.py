import re
import warnings


# edited from chatgpt output
def remove_invalid_windows_chars(filename):
    # Define the regular expression for invalid characters in Windows file paths
    invalid_chars_regex = re.compile(r'[<>:"/\\|?*\x00-\x1F]')

    # Replace invalid characters with underscores
    cleaned_filename = re.sub(invalid_chars_regex, '_', filename)

    # Find removed characters
    removed_chars = ''.join(invalid_chars_regex.findall(filename))

    if removed_chars != '':
        warnings.warn(
            f'Invalid Filename: "{filename}" due to characters: "{removed_chars}". Generated using: "{cleaned_filename}"')
    return cleaned_filename


