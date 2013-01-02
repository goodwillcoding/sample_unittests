# -*- coding: utf-8 -*-


# --------------------------------------------------------------------------- #
class NoSeparatorError(Exception):
    pass


# --------------------------------------------------------------------------- #
def split_argument(string):
    """
    Split the given string ":" or "=" separated strings to a two element
    tuple. If both ":" and "=" are present in the string the first one
    is used as a separator.

    :param args_list:

        string separated by either ":" or "=" (which ever comes first).

    :return: two element tuple split by : or = where first element args
             key and second element as value.
    :rtype: tuple

    :raises: ScriptArgumentError if neither ":" nor "=" separator are not
             present in the given string.
    """

    # find the separator
    colon_pos = string.find(":")
    equal_pos = string.find("=")

    if (colon_pos == -1) and (equal_pos == -1):
        raise NoSeparatorError(
            "List element '%s' is missing a separator, either ':' or '='"
            % string)

    # remove the -1 if it exists and grab the closest position
    separator_pos = min(val for val in [colon_pos, equal_pos] if val != -1)
    # return (key, value)
    return (string[:separator_pos], string[separator_pos + 1:])
