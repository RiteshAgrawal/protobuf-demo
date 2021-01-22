import product_pb2

def main():
    tag = product_pb2.Tag(title='Tag A')
    tag2 = product_pb2.Tag(title='Tag B')
    tags = [tag, tag2]
    p = product_pb2.ProductResponse(id=1, tags=tags)
    bytes_data = p.SerializeToString()
    f = open('product_binary', 'wb')
    f.write(bytes_data)
    f.close()

if __name__ == '__main__':
    main()


