from synthesizer import Player, Synthesizer, Waveform, Writer
import pychord

player = Player()
player.open_stream()
writer = Writer()
loop = 4
chords = []
choice1 = None

while loop == 4:
    vol = float(input("Choose application volume (0 - 0.5 - 1 and inbetween): "))
    if vol < 0 or vol > 1:
        print("Please pick a number as instructed.")
    loop = 3

while loop >= 2:
    true = True
    form = input("Choose waveform (sawtooth, sine, square and triangle): ")
    if form != "sawtooth" or "sine" or "square" or "triangle":
        print("Please pick a waveform from the list.")
    if form == "sawtooth":
        synthesizer = Synthesizer(
            osc1_waveform=Waveform.sawtooth, osc1_volume=vol, use_osc2=False
        )
    if form == "sine":
        synthesizer = Synthesizer(
            osc1_waveform=Waveform.sine, osc1_volume=vol, use_osc2=False
        )
    if form == "square":
        synthesizer = Synthesizer(
            osc1_waveform=Waveform.square, osc1_volume=vol, use_osc2=False
        )
    if form == "triangle":
        synthesizer = Synthesizer(
            osc1_waveform=Waveform.triangle, osc1_volume=vol, use_osc2=False
        )

    print("")
    print("Press 1 to type a chord, Press 2 to type a waveform.")
    print("")
    if choice1 is None:
        choice1 = int(input())
    else:
        pass

    if choice1 == 1:
        print("")
        print("Enter chord.")
        print("")
        print("Chords examples: C3, G7, F3.")
        print("")
        print("You can create a chord progression.")
        print("")
        print("""Type "Stop" to finish.""")
        while true is True:
            print("")
            c1 = input()
            if c1 == "Stop" or c1 == "stop":
                true = False
            else:
                chords.append(c1)

        choice1 = None
        choice2 = 1
        print("")

    elif choice1 == 2:
        while true is True:
            print("")
            wave_frequency = int(input("Enter the wave frequency: "))
            print("")
            print("Wave length means how long the wave will play.")
            wave_length = int(input("Enter wave length: "))
            print("")
            choice1 = None
            choice2 = 2
            true = False

    if choice2 == 1:
        print("Wave length means how long the wave will play.")
        wave_length2 = int(input("Enter wave length: "))

        for single in chords:
            chord = [f"{single}"]
            player.play_wave(synthesizer.generate_chord(chord, wave_length2))

    if choice2 == 2:
        wf = int(wave_frequency)
        wl = int(wave_length)
        player.play_wave(synthesizer.generate_constant_wave(wf, wl))

    print("")
    print("Press 1 to save as .wav file")
    print("")
    print("Press 2 to restart.")
    print("")

    x = int(input())

    if x == 1:
        if choice2 == 1:
            wave = synthesizer.generate_chord(chords, wave_length2)
            writer.write_wave("sounds", wave)

        if choice2 == 2:
            writer.write_wave(
                "sounds",
                synthesizer.generate_constant_wave(wf, wl),
            )

        loop = loop + 1
    if x == 2:
        loop = loop + 1
        c1.clear()
