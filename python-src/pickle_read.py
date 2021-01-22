import pickle

def main():
    f = open('pickle_data', 'rb')
    b = pickle.load(f)
    print(b, type(b))
    f.close()


if __name__ == '__main__':
    main()

