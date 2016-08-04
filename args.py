#--------------------------------#
# Testing command line arguments #
#--------------------------------#

# Use sys to get command line arguments, and getopt to parse them
import sys
import getopt


def parse_command_line_args(argv):
    """Parses command line arguments"""
    # Get opts and args
    try:
        opts, args = getopt.getopt(argv, "hs:c:", ["help", "search=", "category="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    # Handle opts and args
    for opt, arg in opts:
        if  opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-s", "--search"):
            url = "https://www.unrealengine.com/marketplace/assets?lang=&q={}".format(arg)
            print (url)
        elif opt in ("-c", "--category"):
            url = "https://www.unrealengine.com/marketplace/content-cat/assets/{}".format(arg)
            print (url)
        else:
            url = "https://www.unrealengine.com/marketplace/content-cat/assets/recent"
            print (url)

    print ("parsing complete")


def usage():
    """Displays usage help documentation"""
    print ('Usage: {} [-h] [-s QUERY | -c CATEGORY]'.format(sys.argv[0]))
    print ()
    print ("Optional arguments:")
    print ("  -h, --help                show this help message")
    print ("  -s, --search QUERY        search marketplace by keyword")
    print ("  -c, --category CATEGORY   search marketplace by category")
    print ()


parse_command_line_args(sys.argv[1:])

