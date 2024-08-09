def camel_case_to_snake_case(input_string: str) -> str:
    result: list[str] = []
    n: int = len(input_string)

    for i, char in enumerate(input_string):
        if char.isupper() and i > 0 and (
                input_string[i - 1].islower() or (i + 1 < n and input_string[i + 1].islower())):
            result.append('_')

        result.append(char.lower())

    return ''.join(result)