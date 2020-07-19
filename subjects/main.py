import Hello.gen
import Palindrome.gen
import Hopcroft_Karp.gen
import Words.gen
import Convex_Hull.gen
import Mediane.gen
import Cycle.gen
import Roads.gen
import Polygons.gen
import RainbowRider.gen
import LesserPath.gen
import Rect.gen

import sys

def log(l):
    print(l, file=sys.stderr)

def translate_html(html_code):
    data = [("'", "''")]

    for (a, b) in data:
        html_code = html_code.replace(a, b)

    return (html_code)

def main():
    problems = []
    tests = []

    data = []

    log("Generate dataset for Hello")
    data.append(Hello.gen.gen())

    log("Generate dataset for Words")
    data.append(Words.gen.gen())

    log("Generate dataset for Palindrome")
    data.append(Palindrome.gen.gen())

    log("Generate dataset for Hopcroft_Karp")
    data.append(Hopcroft_Karp.gen.gen())

    log("Generate dataset for Convex_Hull")
    data.append(Convex_Hull.gen.gen())

#    log("Generate dataset for Rect")
#    data.append(Rect.gen.gen())

    log("Generate dataset for Mediane")
    data.append(Mediane.gen.gen())

    log("Generate dataset for Cycle")
    data.append(Cycle.gen.gen())

    log("Generate dataset for Roads")
    data.append(Roads.gen.gen())

    log("Generate dataset for Polygons")
    data.append(Polygons.gen.gen())

    log("Generate dataset for RainbowRider")
    data.append(RainbowRider.gen.gen())

    log("Generate dataset for LesserPath")
    data.append(LesserPath.gen.gen())

    counter = 1
    for d in data:
        (name, description, difficulty, dataset) = d
        problems.append((name, description, difficulty))
        tests.append((dataset, counter))
        counter = counter + 1

    for p in problems:
        (name, description, difficulty) = p

        description = translate_html(description)

        print("insert into problems(problem_name, problem_description, problem_difficulty)")
        print("values('%s', '%s', %d);" % (name, description, difficulty))
        print()

    for dataset in tests:
        (li, counter) = dataset

        for test in li:
            (i, o, time, point) = test

            print("insert into tests(test_in, test_out, test_time, test_points, problem_id)")
            print("values('%s', '%s', %d, %d, %d);" % (i, o, time, point, counter))
            print()

if __name__ == "__main__":
    main()
