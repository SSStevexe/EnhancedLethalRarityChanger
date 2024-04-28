# Enhanced Lethal Company Rarity Changer

## What is this?
This allows mod makers to quickly change the rarity of the monsters in their mod packs without having to manually change the rarity of each monster

- Supports negative numbers to decrease rarity
- Will optionally not change rarities that are 0.
- If negative numbers are used, it will not go below 0

## How to use?

- Have the script in the same directory as a file that contains monster rarity data. Sample rarity data file is either by default `sample_rarity.txt` or supplied through an argument `--input_file`
- Run the script with the following commands:
  - `py ./rarity_changer.py` this will prompt you for further instructions
  - `py ./rarity_changer.py --modify_zero` This will allow zeros to be changed as well.
  - `py ./rarity_changer.py --modify_zero --change_amount 100` This will change all rarities to 100
  - `py ./rarity_changer.py --change_amount 100 "` This will change rarities to 100 but **NOT** affect rarities that are 0 in file specified
- Other commands 
  - `py ./rarity_changer.py --input_file "path/to/file.txt"` This will use the file specified instead of the default file
## Below is an example of  what the rarity file should look like (taken from LethalEnhanced)
```json
[
  {
    "key": "Puffer",
    "value": {
      "override": true,
      "rarity": 30
    }
  },
  {
    "key": "Blob",
    "value": {
      "override": true,
      "rarity": 20
    }
  },
  {
    "key": "Masked",
    "value": {
      "override": true,
      "rarity": 14
    }
  },
  {
    "key": "Flowerman",
    "value": {
      "override": true,
      "rarity": 12
    }
  },
  {
    "key": "Crawler",
    "value": {
      "override": true,
      "rarity": 18
    }
  },
  ...
]

```

## Sample output when given change rarity of 100

```json
[
    {
        "key": "Puffer",
        "value": {
            "override": true,
            "rarity": 130
        }
    },
    {
        "key": "Blob",
        "value": {
            "override": true,
            "rarity": 120
        }
    },
    {
        "key": "Masked",
        "value": {
            "override": true,
            "rarity": 114
        }
    },
    {
        "key": "Flowerman",
        "value": {
            "override": true,
            "rarity": 112
        }
    },
    {
        "key": "Crawler",
        "value": {
            "override": true,
            "rarity": 118
        }
    }
...
```