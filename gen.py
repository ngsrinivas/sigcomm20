#!/usr/bin/python

import subprocess

header_file = 'header'
footer_file = 'footer'
data_folder = 'data-files/'
stage_folder = 'staging/sigcomm/2020/'
gen_script = 'gen.sh'

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
              'camera-ready_ws',
              'tutorial-scion',
              'tutorial-mptp',
              'tutorial-aarp',
              'tutorial-netfinance',
              'camera-ready',
              'cf-posters',
              'tutorial-quic',
              'content-forthcoming',
              'supporters']

templated_files = {'program': 'main-program',
                   'workshop-optsys' : 'optsys-program',
                   'workshop-epiq': 'epiq-program',
                   'workshop-hotedgevideo': 'hotedgevideo-program',
                   'n2women': 'n2women-program',
                   'workshop-netai': 'netai-program',
                   'workshop-nai': 'nai-program'}

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

for f in templated_files.keys():
    script_folder = templated_files[f]
    cmd = "cd %s%s ; sh %s ; cd -" % (
        data_folder, script_folder, gen_script)
    print cmd
    subprocess.call(cmd, shell=True)
    data = read_file(f)
    write_file(f, header + data + footer)
