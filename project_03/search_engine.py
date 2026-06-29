from collections import defaultdict, Counter
from dataclasses import dataclass
from math import log
from string import punctuation


@dataclass
class SearchResult:
    name: str
    score: float


def split_to_words(text: str) -> list[str]:
    translator = str.maketrans(punctuation, " " * len(punctuation))
    clean_text = text.translate(translator)
    words = clean_text.lower().split()

    return words


class SearchEngine:
    def __init__(self, documents: list[str]) -> None:
        self.inverted_index = defaultdict(list)
        self.words_in_doc = Counter()

        for document in documents:
            with open(document, "r", encoding="utf-8") as file:
                text = file.read()
                words = split_to_words(text)

                self.words_in_doc[document] = len(words)

                for word, count in Counter(words).items():
                    self.inverted_index[word].append((document, count))

    def search(self, query: str) -> list[SearchResult]:
        document_scores = defaultdict(float)

        for word in split_to_words(query):
            if word not in self.inverted_index:
                continue

            doc_count = len(self.words_in_doc)
            doc_count_with_word = len(self.inverted_index[word])
            IDF = log((doc_count + 1) / (doc_count_with_word + 1))

            for document, count in self.inverted_index[word]:
                TF = count / self.words_in_doc[document]
                score = TF * IDF
                document_scores[document] += score

        results = []

        for document, score in document_scores.items():
            result = SearchResult(document, score)
            results.append(result)

        results.sort(key=lambda x: x.score, reverse=True)

        return results


def main():
    docs = ["docs/a.txt", "docs/b.txt"]
    se = SearchEngine(docs)

    print(se.search("Inverted index (DATA STRUCTURE)."))


if __name__ == "__main__":
    main()
