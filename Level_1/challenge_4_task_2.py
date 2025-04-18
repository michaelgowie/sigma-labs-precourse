def outed(meet, boss):
    total = 0
    for name in meet.keys():
        if name == boss:
            total += (meet[name] * 2)
        else:
            total += meet[name]
    score = total / len(meet.keys())
    if score <= 5:
        return ('Get Out Now!')
    else:
        return ('Nice Work Champ!')


def boredom(staff):
    boredom_dict = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3, 'trading': 6, 'change': 6, 'IS': 8, 'retail': 5,
                    'cleaning': 4, 'pissing about': 25}
    total = 0
    for name in staff.keys():
        total += boredom_dict[staff[name]]
    if total <= 80:
        return 'kill me now'
    elif total < 100:
        return 'i can handle this'
    else:
        return 'party time!!'
