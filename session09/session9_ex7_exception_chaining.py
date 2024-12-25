# Save as: session9_ex7_exception_chaining.py
def process_data(data):
    # TODO:
    # 1. if len(data) == 0, raise ValueError
    # 2. if not isinstance(data, list), raise TypeError
    # 3. else return "Data processed"
    if len(data) == 0:
        raise ValueError("No data provided")
    
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    
    return "Data processed"

def caller(data):
    try:
        return process_data(data)
    except (ValueError, TypeError) as e:
        raise RuntimeError("Data processing failed") from e

def main():
    # 1. try:
    #     - ask user whether to pass an empty list, non-list, or normal list
    #     - call process_data(...) 
    #    except (ValueError, TypeError) as e:
    #        raise RuntimeError("Data processing failed") from e
    # 2. also wrap main in another try to catch that RuntimeError and print chain

    try:
        print(caller([]))
    except RuntimeError as e:
        print("Error:", e)

    try:
        print(caller((1, 2)))
    except RuntimeError as e:
        print("Error:", e)

    try:
        print(caller([1, 2]))
    except RuntimeError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()