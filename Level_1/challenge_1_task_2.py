name = input('Hello, what\'s your name?')
if name in ["alice", "Alice", 'bob', 'Bob']:
    print(f'Hello, {name.title()}')
else:
    print('I can\'t greet you!')
