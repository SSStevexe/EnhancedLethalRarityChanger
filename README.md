# Enhanced Lethal Company Rarity Changer

## What is this?
This allows mod makers to quickly change the rarity of the monsters in their mod packs without having to manually change the rarity of each monster.

## How to use?

- Have the script in the same directory as a file that contains monster rarity data.
- Run the script with the following command:
  - `py ./enhanced_lethal_company_rarity_changer.py <path to rarity file> <path to output file> <rarity to change to>`
    - You don't need to supply arguments. In this case you can use: `py ./enhanced_lethal_company_rarity_changer.py`
  - Below is an example of  what the rarity file should look like (taken from LethalEnhanced)
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

### Sample output when given change rarity of 100

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