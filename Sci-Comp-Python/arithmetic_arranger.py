def padding(string, req_length, pattern=' '):
    padding_str = ''
    for i in range(req_length - len(string)):
        padding_str += pattern
    return padding_str + string

def arithmetic_arranger(problems, show_answers=False):
    lines = {}
  
    # If too many problems:
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # For each problem:
    for problem in problems:
        # Parse operator & digits
        parsed = []
        operator = '+'
        parsed = problem.split(' + ')
        if len(parsed) == 1:
            operator = '-'
            parsed = problem.split(' - ')

        if len(parsed) == 1:
            return "Error: Operator must be '+' or '-'."

        # Set variables, check valid
        left_digit, right_digit = parsed[0], parsed[1]

        if not left_digit.isnumeric() or not right_digit.isnumeric():
            return 'Error: Numbers must only contain digits.'
        left_digit, right_digit = int(left_digit), int(right_digit)
        
        answer = None
        if show_answers:
            answer = left_digit + right_digit if operator == '+' else left_digit - right_digit

        # Count length for format
        left_digit_len = len(str(left_digit))
        right_digit_len = len(str(right_digit))

        if left_digit_len > 4 or right_digit_len > 4:
            return 'Error: Numbers cannot be more than four digits.'

        length_with_op = 0
        if left_digit_len > right_digit_len:
            length_with_op = left_digit_len + 2
        else:
            length_with_op = right_digit_len + 2

        left_digit_str = padding(str(left_digit), length_with_op)
        right_digit_str = padding(str(right_digit), length_with_op - 2)
        answer_str = show_answers and padding(str(answer), length_with_op)

        lines[problem] = [
            left_digit_str,
            operator + " " + right_digit_str,
            padding('', length_with_op, '-'),
        ]
        if show_answers:
            lines[problem].append(answer_str)
    
    # Combine lines
    output_lines = {}
    for problem in lines:
        index = 0
        for line in lines[problem]:
            if not index in output_lines:
                output_lines[index] = line
            else:
                output_lines[index] += "    " + line
            
            index += 1

    result_string = ''
    for line in output_lines:
        result_string += output_lines[line] + "\n"
    return result_string[:-1]

def test():
    print(f'{arithmetic_arranger(["3801 - 2", "123 + 49"])}')

test()
