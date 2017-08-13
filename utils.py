#! /usr/bin/env python3
import re
from termcolor import cprint


def confirm_input(prompt="> ", ask="Is this correct? (Y/n)"):
    """
    """
    print(ask)
    valid = ['y', 'Y', 'yes', 'Yes', 'n', 'N', 'no', 'No']

    while True:
        i = rinput(prompt, valid)
        if i in valid[:4]:
            return True
        elif i in valid[4:]:
            return False
        else:
            break


def rinput(prompt, valid, escape=['q'], invalid="Invalid input.", regex=False):
    """
    """

    while True:
        i = input(prompt)

        if regex:
            for pattern in valid:
                if re.search(pattern, i):
                    return i
        elif i in valid:
            return i
        elif i in escape:
            break

        print(invalid)


def generate_template(align='left', fill_char='', width=50):
    """
    """
    alignments = {'left': '<',
                  'right': '>',
                  'center': '^'}
    template = '{{:{fill_char}{align}{width}}}'.format(fill_char=fill_char,
                                                     align=alignments[align],
                                                     width=20)
    return template


def rprint(template, strings, spacing, color=None):
    """
    """
    for each in zip(template, strings, spacing):
        line = each[0].format(each[1][:each[2]], width=each[2])
        if not color:
            print(line, end='')
        else:
            cprint(line, color, end='')
