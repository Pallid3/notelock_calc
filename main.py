# od = 9
# bpm = 236
# rhythm = 2 # Choose the rhythm. For example 1/1, 1/2th, 1/3rd or 1/4th.
# ar = 9.8


def inputfloat(no_way):
    while True:
        try:
            a = float(input(no_way))
            break
        except ValueError:
            print("you suck ass")
    return a

def inputrhythm(no_way):
    while True:
        try:
            a = int(input(no_way))
            if a > 4:
                print("you suck ass, big number does not = funny")
                continue
            break
        except ValueError:
            print("you suck ass")
    return a

od = inputfloat("od: ")
bpm = inputfloat("bpm: ")
rhythm = inputrhythm("rhythm: ")
ar = inputfloat("ar: ")

note_one_one = bpm * 1
note_one_two = bpm * 2
note_one_three = bpm * 3
note_one_four = bpm * 4

notes = [note_one_one, note_one_two, note_one_three, note_one_four]

def calc_od50(od):
    od50 = 200 - (10 * od)
    return od50

def calc(tempo):
    notes_per_second = tempo / 60
    time_between_notes = 1000 / notes_per_second
    time_between_notes = round(time_between_notes)
    return notes_per_second, time_between_notes

def ar_calc(ar):
    if ar < 5:
        preempt = 1200 + 120 * (5 - ar)
    elif ar == 5:
        preempt = 1200
    elif ar > 5:
        preempt = 1200 - 150 * (ar - 5)
    return preempt

def density(ar, bpm, rhythm):
    preempt = ar_calc(ar)
    tempo = notes[rhythm-1]
    notes_per_second, time_between_notes = calc(tempo)
    dens = preempt/time_between_notes
    # print("time_between_notes: ", time_between_notes, "; preempt:", preempt)
    return dens

def main_notelock(rhythm):
    tempo = notes[rhythm-1]
    notes_per_second, time_between_notes = calc(tempo)
    hit_window = calc_od50(od)
    your_chance = time_between_notes - hit_window
    # print("notes_per_second:", notes_per_second)
    # print("time_between_notes:", time_between_notes, "ms")
    # print("OD:", od)
    # print("BPM:", bpm)
    if your_chance > 0:
        print("To escape notelock you have to click earliest at", your_chance-1, "ms before the perfect hit") # your_chance-1 cuz i cba to check how osu rounding works
    else:
        print("Go kys")
        print("To escape notelock you have to click earliest at", -your_chance+1, "ms AFTER the perfect hit")

def main_density(ar, bpm, rhythm):
    density_real = density(ar, bpm, rhythm)
    density_round = round(density_real, 2)
    print("Density:", density_round)

main_notelock(rhythm)
main_density(ar, bpm, rhythm)

