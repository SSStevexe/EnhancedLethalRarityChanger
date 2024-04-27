import json

file_with_monster_rarity = 'sample_rarity.txt'
file_output_monster_rarity = 'output_rarity.txt'
data: {} = {}


def get_user_input():
    change_rarity_by = input('Enter the rarity change (will affect all rarities except those with 0):')
    # make sure the input is a number
    if not change_rarity_by.isdigit():
        print('Please enter a number')
        get_user_input()
    return int(change_rarity_by)


def get_json_data() -> {}:
    global data
    try:
        with open(file_with_monster_rarity) as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f'File not found: {file_with_monster_rarity}')
        print('Please make sure the file is in the same directory as the script')
        exit(0)
    except json.JSONDecodeError:
        print(f'Error decoding JSON file: {file_with_monster_rarity}')
        print('Please make sure the file is a valid JSON file!')
        exit(0)


def change_rarity(change_by, affect_zero=False):
    for monster in data:
        if monster['value']['rarity'] != 0:
            if monster['value']['rarity'] + change_by < 0:
                monster['value']['rarity'] = 0
            monster['value']['rarity'] += change_by


def write_to_file():
    with open(file_output_monster_rarity, 'w') as f:
        json.dump(data, f, indent=4)
        f.close()


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Change the rarity of monsters in a JSON file')
    parser.add_argument('file', default=file_with_monster_rarity, nargs="?", help='The file containing the monster data')
    parser.add_argument('change', default=0, nargs="?", help='The amount to change the rarity by')
    parser.add_argument('affect_zero', default=False, nargs="?", help='Whether to affect monsters with rarity 0. Will not go below 0.')
    args = parser.parse_args()
    return args.file, args.change, args.affect_zero


if __name__ == '__main__':
    args = parse_args()
    file_with_monster_rarity = args[0]
    change = int(args[1])
    affect_zero = args[2]

    get_json_data()
    change_rarity(change if change > 0 else get_user_input(), affect_zero)
    write_to_file()
    print("Data has been written to output_rarity.txt!")
