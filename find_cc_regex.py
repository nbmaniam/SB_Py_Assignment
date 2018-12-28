import optparse
import re


if __name__ == '__main__':
    parser = optparse.OptionParser('usage%prog -F <CC file>')
    parser.add_option('-F', dest="ccFile", type="string", help = 'Specify file with CC numbers')
    (options, args) = parser.parse_args()
    ccFile = options.ccFile

    if ccFile == None:
        print(parser.usage)
        exit(0)
        
    '''
        1) Open the file with potential credit card numbers, one on each line
        2) For each number, remove any trailing whitespace
        3) Create a regular expression to identify a valid credit card number
        4) Go through the file and print the total number of valid credit card numbers that you've found
    '''
    #### YOUR CODE HERE #####
    ## Open file ccnumbers.txt
    f = open(ccFile)
    lines = f.read().split('\n')
    count = 0
    
    for ccnum in lines:
     #[0-9]{3}-[0-9]{3}-[0-9]{3}-[0-9]{3} - refor xxxx-xxxx-xxxx-xxxx
     #[0-9]{16}  - re for xxxxxxxxxxxxxxxx
     validccnum = (re.findall("^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$", ccnum) or re.findall("^[0-9]{16}$",ccnum))
     if len(validccnum) != 0:
       count = count + 1  
       print (validccnum[0])
       
    print ("Number of Valid CC:" + str(count))
    f.close()  
      
    
