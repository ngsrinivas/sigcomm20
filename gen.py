#!/usr/bin/python

header_file = 'header'
footer_file = 'footer'
data_folder = 'data-files/'
stage_folder = 'staging/sigcomm/2020/'

# Add list of files to generate here
data_files = ['index',
              'cfp',
              'cf-workshops',
              'tpc',
              'org-committee',
              'cf-tutorials',
              'submission',
              'workshop-spin',
              'workshop-mantra',
              'workshop-netai',
              'workshop-nai',
              'workshop-hotedgevideo',
              'workshop-optsys',
              'workshop-epiq',
              'camera-ready_ws',
              'tutorial-scion',
              'tutorial-mptp',
              'tutorial-aarp',
              'tutorial-pins',
              'tutorial-netfinance',
              'camera-ready',
              'cf-posters',
              'tutorial-quic',
              'n2women']

def read_file(fname):
    with open(data_folder + fname + '.html', 'r') as f:
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
