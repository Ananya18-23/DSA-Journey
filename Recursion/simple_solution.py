# print four times ananya 
def func(count):
    if count == 4:
        return

    print("Ananya")
    func(count + 1)

func(0)