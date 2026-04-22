od = 10
bpm=298

note_one_one = bpm * 1
note_one_two = bpm * 2
note_one_three = bpm * 3
note_one_four = bpm * 4

notes = [note_one_one, note_one_two, note_one_three, note_one_four]

only_bpm_and_one_two = [note_one_two] # yeah I asked gpt to put my variables in list, and now this is running in main function, rest of the code is not vibecoded.

def calc_od50(od):
    od50 = 200 - (10 * od)
    return od50

def calc(tempo):
    notes_per_second = tempo / 60
    time_between_notes = 1000 / notes_per_second
    time_between_notes = round(time_between_notes)
    return notes_per_second, time_between_notes

for tempo in only_bpm_and_one_two:
    notes_per_second, time_between_notes = calc(tempo)
    hit_window = calc_od50(od)
    your_chance = time_between_notes - hit_window
    # print("notes_per_second:", notes_per_second)
    # print("time_between_notes:", time_between_notes, "ms")
    print("OD:", od)
    print("BPM:", bpm)
    if your_chance > 0:
        print("To escape notelock you have to click earliest at", your_chance-1, "ms before perfect hit") # your_chance-1 cuz i cba to check how osu rounding works
    else:
        print("Go kys")
        print("To escape notelock you have to click earliest at", -your_chance+1, "ms after perfect hit")
