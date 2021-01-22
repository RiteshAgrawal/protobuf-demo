import product_pb2

def main():
    d = open('product_binary', 'rb').read()
    p = product_pb2.ProductResponse()
    p.ParseFromString(d)
    print(p)


if __name__ == '__main__':
    main()
