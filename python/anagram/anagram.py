def find_anagrams(word, candidates):
    reference = sorted(word.lower())
    anagrams = []

    for candidate in candidates:
        if len(reference) != len(candidate):
            continue

        if candidate.lower() == word.lower():
            continue

        if reference == sorted(candidate.lower()):
            anagrams.append(candidate)

    return anagrams
