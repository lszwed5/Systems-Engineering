def lcs_without_breaks(str1, str2, str1length, str2length, result=0):
    """Returns the length of the given strings' longest common contiguous substring"""
    if str1length == 0 or str2length == 0:
        return result

    if str1[str1length - 1] == str2[str2length - 1]:
        result = lcs_without_breaks(str1, str2, str1length - 1, str2length - 1, result + 1)

    result = max(result, max(lcs_without_breaks(str1, str2, str1length, str2length - 1, 0),
                             lcs_without_breaks(str1, str2, str1length - 1, str2length, 0)))

    return result


def lcs_with_breaks(str1, str2, str1length, str2length):
    """Returns the length of the given strings' longest common substring"""
    if str1length == 0 or str2length == 0:
        return 0
    elif str1[str1length - 1] == str2[str2length - 1]:
        return 1 + lcs_with_breaks(str1, str2, str1length - 1, str2length - 1)
    else:
        return max(lcs_with_breaks(str1, str2, str1length - 1, str2length),
                   lcs_with_breaks(str1, str2, str1length, str2length - 1))


s1 = "konwalia"
s2 = "zawalina"
print(lcs_without_breaks(s1, s2, len(s1), len(s2)))

X = "ApqBCrDsEF"
Y = "tABuCvDEwxFyz"
print(lcs_with_breaks(X, Y, len(X), len(Y)))
