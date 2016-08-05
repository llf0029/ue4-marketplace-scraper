#--------------------------------#
# Testing cmd-based interpreter  #
#--------------------------------#

# Use sys to get command line arguments, and getopt to parse them
import cmd

class UmCmd(cmd.Cmd):

    intro = 'Welcome to the Unreal Engine 4 Marketplace scraper app.\n' + \
            'Type help or ? to list commands.\n'
    prompt = 'UE4 Marketplace>'
    completekey = 'Tab'

    def start(self):
        self.cmdloop()

    #--------------------------------#
    # Commands                       #
    #--------------------------------#
    def do_search(self, arg):
        """Find marketplace items by keyword(s):    SEARCH fire effects"""
        print ('Testing search!')
        print (arg)

    def do_category(self, arg):
        """Find marketplace items by category:      CATEGORY blueprints"""
        print ('Testing category')
        print (arg)

    def do_results(self, arg):
        """Set the number of results to display:    RESULTS 5"""
        print ('Testing results setting')
        print (arg)

    def do_exit(self, line):
        """Exit the Unreal Engine 4 Marketplace scraper app"""
        return True

    def help_help(self):
        print ('Show help documentation')


def main():
    console = UmCmd()
    console.start()

if __name__ == "__main__":
    import args
    
    main()