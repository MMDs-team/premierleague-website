ACTION_NAMES = [
    'goal',
    'assist',
    'goal_from_header',
    'goal_from_penalty',
    'goal_from_freekick',
    'goal_from_inside_box',
    'goal_from_outside_box',
    'goal_from_counter_attack',
    'save',
    'own_goal',
    'shot',
    'pass',
    'cross',
    'offside',
    'yellow_card',
    'red_card',
    'tackle',
    'foul',
    'penalty',
    'corner ',
    'clean_sheet',
    'appearance'
]

ID_START = 1
ACTIONS = dict(zip(
    ACTION_NAMES, 
    range(ID_START, len(ACTION_NAMES) + 1)
))