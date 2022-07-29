def solution_with_count_and_set(emojis: str) -> dict[str, int]:
    # avec set et count
    emojis_count = {
        emoji: emojis.count(emoji)
        for emoji in set(emojis)
    }
    return emojis_count


def solution_with_counter(emojis: str) -> dict[str, int]:
    from collections import Counter
    
    # avec counter
    emojis_count = Counter(emojis)
    # print(f"{type(emojis_count)=}")
    emojis_count = dict(Counter(emojis))
    return emojis_count


def solution_with_defaultdict(emojis: str) -> dict[str, int]:
    from collections import defaultdict
    
    # avec defaultdict
    emojis_count = defaultdict(int)
    for emoji in emojis:
        emojis_count[emoji] += 1
    return emojis_count

if __name__ == "__main__":
    emojis = "🥳😎🥳🥳😍🥳😍🚀"
    emojis_count_expected = {'🥳': 4, '🚀': 1, '😎': 1, '😍': 2}
    
    for solution in (
        solution_with_count_and_set, 
        solution_with_counter, 
        solution_with_defaultdict
    ):
        emojis_count = solution(emojis)
        assert emojis_count == emojis_count_expected
