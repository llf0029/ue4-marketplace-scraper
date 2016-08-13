# Use sys to get command line arguments, and getopt to parse them
import sys
import getopt

import um_cmd
import um_controller
import um_view
import data_util
import analysis_util


def main(args):
    v = um_view.UmView()
    d = data_util.DataUtil()
    a = analysis_util.AnalysisUtil()
    c = um_controller.UMController(v, d, a)
    
    if not args == []:
        try:
            opts, args = getopt.getopt(args, "hs:c:", ["help", "search=", "category="])
        except getopt.GetoptError:
            usage()
            sys.exit(2)

        # Handle args
        for opt, arg in opts:
            if  opt in ("-h", "--help"):
                usage()
                sys.exit()
            elif opt in ("-s", "--search"):
                c.search(arg)
            elif opt in ("-c", "--category"):
                c.category(arg)
            else:
                print ('ELSE>>>>>>')
    else:
        cmd = um_cmd.UmCmd(c)
        cmd.start()

    
def usage():
    """Displays usage help documentation"""
    print ('Usage: {} [-h] [-s QUERY | -c CATEGORY]'.format(sys.argv[0]))
    print ("\nOptional arguments:")
    print ("  -h, --help                show this help message")
    print ("  -s, --search QUERY        search marketplace by keyword")
    print ("  -c, --category CATEGORY   search marketplace by category")
    print ("\nOr run __main__.py without arguments to enter interactive mode.")


    
if __name__ == '__main__':
    main(sys.argv[1:])
