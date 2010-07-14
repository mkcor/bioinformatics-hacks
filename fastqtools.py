# Austin G. Davis-Richardson
# harekrishna@gmail.com
# fastqtools - tools for manipulating, filtering and generating statistics
#   from fastq files (generated by Illumina)

# TODO
# - Average quality scores for a read
# - Average quality scores by base for all reads
# - Filter reads based on length, average quality score, minimum quality score

import sys

def main(args):
    ''' Biscuits & Gravy '''
    task = args[1]
    target = args[2]
    yargs = args[3:]

    handle = open(target, 'r')

    if task == 'trim':
        trim(handle, yargs)
    elif task == 'average':
        average(handle, yargs)
    elif task == 'filter':
        filtr(handle, yargs)
    elif task == 'help':
        help(args)
    else:
        usage()

def trim(handle, args):
    print args

def average(handle, args):
    print args
    
def filtr(handle, args):
    print args
    
def help(args):
    task = args[0]
    helps = {
        'all': '',
        'trim': '',
        'average': '',
        'filter': '',
    }
    print helps['task']


def usage():
    print help('all')

if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print "Owwie!"
        quit()