from random import choice

# randomly generate a comment from https://www.mcsweeneys.net/articles/a-pseudo-intellectual-comment-generator-for-men

A0 = [
    "Actually, the",
    "I'm sure you know that",
    "I didn't read it, but",
    "I hate to burst your bubble, but",
    "I'm sure you know that",
]

A1 = [
    "technocratic",
    "neo-liberal",
    "Marxist",
    "globalist",
    "totalitarian",
]

A2 = [
    "liberal fascists",
    "oligarchs",
    "propaganda machines",
    "corporate dems",
    "vaccine pushers",
]

A3 = [
    "will secretly",
    "are merely used to",
    "can always be counted on to",
    "should",
    "should not",
]

A4 = [
    "undermine",
    "conspire against",
    "suppress",
    '"cancel"',
    "supplant",
]

A5 = [
    "our republic. It's not a democracy, btw.",
    "my 1st amendment rights.",
    "late-stage capitalism.",
    "Bernie Sanders, every time.",
    "that hawk, Hillary Clinton.",
]

A6 = [
    "Let's just watch our civil liberties evaporate.",
    "Try doing your own research instead of following lamestream media.",
    'Read the "I Ching".',
    "Hope I'm wrong!",
    "Enjoy your fake pandemic!",
]

def well_actually():
    return f"{choice(A0)} {choice(A1)} {choice(A2)} {choice(A3)} {choice(A4)} {choice(A5)} Don't believe me? {choice(A6)}"
