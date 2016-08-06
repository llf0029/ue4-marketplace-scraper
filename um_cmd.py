# Imports
import cmd

# Class definition
class UmCmd(cmd.Cmd):
    intro = 'Welcome to the Unreal Engine 4 Marketplace scraper app.\n' + \
            'Type help or ? to list commands.\n'
    prompt = 'UE4 Marketplace>'
    
    def __init__(self, controller):
        self.controller = controller    # Set controller
        cmd.Cmd.__init__(self)          # Run main init method

    def start(self):
        self.cmdloop()


    # -------- App Commands --------
    def do_search(self, arg):
        """Find marketplace items by keyword(s):    SEARCH fire effects"""
        self.controller.search(arg)

    def do_category(self, arg):
        """Find marketplace items by category:      CATEGORY blueprints"""
        self.controller.category(arg)

    def do_view_asset_image(self, arg):
        """Displays the image of the chosen asset:  VIEW_ASSET_IMAGE 4"""
        self.controller.display_asset_image(arg)

    def do_results(self, arg):
        """Set the number of results to display:    RESULTS 10"""
        self.controller.set_num_of_results(arg)

    def do_save(self, arg):
        """Store the results of the previous query for later use"""
        self.controller.save_last_query()

    def do_load(self, arg):
        """Reload a previously stored query"""
        self.controller.load_stored_query()


    # -------- Misc Commands --------
    def do_exit(self, arg):
        """Exit the Unreal Engine 4 Marketplace scraper app"""
        print ('Shutting down...')
        return True

    def help_help(self):
        print ('Show help documentation for this app')





if __name__ == '__main__':
    import cmd_view
    import data_util
    import um_controller

    v = cmd_view.CmdView()
    d = data_util.DataUtil()
    c = um_controller.UMController(v, d)
    console = UmCmd(c)
    console.start()