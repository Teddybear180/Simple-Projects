def arithmetic_arranger(problems, show_answers = True):
    # prepare lists to hold the parts of the equation
    part1 = []
    part2 = []
    dashes = []
    answers = []
    
    # create error exceptions
    # list cannot contain more than 5 problems
    if len(problems) > 5:
        return('Error: Too many problems.')
    
    # problems must have either + or - operators
    for problem in problems:
        if not ('+' or '-' not in problem):
            return("Error: Operator must be '+' or '-'.")
            
   
    # split equations to check operands for letters and length
    for problem in problems:
        parts = problem.split()
        for part in parts:
            # if operand is more than 4 digits, error
            if len(part) > 4:
                return('Error: Numbers cannot be more than four digits.')
            # if operand contains chars that are not numbers, error
            if part not in ['+', '-'] and not part.isdigit():
                return('Error: Numbers must contain only digits.')
                

    # process each problem 
    for problem in problems:
        
        # split each problem into its components: operand 1, operator, operand2
        parts = problem.split()
        # unpack parts 
        operand1, operator, operand2 = parts[0], parts[1], parts[2]
        
        # calculate operand length
        max_length = max(len(operand1), len(operand2)) + 2 # adding space forthe operator and one space
        
        # prepare the firstline, second line and dash line 
        part1.append(f'{operand1:>{max_length}}')
        part2.append(f'{operator} {operand2:>{max_length-2}}')
        dashes.append('-' * max_length)
        
        # calculate answers if needed
        if show_answers:
            if operator == '+':
                answer = int(operand1) + int(operand2)
            elif operator == '-':
                answer = int(operand1) - int(operand2)
            answers.append(f'{answer:>{max_length}}')
        
    # combine our lines
    arranged_problems = '    '.join(part1) + '\n' + '    '.join(part2) + '\n' + '    '.join(dashes)
    
    # in answers are shown, add them to the end
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
        
    return arranged_problems
        
        
        
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])) 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
print(arithmetic_arranger)