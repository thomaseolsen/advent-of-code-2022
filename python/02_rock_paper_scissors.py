with open("../input_data/02_rock_paper_scissors.txt") as f:
    RPS_GAME = f.read().split("\n")

OPP_ROCK = "A"
OPP_PAPER = "B"
OPP_SCISSORS = "C"

SELF_ROCK = "X"
SELF_PAPER = "Y"
SELF_SCISSORS = "Z"

SCORE_WIN = 6
SCORE_DRAW = 3
SCORE_LOSE = 0

SCORE_PLAY = {
    SELF_ROCK: 1,
    SELF_PAPER: 2,
    SELF_SCISSORS: 3,
}

P2_RESULT_LOSE = "X"
P2_RESULT_DRAW = "Y"
P2_RESULT_WIN = "Z"

def p1_round_result(round: str) -> int:
    match round:
        case "A X" | "B Y" | "C Z":
            return SCORE_DRAW
        case "A Y" | "B Z" | "C X":
            return SCORE_WIN
        case "A Z" | "B X" | "C Y":
            return SCORE_LOSE
        case _:
            return 0

def p2_round_result(round: str) -> int:
    move_score: int
    match round:
        case "A X" | "B X" | "C X":
            match round[0]:
                case "A":
                    move_score = SCORE_PLAY.get(SELF_SCISSORS)
                case "B":
                    move_score = SCORE_PLAY.get(SELF_ROCK)
                case "C":
                    move_score = SCORE_PLAY.get(SELF_PAPER)
                case _:
                    move_score = 0
            return SCORE_LOSE + move_score
        case "A Y" | "B Y" | "C Y":
            match round[0]:
                case "A":
                    move_score = SCORE_PLAY.get(SELF_ROCK)
                case "B":
                    move_score = SCORE_PLAY.get(SELF_PAPER)
                case "C":
                    move_score = SCORE_PLAY.get(SELF_SCISSORS)
                case _:
                    move_score = 0
            return SCORE_DRAW + move_score
        case "A Z" | "B Z" | "C Z":
            match round[0]:
                case "A":
                    move_score = SCORE_PLAY.get(SELF_PAPER)
                case "B":
                    move_score = SCORE_PLAY.get(SELF_SCISSORS)
                case "C":
                    move_score = SCORE_PLAY.get(SELF_ROCK)
                case _:
                    move_score = 0
            return SCORE_WIN + move_score
        case _:
            return 0

p1_running_score = 0
p2_running_score = 0

for round in RPS_GAME:
    p1_running_score += SCORE_PLAY.get(round[2]) + p1_round_result(round)
    p2_running_score += p2_round_result(round)

print(p1_running_score)  # 14,163
print(p2_running_score)  # 12,091
