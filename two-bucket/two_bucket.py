# # rules
# # keep track of states
# # never reach 0 capacity
# # never reach max capacity


# def measure(bucket_one, bucket_two, goal, start_bucket):
#     states = []
#     if start_bucket == "one":
#         states.append((bucket_one, 0))
#     else:
#         states.append((0, bucket_two))

#     while goal not in states[-1]:
#         if len(states) > 100:
#             raise ValueError("too many loop")

#         action = next_action(states, bucket_one, bucket_two)
#         if len(action) == 0:
#             raise ValueError("no next action")

#         # if len(action) > 1:
#         # print(action)
#         # raise ValueError("too many actions")

#         run_action(states, bucket_one, bucket_two, action[0])

#     print(states)
#     bucket = "one" if states[-1][0] == goal else "two"
#     return (len(states), bucket, states[-1][0] if bucket == "two" else states[-1][1])


# def run_action(states, bucket_one, bucket_two, action):
#     one, two = states[-1]
#     if action == "fill_one":
#         states.append((bucket_one, two))
#     elif action == "fill_two":
#         states.append((one, bucket_two))
#     elif action == "empty_one":
#         states.append((0, two))
#     elif action == "empty_two":
#         states.append((one, 0))
#     elif action == "put_one_in_two":
#         delta = min(one, bucket_two - two)
#         states.append((one - delta, two + delta))
#     elif action == "put_two_in_one":
#         delta = min(two, bucket_one - one)
#         states.append((one + delta, two - delta))
#     else:
#         raise ValueError("unknown action")


# def next_action(states, bucket_one, bucket_two):
#     actions = []
#     if should_fill_one(states, bucket_one, bucket_two):
#         actions.append("fill_one")

#     if should_fill_two(states, bucket_one, bucket_two):
#         actions.append("fill_two")

#     if should_empty_one(states):
#         actions.append("empty_one")

#     if should_empty_two(states):
#         actions.append("empty_two")

#     if should_put_one_in_two(states, bucket_one, bucket_two):
#         actions.append("put_one_in_two")

#     if should_put_two_in_one(states, bucket_one, bucket_two):
#         actions.append("put_two_in_one")

#     return actions


# def should_fill_one(states, bucket_one, bucket_two):
#     _, two = states[-1]  # this is the current state
#     if two == bucket_two:
#         return False  # we will reach full capacity

#     if (bucket_one, two) in states:
#         return False  # we will reach a state explored previously

#     return True


# def should_fill_two(states, bucket_one, bucket_two):
#     one, _ = states[-1]  # this is the current state
#     if one == bucket_one:
#         return False  # we will reach full capacity

#     if (one, bucket_two) in states:
#         return False  # we will reach a state explored previously

#     return True


# def should_empty_one(states):
#     _, two = states[-1]  # this is the current state
#     if two == 0:
#         return False  # we will reach empty capacity

#     if (0, two) in states:
#         return False  # we will reach a state explored previously

#     return True


# def should_empty_two(states):
#     one, _ = states[-1]
#     if one == 0:
#         return False  # we will reach empty capacity

#     if (one, 0) in states:
#         return False  # we will reach a state explored previously

#     return True


# def should_put_one_in_two(states, bucket_one, bucket_two):
#     one, two = states[-1]
#     if two == bucket_two:
#         return False  # two is already full

#     delta = min(one, bucket_two - two)
#     next_one, next_two = one - delta, two + delta
#     if (next_one, next_two) in states:
#         return False  # we will reach a state explored previously

#     return True


# def should_put_two_in_one(states, bucket_one, bucket_two):
#     one, two = states[-1]
#     if one == bucket_one:
#         return False  # one is already full

#     delta = min(two, bucket_one - one)
#     next_one, next_two = one + delta, two - delta
#     if (next_one, next_two) in states:
#         return False  # we will reach a state explored previously

#     return True


def measure(bucket_one, bucket_two, goal, start_bucket):
    visited = set()
    queue = []
    if start_bucket == "one":
        queue.append((bucket_one, 0, 1))
        invalid = (0, bucket_two)
    else:
        queue.append((0, bucket_two, 1))
        invalid = (bucket_one, 0)
    while queue:
        b1, b2, step = queue.pop(0)
        if b1 == goal:
            return step, "one", b2
        if b2 == goal:
            return step, "two", b1

        if (b1, b2) in visited or (b1, b2) == invalid:
            continue
        visited.add((b1, b2))
        # Pouring one bucket into the other bucket until either: a) the first bucket is empty b) the second bucket is full
        queue.append(
            (min(b1 + b2, bucket_one), b2 - (min(b1 + b2, bucket_one) - b1), step + 1)
        )
        queue.append(
            (b1 - (min(b1 + b2, bucket_two) - b2), min(b1 + b2, bucket_two), step + 1)
        )
        # Emptying a bucket and doing nothing to the other.
        queue.append((b1, 0, step + 1))
        queue.append((0, b2, step + 1))
        # Filling a bucket and doing nothing to the other.
        queue.append((bucket_one, b2, step + 1))
        queue.append((b1, bucket_two, step + 1))
    raise ValueError("No Solution Possible")
