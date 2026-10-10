#modules
from modules import example as mex
from modules import info

#system
from system import example as sex
from system import help 

#extarnal
import argparse

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('--help', action='store_true')
parser.add_argument('-info', type=str, help='path of file')

args = parser.parse_args()



if args.help:
    help.run()
    sex.test()
    mex.test()

if args.info:
    info.run(args.info)