import re
import pandas as pd
import os
import csv


def edit_distance(s1, s2):
    """Calculate the Levenshtein distance between two strings."""
    if len(s1) < len(s2):
        return edit_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def find_position_of_similar_word(word, sentence):
    matches = list(re.finditer(r'\b\w+\'?\w*\b', sentence))
    min_distance = float('inf')
    best_position = None
    duplicate = False

    for match in matches:
        sentence_word = match.group(0)
        distance = edit_distance(word, sentence_word)
        if distance < min_distance:
            min_distance = distance
            best_position = (match.start(), match.end())
            duplicate = False
        elif distance == min_distance:
            duplicate = True

    if duplicate:
        return -1

    return best_position

def update_word_positions_in_corpus(corpus_number):

    dwug_folder = f"./rusemshift_{corpus_number}/DWUG/data"

    words = os.listdir(dwug_folder)
    print("List of word directories:", words)
    words.sort() # optional sort to track the progress

    counter = 0
    sentence_counter = 0
    multiple = 0
    # iterate over folders in dwug_folder:
    for word in words:
            uses_df = pd.read_csv(os.path.join(dwug_folder, word, 'uses.csv'), sep='\t')

            sentences = uses_df['context']
            sentence_counter += len(sentences)

            positions = uses_df['indexes_target_token']

            new_positions = []
            for sentence, position in zip(sentences, positions):
                pos1, pos2 = position.split(':')

                word_full = sentence[int(pos1):int(pos2)]
                
                if word_full.lower() != word:
                        new_position = find_position_of_similar_word(word, sentence)
                        if new_position == -1:
                            multiple += 1
                            new_positions.append(position)
                            continue

                        # fix position
                        new_positions.append(f'{new_position[0]}:{new_position[1]}')
                        counter += 1
                else:
                    new_positions.append(position)

            uses_df['indexes_target_token'] = new_positions

            # save the updated uses_df
            uses_df.to_csv(os.path.join(dwug_folder, word, 'uses.csv'), sep='\t', index=False, quoting=csv.QUOTE_NONE)

    print("Count of positions not pointing to the lemma of the word:", counter)
    print("Total number of sentences in corpus:", sentence_counter)
    print("Count of multiple best_match words, where position was left as original:", multiple)

update_word_positions_in_corpus(1)
update_word_positions_in_corpus(2)
