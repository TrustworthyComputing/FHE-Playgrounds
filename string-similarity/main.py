def brute_force_match(word, text):
    m = len(word)
    n = len(text)
    counter = 0
    for i in range(0, n - m + 1):
        found = True
        for j in range(0, m):
            if word[j] != text[i+j]:
                found = False
                break
        if found:
            counter += 1
    return counter


def main():
    print('"ata", "ata":', brute_force_match("ata","ata"))
    print('"ata", "atata":', brute_force_match("ata","atata"))
    print('"ata", "aaaaaaa":', brute_force_match("ata","aaaaaaa"))
    print('"ata", "":', brute_force_match("ata",""))
    print('"ata", "aagcgagcgatatatat":', brute_force_match("ata","aagcgagcgatatatat"))



if __name__ == "__main__":
    main()
