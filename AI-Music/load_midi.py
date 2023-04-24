from music21 import converter, chord, note

dataset_name = "cello"
filename = "cs1-2all"
file = "./data/{}/{}.mid".format(dataset_name, filename)

original_score = converter.parse(file).chordify()