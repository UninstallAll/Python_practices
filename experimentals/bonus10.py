while True:
    try:
        width = float(input("Width: "))
        length = float(input("Length: "))
        if width == length:
            exit('This is a fucking square!')

        area = width * length
        print(area)
    except ValueError:
        print('please give me a fucking number not text!')
        continue