import pretty_errors

pretty_errors.configure(
    separator_character='*',
    filename_display=pretty_errors.FILENAME_EXTENDED,
    line_color=pretty_errors.RED + '> ' + pretty_errors.default_config.line_color,
    display_link=True,
    # timestamp_color= pretty_errors.CYAN,
    display_timestamp=True,
)

if __name__ == "__main__":
    # Simulate a NameError by trying to print an undefined variable
    # print(undefined_variable)

    my_dict = {"apple": 3, "banana": 2}
    count = my_dict["cherry"]  # Causes a KeyError

    # big_list = [0] * 10**9 # memory error

