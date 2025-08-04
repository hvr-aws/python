def display(name):
    def message():
        return " Hellow "
    result= message()+name
    return result

print(display("Harsha"))