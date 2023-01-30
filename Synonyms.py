import math


def norm(vec):
  sum_of_squares = 0.0
  for x in vec:
    sum_of_squares += vec[x] * vec[x]

  return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
  dot_product = 0
  final_result = 0
  for x in vec1:
    for y in vec2:
      if x == y:
        dot_product += (vec1[x] * vec2[y])
  final_result = dot_product / (norm(vec1) * norm(vec2))
  return final_result


def build_semantic_descriptors(sentences):
  semantic_descriptors = {}
  for each_sentence in sentences:
    list_of_words = []
    for each_word in each_sentence:
      if each_word not in list_of_words:
        list_of_words.append(
          each_word
        )  #if the word isn't already in the list of words, adds each word into list

    for word in list_of_words:  #iterates through each word in sentence (via list)
      if word not in semantic_descriptors:
        semantic_descriptors[word] = {
        }  #dictionary in dictionary - creates empty dictionary for each of the words in list
      for word_1 in list_of_words:
        if word != word_1:  # ensures the value (which is a dictionary) doesn't include the key
          if word_1 not in semantic_descriptors[word]:
            semantic_descriptors[word][
              word_1] = 1  # first time the word is appearing, its count is 1
          else:
            semantic_descriptors[word][
              word_1] += 1  # the word repeats multiple times
  return semantic_descriptors


def build_semantic_descriptors_from_files(filenames):
  for text in filenames:
    text = open(text, encoding = "utf8").read().lower()
    text = text.replace("\n", " ").replace(',', ' ').replace('-', ' ').replace('--', ' ').replace(':', ' ').replace(';', ' ').split('.')
    sentences = []
    for x in range(len(text)):
        text[x] = text[x].split('?')
        for y in range(len(text[x])):
            text[x][y] = text[x][y].split('!')
            for z in range(len(text[x][y])):
                text[x][y][z] = text[x][y][z].split()
                sentences.append(text[x][y][z])
    dictionary = build_semantic_descriptors(sentences)
    return dictionary



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    word = word.lower()
    cosine = 0.0
    res = choices[0]
    case = False
    words = len(choices)

    for index in range(words):
        choices[index] = choices[index].lower()

    for x in semantic_descriptors:
        if x == word:
            case = True
    if not case:
        return res

    for x in choices:
        if x not in semantic_descriptors:
            testing = -1
        else:
            testing = similarity_fn(semantic_descriptors[word],semantic_descriptors[x])
        if testing > cosine:
            if word != x:
                cosine = testing
                res = x
    return res



def run_similarity_test(filename, semantic_descriptors, similarity_fn):
  cor_ans = 0.0

  file = open(filename).read().split("\n")  # puts each line of file into a seperate string
  for line in range(len(file)):
    file[line] = file[line].split()
    if len(file[line]) == 0:
      line -= 1
      del file[line]
      continue
    if file[line][1] == most_similar_word(file[line][0], file[line][2:],semantic_descriptors, similarity_fn):
      cor_ans += 1
  percent = cor_ans / len(file) * 100

  return percent
