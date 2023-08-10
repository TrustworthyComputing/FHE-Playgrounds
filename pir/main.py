# Private Information Retrieval

def pir(db, key):
    assert key >= 0 and key < len(db), "Incorrect key."
    return db[key]


def main():
    key = 3
    db = [10, 20, 30, 40, 50, 60, 70, 80]

    print(db)
    elem = pir(db, key)
    print('The element in index', key, 'is', elem)


if __name__ == "__main__":
    main()
