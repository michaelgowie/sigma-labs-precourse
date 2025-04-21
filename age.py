import datetime


def age_calculator(date_str):
    today = datetime.date.today()
    historical_date = datetime.datetime(
        int(date_str[:4]), int(date_str[5:7]), int(date_str[8:]))
    if historical_date.month > today.month:
        difference = (today.year - historical_date.year) - 1
    elif historical_date.month < today.month:
        difference = today.year - historical_date.year
    else:
        if historical_date.day <= today.day:
            difference = today.year - historical_date.year
        else:
            difference = today.year - historical_date.year - 1
    return difference


if __name__ == "__main__":
    print(age_calculator("1972-04-22"))
