def generate_numbers():
    i = 0
    while True:
        i += 1
        yield i
        k = yield
        print(k)

if __name__ == "__main__":
    generator = generate_numbers()
    
    item = next(generator)
    print("Recieved in the main script: " + str(item))

    
    generator.send(5)