# Imports
import cmd

# Class definition
class UmCmd(cmd.Cmd):
    intro = 'Welcome to the Unreal Engine 4 Marketplace scraper app.\n' + \
            'Type help or ? to list commands.\n'
    prompt = 'UE4 Marketplace>'

    categories = [
        'recent', '2d', 'animations', 'archvis', 'blueprints', 'characters', 
        'codeplugins', 'communitysamples', 'environments', 'fx', 'materials',
        'music', 'onsale', 'props', 'showcasedemos', 'soundfx', 'textures',
        'weapons'
    ]
    
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

    def do_analyse_results(self, arg):
        """Compares the prices of the last query's assets"""
        self.controller.analyse_results()

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

    def help_category(self):
        print ('Find marketplace items by category:      CATEGORY blueprints')
        print ('Possible categories:')
        for cat in self.categories:
            print ('  - {}'.format(cat))





if __name__ == '__main__':
    import um_view
    import um_controller
    import data_util
    import analysis_util

    v = um_view.UmView()
    d = data_util.DataUtil()
    a = analysis_util.AnalysisUtil()
    c = um_controller.UMController(v, d, a)
    console = UmCmd(c)
    console.start()
