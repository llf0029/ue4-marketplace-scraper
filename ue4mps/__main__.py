import um_cmd
import um_controller

def main(args):
    ctrl = um_controller.UMController()
    cmd = um_cmd.UmCmd(ctrl)
    
    # <<< If args exist
        # <<< Run arg command
    #else:
    cmd.start()
    
    
if __name__ == '__main__':
    main()
