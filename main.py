def what_day(num: int) -> str:
    """
    Return the weekday according to the input number.
    :param num:
    :return:
    """
    days_dict = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days_dict[num] if num in days_dict else "Wrong, please enter a number between 1 and 7"
