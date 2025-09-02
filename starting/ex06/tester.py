from ft_filter import ft_filter


def main():
    print("Running ft_filter tests...\n")

    # 1. Simple numbers
    nums = [1, 2, 3, 4, 5]
    assert list(ft_filter(lambda x: x % 2 == 0, nums)) == \
        list(filter(lambda x: x % 2 == 0, nums))

    # 2. Strings with condition
    words = ["apple", "bee", "cat", "dog", "elephant"]
    assert list(ft_filter(lambda w: len(w) > 3, words)) == \
        list(filter(lambda w: len(w) > 3, words))

    # 3. Empty list
    assert list(ft_filter(lambda x: True, [])) == \
        list(filter(lambda x: True, []))

    # 4. All filtered out
    assert list(ft_filter(lambda x: False, nums)) == \
        list(filter(lambda x: False, nums))

    # 5. Mixed types
    mixed = ["123", "", "abc", " ", "XYZ"]
    assert list(ft_filter(lambda s: s.isalpha(), mixed)) == \
        list(filter(lambda s: s.isalpha(), mixed))

    print("All tests passed")


if __name__ == "__main__":
    main()
