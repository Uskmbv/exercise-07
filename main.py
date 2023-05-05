#1

def create_file(filename):
    with open(filename, 'w') as file:
        file.write('Ada, Alan, Isabella, Lizbeth, Abigail, Meltem, Gülcan')
    print('File created successfully!')

create_file('names.txt')


#2

def transform_to_row(input_file, output_file):
    with open(input_file, 'r') as input:
        contents = input.read()

    words = contents.split(',')

    with open(output_file, 'w') as output:
        for word in words:
            output.write(word.strip() + '\n')

    print('Transformation complete!')


transform_to_row('names.txt', 'names_row.txt')

#3

def add_greeting(input_file, output_file):
    with open(input_file, 'r') as input:
        contents = input.read()

    words = contents.split('\n')

    greetings = ['Hello ' + word for word in words]

    greeting_string = '\n'.join(greetings)

    with open(output_file, 'w') as output:
        output.write(greeting_string)

    print('Greetings added!')


add_greeting('names_row.txt', 'greeted_names.txt')

#4

def strip_greeting(input_file, output_file):
    with open(input_file, 'r') as input:
        contents = input.read()

    words = contents.split('\n')

    stripped_words = [word.replace('Hello ', '') for word in words]

    stripped_string = '\n'.join(stripped_words)

    with open(output_file, 'w') as output:
        output.write(stripped_string)

    print('Greetings stripped!')


strip_greeting('greeted_names.txt', 'stripped_names.txt')


#5

def combine_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        contents1 = f1.readlines()
        contents2 = f2.readlines()

        if len(contents1) != len(contents2):
            print("Files must have the same number of lines.")
            return

        with open(output_file, 'w') as output:
            for line1, line2 in zip(contents1, contents2):
                output.write(line1.strip() + " " + line2.strip() + "\n")