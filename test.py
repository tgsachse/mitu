#!/usr/bin/env python3
import utils

template_right = utils.generate_template(align='right', fill_char='', width=20)
template_center = utils.generate_template(align='center', fill_char='', width=30)
templates = [template_right, template_right, template_center, template_center]
strings = ['abcdeffffffffffffffffffffffffffffffffffffffffffffffff',
            'hfffffffffffffffffffffffffffffffffffffffffffffffffi',
            'dddddddddddddddddddddddddddddddddddddddddddddddleetcode',
            'yffffffffffffffffffffffffffffffffffffffffffffffffffffaya']
spacing = [20, 10, 10, 10]
utils.rprint(templates, strings, spacing, color='blue')
print(utils.confirm_input())
utils.rinput('rekme', ['^k+'], escape=['p', 'pp'], invalid='rekt', regex=True)
