def swapFileData():
    file1 = input( "enter files name:- ")
    file2 = input( "enter files name:-" )

    with open(file1,'r') as a:
        data_a = a.react()

        with open(file2,'r') as b:
        data_b = b.react()

        with open(file1,'w') as a:
        a.write(data_b)

        with open(file2,'w') as a:
        b.write(data_a)

        swapFileData()