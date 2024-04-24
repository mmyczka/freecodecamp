def arithmetic_arranger(problems, show_answers=False):
    if error:= check_problems(problems):
        return error
    return format_problems(problems, show_answers)

# Format problems
def format_problems(problems, show_answers):
    # Get components and results of a problem
    components = [problem.split() + [str(eval(problem))] for problem in problems]
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    # Format lines
    for component in components:
        # Line width is the maximum length of the first and last component plus 2 for operator and space
        line_width = max(len(component[0]), len(component[2])) + 2
        line1 += component[0].rjust(line_width) + "    "
        line2 += component[1] + component[2].rjust(line_width - 1) + "    "
        line3 += "-" * (line_width) + "    "
        line4 += component[3].rjust(line_width) + "    "
    
    # Return formatted problems
    return line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() + ('\n' + line4.rstrip() if show_answers else "")


# Check if the number of problems is greater than 5
def check_problem_count(problems):
    return len(problems) > 5

# Check if there are operators '*' or '/' in problems
def check_operators(problems):
    return any(
        '*' in problem or '/' in problem 
        for problem in problems
    )

# Check if numbers contains something else than digits
def check_numbers(problems):
    for problem in problems:
        for i, number in enumerate(problem.split()):
            if not number.isdigit() and i != 1:
                return True
    return False

# Check if numbers are bigger than four digits in width
def check_numbers_len(problems):
    for problem in problems:
        for i, number in enumerate(problem.split()):
            if len(number) > 4 and i != 1:
                return True
    return False

# Check if any of the errors occurred
def check_problems(problems):
    if check_problem_count(problems):
        return "Error: Too many problems."
    if check_operators(problems):
        return "Error: Operator must be '+' or '-'."
    if check_numbers(problems):
        return "Error: Numbers must only contain digits."
    if check_numbers_len(problems):
        return "Error: Numbers cannot be more than four digits."


print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')