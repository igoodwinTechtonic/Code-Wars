def who_eats_who(zoo: str):
    eats = [
      ("antelope", "grass"),
      ("big-fish", "little-fish"),
      ("bug", "leaves"),
      ("bear", "fish"),
      ("bear", "bug"),
      ("bear", "chicken"),
      ("bear", "cow"),
      ("bear", "leaves"),
      ("bear", "sheep"),
      ("chicken", "bug"),
      ("cow", "grass"),
      ("fox", "chicken"),
      ("fox", "sheep"),
      ("giraffe", "leaves"),
      ("lion", "antelope"),
      ("lion", "cow"),
      ("panda", "leaves"),
      ("sheep", "grass"),
    ]
    things = zoo.split(',')
    output = []
    for i, v in enumerate(things):
        # If the first thing can't eat anything, skip it
        left = [idx for idx, tup in enumerate(eats) if tup[0] == v]
        if (len(left) == 0): continue

        # Looks left first, then right
        if (i != 0):
            lookLeft = [
              idx for idx, tup in enumerate(eats)
              if (tup[1] == things[i - 1])
            ]
            print(lookLeft)
            # eatsLeftIdx = [idx for idx in left if idx in lookLeft]
            # if (len(eatsLeftIdx) != 0):
            #     print(f"{eats[eatsLeftIdx[0]][0]} eats {eats[eatsLeftIdx[0]][1]}")
            #     things.remove(eats[eatsLeftIdx[0]][1])
            #     return who_eats_who(''.join(things))

        if (i < (len(things) - 1)):
            lookRight = [idx for idx, tup in enumerate(eats) if tup[1] == things[i + 1]]
            print(lookRight)
            # eatsRightIdx = [idx for idx in left if idx in lookRight]
            # if (len(eatsRightIdx) != 0):
            #     print(f"{eats[eatsRightIdx[0]][0]} eats {eats[eatsRightIdx[0]][1]}")
            #     things.remove(eats[eatsRightIdx[0]][1])
            #     return who_eats_who(''.join(things))

        # If there are intersecting indices
        # eatsIdx = [idx for idx in left if idx in right]
        # if (len(eatsIdx) != 0):
        #     eatsIdx[0]
        # print(left, lookLeft, lookRight)


    # return output

# who_eats_who("fox,bug,chicken,grass,sheep")
print(who_eats_who("bug,leaves,cow,bear"))

"""
    antelope eats grass
    big-fish eats little-fish
    bug eats leaves
    bear eats big-fish
    bear eats bug
    bear eats chicken
    bear eats cow
    bear eats leaves
    bear eats sheep
    chicken eats bug
    cow eats grass
    fox eats chicken
    fox eats sheep
    giraffe eats leaves
    lion eats antelope
    lion eats cow
    panda eats leaves
    sheep eats grass

INPUT: A comma-separated string representing all the things at the zoo

TASK: Figure out who eats whom until no more eating is possible.

OUTPUT: 

A list of strings (refer to the example below) where:
    The first element is the initial zoo (same as INPUT)
    The last element is a comma-separated string of what the zoo looks like when all the eating has finished
    All other elements (2nd to last-1) are of the form X eats Y describing what happened

Notes:
    Animals can only eat things beside them
    Animals always eat to their LEFT before eating to their RIGHT
    Always the LEFTMOST animal capable of eating will eat before any others
    Any other things you may find at the zoo (which are not listed above) do not eat anything and are not edible
"""

    # for i in things:
        # # grabs position of things in zoo list
        # idx = things.index(i)
        # # If the first thing in the list, look right
        # if (idx == 0):
        #     try:
        #         # If the index matches, remove thing and call recursion
        #         if (left.index(i) == right.index(things[1])):
        #             print(who_eats_who(','.join(filter(lambda x: x != things[1], things))))
        #             return f"{i} eats {things[1]}"
        #     except (ValueError, IndexError): continue
        # # If not the first thing in the list, look left first
        # else:
        #     try:
        #         print(left.index(i), right.index(things[idx - 1]))
        #         if (left.index(i) == right.index(things[idx - 1])):
        #             print(who_eats_who(','.join(filter(lambda x: x != things[idx - 1], things))))
        #             return f"{i} eats {things[idx - 1]}"
        #         elif (left.index(i) == right.index(things[idx + 1])):
        #             print(who_eats_who(','.join(filter(lambda x: x != things[idx + 1], things))))
        #             return f"{i} eats {things[idx + 1]}"
        #     except (ValueError, IndexError): continue