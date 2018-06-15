#!/usr/local/bin/python

'''
   This program is used to transform the "your_dump_file_name"
   file containing dump data from certain database into a format 
   readable by TOAD. 
   This program was developed as part of a requirement.
'''

__author__ = 'Anushree Kesarwani'
__version__ = '1.0'


INPUT_FILE = 'your_dump_file_name'
OUTPUT_FILE = 'your_dump_file_name_out.txt'
INTERMEDIATE_FILE = 'your_dump_file_name_tmp.txt'

FILE_PATH = '/input/file/path/'
READ_FILE = FILE_PATH + INPUT_FILE
WRITE_FILE = FILE_PATH + OUTPUT_FILE
TMP_FILE = FILE_PATH + INTERMEDIATE_FILE

###########DONOT CHANGE ANYTHING BELOW THIS LINE###########

def transform_for_toad():
        rr = open(TMP_FILE,'rt')
        ww = open(WRITE_FILE, 'a')
        s = len(rr.read())
        rr.seek(0,0)
        data = rr.read()
        i = 0
        j = 86
        #print data[i:j],'\n'
        while(j<=s):
                #print 'i=',i
                #print 'j=',j
                var = data[i:j]
                #print var
                ww.write(var)
                ww.write('\n')
                i = j
                j = j + 86

        rr.close()
        ww.close()
        
def initial_transform():
        with open (READ_FILE,'rt') as in_file, open(TMP_FILE, 'w') as out_file:
                line = in_file.read()
                print line[:86]
                line_minus_header = line[86:]
                in_file.readlines()
                x = in_file.tell()
                out_file.write(line_minus_header)

        f = open(TMP_FILE, 'a')
        f.seek(x)
        f.write('\n')
        f.close()
        in_file.close()
        
		
def main():
        initial_transform()
        transform_for_toad()

if __name__ == '__main__':
        main()
