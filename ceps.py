from typing import Union

import re

def compare(
    their_cep: str, 
    my_cep: str, 
    resemblance: list[str],
    rules: list[tuple[int, str]] = [
        (0, "region"),
        (1, "subregion"),
        (2, "sector"),
        (3, "subsector"),
        (4, "divison"),
    ],
) -> list[str]:

    rules_len = len(rules)
    if rules_len <= 0 or rules_len > len(their_cep) or rules_len > len(my_cep):
        return resemblance

    (digit, result) = rules[0]
    if not their_cep[digit] == my_cep[digit]:
        return resemblance

    resemblance.append(result)
    return compare(their_cep, my_cep, resemblance, rules[1:])


def valid(cep: Union[str, None], validator = re.compile(r'(\d){5}(\d){3}')):
    return cep is not None and validator.match(cep)