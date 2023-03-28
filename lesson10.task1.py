def oops():
    raise IndexError("Index out of range")

def catch_oops():
    try:
        oops()
    except IndexError as e:
        print(f"Oops! {type(e).__name__}: {str(e)}")

def oops():
    raise KeyError("Key not found")
catch_oops()

