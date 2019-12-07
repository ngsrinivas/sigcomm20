#!/usr/bin/python

header_file = 'header'
footer_file = 'footer'
data_folder = 'data-files/'
stage_folder = 'staging/sigcomm/2020/'

# Add list of files to generate here
data_files = ['index', 'cfp']

def read_file(fname):
    with open(data_folder + fname + '.srhtml', 'r') as f:
        data = f.read()
    return data

def write_file(fname, contents):
    with open(stage_folder + fname + '.html', 'w') as f:
        f.write(contents)

header = read_file(header_file)
footer = read_file(footer_file)

for f in data_files:
    data = read_file(f)
    write_file(f, header + data + footer)
