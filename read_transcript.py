from collections import namedtuple
import csv

phn_line = namedtuple('transcription', ['start_s', 'end_s', 'label'])

def read_transcription_file(phn_file, sample_rate=16000):
    phn_data = []

    with open(phn_file, 'r') as open_f:
        cread = csv.reader(open_f, delimiter=' ')
        for row in cread:
            phn_data.append(phn_line(
                (int(row[0]) / sample_rate),
                (int(row[1]) / sample_rate),
                row[2]
            ))
    return phn_data