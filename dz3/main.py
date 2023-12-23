result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a must be higher or rivni b")
        if b > 100:
            raise IndexError("b must be higher or rivni 100")
        return a / b
    except ValueError as fi:
        print(f"ValueError: {fi}")
    except IndexError as se:
        print(f"IndexError: {se}")
    except Exception as th:
        print(f"An unexpected error occurred: {th}")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, "invalid_key": 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)