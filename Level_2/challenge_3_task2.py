jane_dict = {'first_name': 'Jane',
             'surname': 'Doe', 'Age': 42, 'Employed': True}

tom_dict = {'first_name': 'Tom',
            'surname': 'Smith', 'Age': 18, 'Employed': True}
mariam_dict = {'first_name': 'Mariam',
               'surname': 'Coulter', 'Age': 66, 'Employed': False}
gregory_dict = {'first_name': 'Gregory',
                'surname': 'Tims', 'Age': 66, 'Employed': False}

people = [jane_dict, tom_dict, mariam_dict, gregory_dict]


def print_people(people):
    for person in people:
        f_name = person['first_name']
        surname = person['surname']
        age = person['Age']
        print(f'Name: {f_name} {surname}')
        print(f'Age: {str(age)}')
        if person['Employed']:
            print('Employed: Yes')
        else:
            print('Employed: No')


def remove_person(people):
    removed_person = input(
        'State the first name of the person you would like to remove.')
    for person in people:
        if person['first_name'] == removed_person:
            people.remove(person)
    return (people)


def add_person(people):
    new_dict = {}
    f_name = input('First Name: ')
    surname = input('Surname: ')
    age = int(input('Age: '))
    employed = input('Employed (Y/N): ')
    if employed == 'Y':
        employed = True
    else:
        employed = False
    new_dict['first_name'] = f_name
    new_dict['surname'] = surname
    new_dict['Age'] = age
    new_dict['Employed'] = employed
    people.append(new_dict)
    return people


finished = False
while finished == False:
    print_people(people)
    while True:
        choice = input('Add or Remove')
        if choice == 'Add':
            people = add_person(people)
            finished_answer = input('If you are finished, type "finished".')
            if finished_answer == 'finished':
                finished = True
                print('This is your final database.')
                print_people(people)
            break
        elif choice == 'Remove':
            people = remove_person(people)
            finished_answer = input('If you are finished, type "finished".')
            if finished_answer == 'finished':
                finished = True
                print('This is your final database.')
                print_people(people)
            break
        else:
            print('Please only input Add or Remove.')
