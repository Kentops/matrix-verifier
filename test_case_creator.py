def old_create_test_case(size = 2048):

    output = open("test_case.txt","w")
    output_string = "["
    for i in range(size):
        output_string += "["
        for j in range(size):
            if j != size-1:
                output_string += str((size * i) +j)+","
            else:
                #last one
                output_string+=str((size * i) + j)
        if i != size -1:
            output_string +="],"
        else:
            output_string+="]]"
    output.write(output_string)
    output.close()

def create_test_case(size = 1024):
    #List comprehension avoids calls to append and thus is faster
    doc = open("test_case.txt","w")
    output = [[(size*j) + i for i in range(size)] for j in range(size)]
    doc.write(str(output))
    doc.close()


create_test_case()