import pickle


def main():
    test_dict = {
        "key1": 1,
        "key2": 2,
    }
    f = open('pickle_data', 'wb')
    pickle.dump(test_dict, f)
    f.close()


if __name__ == '__main__':
    main()

