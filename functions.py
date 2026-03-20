def estimate_1rm(weight, reps, rpe):
    rir = 10 - rpe
    r_eff = rir + reps
    onerm = weight*(1+(rEff/30))
    return onerm

def suggest_weight(current_weight, current_reps, current_rpe, target_reps, target_rpe):
    onerm = estimate_1rm(current_weight, current_reps, current_rpe)
    target_rir = 10 - target_rpe
    r_eff = target_rir + target_reps
    target_weight = onerm/(1+(target_rEff/30))
    
    return target_weight

def round_weight(weight, base):
    weight_ratio = weight/base
    rounded_weight_ratio = round(weight_ratio)
    rounded_weight = round(rounded_weight_ratio*base,1)

    return rounded_weight

program = {
    1: {"5x5": 6.5,
        "3x3": 7,
        "1x1": 8},
    2: {"5x5": 7.5,
        "3x3": 8,
        "1x1": 8.5},
    3: {"5x5": 8,
        "3x3": 8.5,
        "1x1": 9.5},
    4: {"5x5": 8.5,
        "3x3": 9.5,
        "1x1": 10}
}

microcycle = "3x3"
mesocycle = 2

target_reps = int(microcycle.split("x")[0])
target_rpe = program[mesocycle][microcycle]