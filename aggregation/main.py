# Private Aggregation

def aggregate(buckets, votes):
    for v in votes:
        assert v >= 0 and v < len(buckets), "Incorrect key."
        buckets[v] += 1


def main():
    votes = [0, 1, 1, 0, 0, 0, 3, 3]
    buckets = { 0: 0, 1: 0, 2: 0, 3: 0 }

    print(buckets)
    aggregate(buckets, votes)
    print(buckets)


if __name__ == "__main__":
    main()
