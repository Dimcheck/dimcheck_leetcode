def encode_old(strs: list[str]) -> str:
    if not strs:
        return ""

    encode_result = []
    len_s, idx = [len(s) for s in strs], 0

    while idx != len(strs):
        encode_result.append(str(len_s[idx]) + "#" + strs[idx])
        idx += 1

    return "#".join(encode_result)


def encode(strs: list[str]) -> str:
    return ''.join(
        f'{len(string)}#{string}'
        for string in strs
    )


def decode_old(s: str) -> list[str]:
    if s != "":
        strs = s.split(sep="#")
        [strs.remove(x) for x in strs if x.isdigit()]
        return strs
    return []


def decode(s: str) -> list[str]:
    if s != "":
        res, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            # print(s[j])
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res

    return []



print(encode(["neet","code","love","you"]))
print(decode(encode(["neet","code","love","you"])))

print(encode([]))
print(decode(encode([])))

print(encode(["we","say",":","yes","!@#$%^&*()"]))
print(decode((encode(["we","say",":","yes","!@#$%^&*()"]))))

print(encode(["we", "say", ":", "yes"]))
print(decode(encode(["we", "say", ":", "yes"])))