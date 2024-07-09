import sys
import json
import gzip
import glob
from tqdm import tqdm
from pprint import pprint
from collections import Counter

names = [
          "bff_duplicate_url",
          "bff_duplicate_doc",
          "my_tags__uniseg_length_paragraphs_with_doc_length_v1__document",
          "my_tags__gopher_swedish__word_count",
          "my_tags__gopher_swedish__word_count",
          "my_tags__gopher_swedish__median_word_length",
          "my_tags__gopher_swedish__median_word_length",
          "my_tags__gopher_swedish__symbol_to_word_ratio",
          "my_tags__gopher_swedish__fraction_of_words_with_alpha_character",
          "my_tags__gopher_swedish__required_word_count",
          "my_tags__gopher_swedish__fraction_of_lines_starting_with_bullet_point",
          "my_tags__gopher_swedish__fraction_of_lines_ending_with_ellipsis",
          "my_tags__gopher_swedish__fraction_of_duplicate_lines",
          "my_tags__gopher_swedish__fraction_of_characters_in_duplicate_lines",
          "my_tags__gopher_swedish__fraction_of_characters_in_most_common_2grams",
          "my_tags__gopher_swedish__fraction_of_characters_in_most_common_3grams",
          "my_tags__gopher_swedish__fraction_of_characters_in_most_common_4grams",
          "my_tags__gopher_swedish__fraction_of_characters_in_duplicate_5grams",
          "my_tags__gopher_swedish__fraction_of_characters_in_duplicate_6grams",
          "my_tags__gopher_swedish__fraction_of_characters_in_duplicate_7grams",
          "my_tags__gopher_swedish__fraction_of_characters_in_duplicate_8grams",
          "my_tags__gopher_swedish__fraction_of_characters_in_duplicate_9grams",
          "my_tags__gopher_swedish__fraction_of_characters_in_duplicate_10grams",
          ]

counts = {n: 0 for n in names}
total = 0
doc_lengths = {True: 0, False: 0}

files = glob.glob(f"{sys.argv[1]}*")

exceptions = Counter()
fout = open("/data/robin/wikia+wikipedia.txt", "w")

for fn in tqdm(files):
    with gzip.open(fn) as fh:
        for line in fh:
            try:
                total += 1
                d = json.loads(line)
    
                checks = [
                          "bff_duplicate_url" in d["attributes"] and d["attributes"]["bff_duplicate_url"][0][2] == 1,
                          "bff_duplicate_doc" in d["attributes"] and d["attributes"]["bff_duplicate_doc"][0][2] == 1,
                          d["attributes"]["my_tags__uniseg_length_paragraphs_with_doc_length_v1__document"][0][2] < 50,
                          d["attributes"]["my_tags__gopher_swedish__word_count"][0][2] < 50,
                          d["attributes"]["my_tags__gopher_swedish__word_count"][0][2] > 100000,
                          d["attributes"]["my_tags__gopher_swedish__median_word_length"][0][2] < 3,
                          d["attributes"]["my_tags__gopher_swedish__median_word_length"][0][2] > 10,
                          d["attributes"]["my_tags__gopher_swedish__symbol_to_word_ratio"][0][2] > 0.1,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_words_with_alpha_character"][0][2] < 0.8,
                          d["attributes"]["my_tags__gopher_swedish__required_word_count"][0][2] < 2,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_lines_starting_with_bullet_point"][0][2]  > 0.9,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_lines_ending_with_ellipsis"][0][2]  > 0.3,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_duplicate_lines"][0][2] > 0.3,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_lines"][0][2] >  0.3,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_most_common_2grams"][0][2] > 0.2,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_most_common_3grams"][0][2]  > 0.18,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_most_common_4grams"][0][2] > 0.16,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_5grams"][0][2]  > 0.15,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_6grams"][0][2] > 0.14,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_7grams"][0][2]  > 0.13,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_8grams"][0][2] > 0.12,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_9grams"][0][2]  > 0.11,
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_10grams"][0][2] > 0.10,
                          ]
                values = [
                          "bff_duplicate_url" in d["attributes"] and d["attributes"]["bff_duplicate_url"][0][2] == 1,
                          "bff_duplicate_doc" in d["attributes"] and d["attributes"]["bff_duplicate_doc"][0][2] == 1,
                          d["attributes"]["my_tags__uniseg_length_paragraphs_with_doc_length_v1__document"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__word_count"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__word_count"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__median_word_length"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__median_word_length"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__symbol_to_word_ratio"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_words_with_alpha_character"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__required_word_count"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_lines_starting_with_bullet_point"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_lines_ending_with_ellipsis"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_duplicate_lines"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_lines"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_most_common_2grams"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_most_common_3grams"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_most_common_4grams"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_5grams"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_6grams"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_7grams"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_8grams"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_9grams"][0][2],
                          d["attributes"]["my_tags__gopher_swedish__fraction_of_characters_in_duplicate_10grams"][0][2],
                          ]
                doc_lengths[len(d["text"].split()) < 50] += 1
                print(d["text"], file=fout)
                if any(checks) == True:
                    # pprint([(n,c,v) for n,c,v in zip(names, checks, values) if c])
                    # print(json.dumps(d["text"]))
                    # print("#"*50, end="\n\n\n")
                    for n, c in zip(names, checks):
                        if c:
                            counts[n] += 1
            except Exception as e:
                exceptions[e] += 1
    print(sum(exceptions.values()))
    print(total)
    pprint(doc_lengths)
    pprint(counts)
    pprint({k: v/total for k, v in counts.items()})
fout.close()
