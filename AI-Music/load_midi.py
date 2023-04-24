from music21 import converter, chord, note

dataset_name = "Bach"
filename = "vs1-1ada"
file = "data/Bach/vs1-1ada.mid".format()

original_score = converter.parse(file).chordify()