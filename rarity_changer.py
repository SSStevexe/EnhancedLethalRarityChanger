import json

file_with_monster_rarity = 'sample_rarity.txt'
file_output_monster_rarity = 'output_rarity.txt'
data: {} = {}


def get_user_input(modify_rarity_zero=False):
    print('{} monsters with rarity 0'.format("Affecting" if modify_rarity_zero else "Not affecting"))
    change_rarity_by = input('Enter the rarity change: ')
    # make sure the input is a number
    if not change_rarity_by.isdigit():
        print('Please enter a number')
        get_user_input()
    return int(change_rarity_by)


def get_json_data(arg_input=file_with_monster_rarity) -> {}:
    global data
    try:
        with open(arg_input) as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f'File not found: {arg_input}')
        print('Please make sure the file is in the same directory as the script')
        exit(0)
    except json.JSONDecodeError:
        print(f'Error decoding JSON file: {arg_input}')
        print('Please make sure the file is a valid JSON file!')
        exit(0)


def change_rarity(change_by, affect_zero=False):
    for monster in data:
        if monster['value']['rarity'] != 0 or affect_zero:
            if monster['value']['rarity'] + change_by < 0:
                monster['value']['rarity'] = 0
            monster['value']['rarity'] += change_by


def write_to_file(arg_output_file=file_output_monster_rarity):
    with open(arg_output_file, 'w') as f:
        json.dump(data, f, indent=4)
        f.close()


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Change the rarity of monsters in a JSON file')
    parser.add_argument('--input_file', default=file_with_monster_rarity, nargs="?", help='The file containing the monster data')
    parser.add_argument('--output_file', default=file_output_monster_rarity, nargs="?", help='The file to output the data to')
    parser.add_argument('--change_amount', default=0, type=int, nargs="?", help='The amount to change the rarity by')
    parser.add_argument('--modify_zero', action='store_true', help='Whether to affect monsters with rarity 0. Will not go below 0.')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    file_with_monster_rarity = args.input_file
    file_output_monster_rarity = args.output_file
    change_amount = args.change_amount
    modify_zero = args.modify_zero

    get_json_data(file_with_monster_rarity)
    change_rarity(change_amount if change_amount > 0 else get_user_input(modify_zero), modify_zero)
    write_to_file(file_output_monster_rarity)
    print("Data has been written to output_rarity.txt!")
