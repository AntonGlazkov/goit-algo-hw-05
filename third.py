import timeit


def boyer_moore_search(text, pattern):
    if pattern == "":
        return 0
    m = len(pattern)
    n = len(text)
    skip = {}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += skip.get(text[i + m - 1], m)
    return -1


def kmp_search(text, pattern):
    if pattern == "":
        return 0
    m = len(pattern)
    n = len(text)

    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp_search(text, pattern):
    if pattern == "":
        return 0
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1

    base = 256
    mod = 10**9 + 7

    pat_hash = 0
    txt_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        pat_hash = (pat_hash * base + ord(pattern[i])) % mod
        txt_hash = (txt_hash * base + ord(text[i])) % mod

    for i in range(n - m + 1):
        if pat_hash == txt_hash and text[i : i + m] == pattern:
            return i
        if i < n - m:
            txt_hash = (txt_hash - ord(text[i]) * h) % mod
            txt_hash = (txt_hash * base + ord(text[i + m])) % mod
            txt_hash = (txt_hash + mod) % mod

    return -1


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def measure_time(func, text, pattern, number=10):
    def run():
        func(text, pattern)
    return timeit.timeit(run, number=number)


def main():
    article1 = read_file("article1.txt")
    article2 = read_file("article2.txt")

    pattern1_exists = "алгоритм"
    pattern1_fake = "вигаданийпідрядокякогонемає"

    pattern2_exists = "рекомендаційної системи"
    pattern2_fake = "новийвигаданийпідрядок"

    algorithms = [
        ("Boyer-Moore", boyer_moore_search),
        ("Knuth-Morris-Pratt", kmp_search),
        ("Rabin-Karp", rabin_karp_search),
    ]

    texts = [
        ("Стаття 1", article1, pattern1_exists, pattern1_fake),
        ("Стаття 2", article2, pattern2_exists, pattern2_fake),
    ]

    for text_name, text, patt_exist, patt_fake in texts:
        print(f"\n{text_name}")
        print(f"  Існуючий підрядок: {patt_exist!r}")
        for name, func in algorithms:
            t = measure_time(func, text, patt_exist)
            print(f"    {name}: {t:.6f} c")

        print(f"  Вигаданий підрядок: {patt_fake!r}")
        for name, func in algorithms:
            t = measure_time(func, text, patt_fake)
            print(f"    {name}: {t:.6f} c")


if __name__ == "__main__":
    main()
