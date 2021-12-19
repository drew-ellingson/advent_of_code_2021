from soln import SnailNum

# -------------------- Tests ----------------------

# Explode Tests

assert SnailNum("[[[[[9,8],1],2],3],4]").explode() == "[[[[0,9],2],3],4]"
assert SnailNum("[7,[6,[5,[4,[3,2]]]]]").explode() == "[7,[6,[5,[7,0]]]]"
assert SnailNum("[[6,[5,[4,[3,2]]]],1]").explode() == "[[6,[5,[7,0]]],3]"
assert (
    SnailNum("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]").explode()
    == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
)
assert (
    SnailNum("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]").explode()
    == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
)

assert SnailNum("[[[[[15,2],3]]]]").explode() == "[[[[0,5]]]]"
assert SnailNum("[[2,[[[3,15]]]]]").explode() == "[[5,[[0]]]]"
assert SnailNum("[[10,[[[11,12]],14]]]").explode() == "[[21,[[0],26]]]"


# Split Tests

assert SnailNum("[10]").split() == "[[5,5]]"
assert SnailNum("[11]").split() == "[[5,6]]"
assert SnailNum("[1,[1,12]]").split() == "[1,[1,[6,6]]]"
assert (
    SnailNum("[[[[0,7],4],[15,[0,13]]],[1,1]]").split()
    == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
)


# Reduce Tests

test = SnailNum("[[[[4,3],4],4],[7,[[8,4],9]]]").add(SnailNum("[1,1]"))
assert test.reduce() == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

# Addition Test

add1 = SnailNum("[[[[4,3],4],4],[7,[[8,4],9]]]")
add2 = SnailNum("[1,1]")

assert add1.add(add2).str_rep == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

add1 = SnailNum("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")
add2 = SnailNum("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]")
assert (
    add1.add(add2).str_rep
    == "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"
)

# Bigger Addition Tests


def make_test(fp, output):
    with open(fp) as in_file:
        snail_nums = [SnailNum(x.strip()) for x in in_file.readlines()]

    init = snail_nums[0]
    for x in snail_nums[1:]:
        init.add(x)

    assert init.str_rep == output


make_test("day_18/tests/add_1.txt", "[[[[1,1],[2,2]],[3,3]],[4,4]]")
make_test("day_18/tests/add_2.txt", "[[[[3,0],[5,3]],[4,4]],[5,5]]")
make_test("day_18/tests/add_3.txt", "[[[[5,0],[7,4]],[5,5]],[6,6]]")
make_test(
    "day_18/tests/add_4.txt", "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
)

# Magnitude Tests:

assert SnailNum("1").mag() == 1
assert SnailNum("[9,1]").mag() == 29
assert SnailNum("[[1,2],[[3,4],5]]").mag() == 143
assert SnailNum("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").mag() == 1384
assert SnailNum("[[[[1,1],[2,2]],[3,3]],[4,4]]").mag() == 445
assert SnailNum("[[[[3,0],[5,3]],[4,4]],[5,5]]").mag() == 791
assert SnailNum("[[[[5,0],[7,4]],[5,5]],[6,6]]").mag() == 1137
assert SnailNum("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]").mag() == 3488

# Big Magnitude Test:

make_test(
    "day_18/tests/mag_1.txt",
    "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]",
)

assert (
    SnailNum("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]").mag()
    == 4140
)
