# Synonyms

One type of question encountered in the Test of English as a Foreign Language (TOEFL) is the “Synonym
Question”, where students are asked to pick a synonym of a word out of a list of alternatives. 

For example:
1. vexed 

(a) annoyed
(b) amused
(c) frightened
(d) excited

(Answer: (a) annoyed)


An intelligent system was built to learn how to answer questions. The system approximated the semantic similarity between any pair of words as a measure of the closeness of their meanings. The semantic similarity was computed to answer a TOEFL question by finding the answer with the highest similarity to the given word. The semantic similarity between two words was measured using cosine similarity between their semantic descriptor vectors, which were computed using the co-occurrence of the words in sentences within the text. The semantic descriptor vectors were stored as dictionaries for efficiency, without storing the zeros corresponding to words that did not co-occur with the target word.
