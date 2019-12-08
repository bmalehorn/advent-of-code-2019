import math
from collections import defaultdict, deque
from aoc import parse, flatten, pp, uniqc, trace, permutations
import aoc


def read(mem, posdata, eip, index):
    val = mem[eip + index]
    for i in range(index - 1):
        posdata //= 10
    if posdata % 10 == 0:
        assert val >= 0
        return mem[val]
    elif posdata % 10 == 1:
        return val
    else:
        raise Exception(
            "read(%r, %r, %r, %r) has bad posdata %r" % (mem, posdata, val, i, posdata)
        )


def step(mem, eip, input):
    assert eip >= 0
    a = mem[eip]
    opcode = a % 100
    posdata = a // 100
    output = None
    pulled_input = False

    def r(index):
        return read(mem, posdata, eip, index)

    def w(mem_index, val):
        assert mem_index >= 0
        assert mem[mem_index] >= 0
        mem[mem[mem_index]] = val

    if opcode == 1:
        w(eip + 3, r(1) + r(2))
        eip += 4

    elif opcode == 2:
        w(eip + 3, r(1) * r(2))
        eip += 4

    elif opcode == 3:
        # print("input %r" % input)
        pulled_input = True
        w(eip + 1, input)
        eip += 2

    elif opcode == 4:
        output = r(1)
        # print("output %r" % output)
        eip += 2

    elif opcode == 5:
        param = r(1)
        val = r(2)
        if param != 0:
            eip = val
        else:
            eip += 3

    elif opcode == 6:
        if r(1) == 0:
            eip = r(2)
        else:
            eip += 3

    elif opcode == 7:
        if r(1) < r(2):
            w(eip + 3, 1)
        else:
            w(eip + 3, 0)
        eip += 4

    elif opcode == 8:
        if r(1) == r(2):
            w(eip + 3, 1)
        else:
            w(eip + 3, 0)
        eip += 4

    elif opcode == 99:
        print("halt")
        eip = None

    else:
        raise Exception("bad opcode %r" % opcode)

    return eip, output, pulled_input


# That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 638506.)

# 262086
def part1():
    pp(best_sequence([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]))

    pp(
        best_sequence(
            [
                3,
                23,
                3,
                24,
                1002,
                24,
                10,
                24,
                1002,
                23,
                -1,
                23,
                101,
                5,
                23,
                23,
                1,
                24,
                23,
                23,
                4,
                23,
                99,
                0,
                0,
            ]
        )
    )
    pp(
        best_sequence(
            [
                3,
                31,
                3,
                32,
                1002,
                32,
                10,
                32,
                1001,
                31,
                -2,
                31,
                1007,
                31,
                0,
                33,
                1002,
                33,
                7,
                33,
                1,
                33,
                31,
                31,
                1,
                32,
                31,
                31,
                4,
                31,
                99,
                0,
                0,
                0,
            ]
        )
    )
    mem = flatten(parse("07.txt"))
    pp(best_sequence(mem))


def best_sequence(mem):
    best_input_signal = 0
    for phase in permutations([0, 1, 2, 3, 4]):
        input_signal = 0
        for i in range(len(phase)):
            input_signal = doit(mem, phase[i], input_signal)
        if best_input_signal < input_signal:
            best_input_signal = input_signal
            best_phase = phase
    return best_input_signal, best_phase


def doit(mem, phase_setting, input_signal):
    mem = mem[:]
    eip = 0
    state = "phase"
    while eip is not None:
        if state == "phase":
            eip, output, pulled_input = step(mem, eip, input=phase_setting)
            if pulled_input:
                state = "signal"
        elif state == "signal":
            eip, output, pulled_input = step(mem, eip, input=input_signal)
            if output is not None:
                return output
    assert False


def part2():
    # mem = flatten(parse("07.txt"))
    # pp(best_sequence2(mem))
    pp(
        best_sequence2(
            [
                3,
                26,
                1001,
                26,
                -4,
                26,
                3,
                27,
                1002,
                27,
                2,
                27,
                1,
                27,
                26,
                27,
                4,
                27,
                1001,
                28,
                -1,
                28,
                1005,
                28,
                6,
                99,
                0,
                0,
                5,
            ]
        )
    )


def doit2(mem, phase_setting, input_signal):
    mem = mem[:]
    eip = 0
    state = "phase"
    while eip is not None:
        if state == "phase":
            eip, output, pulled_input = step(mem, eip, input=phase_setting)
            if pulled_input:
                state = "signal"
        elif state == "signal":
            eip, output, pulled_input = step(mem, eip, input=input_signal)
            if output is not None:
                return output
    return None


def best_sequence2(mem):
    best_input_signal = 0
    for phase in permutations([5, 6, 7, 8, 9]):
        input_signal = 0
        while True:
            # BUG: Provide each amplifier its phase setting at its first input instruction; all further input/output instructions are for signals.
            # instead, I re-use the phase here
            # All signals sent or received in this process will be between pairs of amplifiers except the very first signal and the very last signal. To start the process, a 0 signal is sent to amplifier A's input exactly once.
            halt = False
            for i in range(len(phase)):
                res = doit2(mem, phase[i], input_signal)
                if res is None:
                    halt = True
                    print('@@@ output')
                    break
                input_signal = res
            if halt:
                break
        if best_input_signal < input_signal:
            best_input_signal = input_signal
            best_phase = phase
    return best_input_signal, best_phase


part2()
