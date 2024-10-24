from sys import argv

# Order colors: red yellow blue black
data = [
    [ # Anna
        [0, 1, 0, 3],
        [2, 3, 1, 0],
        [0, 4, 1, 0],
    ],
    [ # Benjamin
        [2, 2, 1, 0],
        [2, 0, 1, 0],
        [2, 1, 0, 1],
    ],
    [ # Aiden
        [0, 1, 0, 1],
        [0, 0, 2, 0],
        [1, 0, 4, 0],
    ],
    [ # Tarana
        [0, 2, 1, 2],
        [2, 0, 1, 2],
        [1, 0, 1, 1],
    ],
    [ # Li Chang
        [0, 1, 3, 0],
        [2, 0, 2, 0],
        [3, 0, 3, 3],
    ],
]


def get_paths(
        color  : int,
        dataset: int,
        score  : int
):
    result = []
    for i, colorset in enumerate(data[dataset]):

        if dataset == 0 and colorset[color] <= TARGET_SCORE[color]:
            new_paths = get_paths(
                color,
                dataset + 1,
                colorset[color],
            )

            if len(new_paths) > 0:
                for path in new_paths:
                    result.append([i, *path])

            continue

        elif dataset > 0 and dataset < len(data) - 1 and score + colorset[color] <= TARGET_SCORE[color]:
            new_paths = get_paths(
                color,
                dataset + 1,
                score + colorset[color],
            )

            if len(new_paths) > 0:
                for path in new_paths:
                    result.append([i, *path])

            continue

        elif dataset == len(data) - 1:
            if score + colorset[color] == TARGET_SCORE[color]:
                result.append([i])
            continue

    return result


def print_matching_paths(
    red_paths   : list,
    yellow_paths: list,
    blue_paths  : list,
    black_paths : list
):
    print(f'\n[\x1b[32m+\x1b[0m] Possible Solution:\n')

    for path in red_paths:
        if path in yellow_paths\
        and path in blue_paths\
        and path in black_paths:
            print(
                 '┏━━━━━━━━━━┯━━━━━━━━━━━┓\n' +\
                 '┃ \x1b[1m\x1b[36mNAME\x1b[0m     │ \x1b[1m\x1b[36mNUMBER\x1b[0m    ┃\n' +\
                 '┠──────────┼───────────┨\n' +\
                f'┃ \x1b[34mAnna\x1b[0m     │ {path[0] + 1}         ┃\n' +\
                f'┃ \x1b[31mBenjamin\x1b[0m │ {path[1] + 1}         ┃\n' +\
                f'┃ \x1b[32mAiden\x1b[0m    │ {path[2] + 1}         ┃\n' +\
                f'┃ \x1b[35mTarana\x1b[0m   │ {path[3] + 1}         ┃\n' +\
                f'┃ \x1b[37mLi Chang\x1b[0m │ {path[4] + 1}         ┃\n' +\
                 '┗━━━━━━━━━━┷━━━━━━━━━━━┛\n'
            )


def main():
    if len(argv) != 5:
        print('Usage: python ./anomed_solver.py <red> <blue> <yellow> <black>')

    global TARGET_SCORE
    TARGET_SCORE = [int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4])]

    red_paths = get_paths(0, 0, 0)
    yellow_paths = get_paths(1, 0, 0)
    blue_paths = get_paths(2, 0, 0)
    black_paths = get_paths(3, 0, 0)

    print_matching_paths(
        red_paths,
        yellow_paths,
        blue_paths,
        black_paths
    )

if __name__ == '__main__':
    main()
