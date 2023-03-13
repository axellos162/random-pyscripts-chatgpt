def pseudoIsomorphicSubstrings(s):
    n = len(s)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        substrings = []
        char_indices = {}
        for j in range(i):
            char_indices[s[j]] = char_indices.get(s[j], []) + [j]
        for c1, indices1 in char_indices.items():
            for c2, indices2 in char_indices.items():
                if c1 >= c2:
                    continue
                valid_substrings = []
                for i1 in indices1:
                    for i2 in indices2:
                        if i1 >= i2:
                            continue
                        substring1 = s[i1:i2+1]
                        is_pseudo_isomorphic = False
                        for substring2 in valid_substrings:
                            if len(substring1) == len(substring2):
                                pseudo_isomorphic = True
                                for k in range(len(substring1)):
                                    if substring1[k] != substring2[k] and s[i1+k] == s[i2+k]:
                                        pseudo_isomorphic = False
                                        break
                                if pseudo_isomorphic:
                                    is_pseudo_isomorphic = True
                                    break
                        if not is_pseudo_isomorphic:
                            valid_substrings.append(substring1)
                substrings += valid_substrings
        for j in range(i):
            if s[j:i] == s[i-j-1:i][::-1]:
                dp[i] = max(dp[i], dp[j] + len(substrings))
        dp[i] = max(dp[i], dp[i-1])
        print(dp[i])
    return dp[1:]
