import app



#This file will manage the main logic, track the Activity classes and call functions from the timing and app files
def main_app():
    #move this function to a different .py file. Have the .app be only for rendering app windows.
    file = ''
    while True:
        # home_window returns 'change' to change the save directory
        # 'modify' to change settings
        # 'tracking' to start tracking
        # 'log' to view the log
        output = home_window()
        if output == 'change':
            file = file_path_window()
            break
        elif output == 'modify':
            activity1, activity2, activity3 = settings_window("One", "Two", "Three")
            break
        elif output == 'log':
            log_window()
            break
        elif output == 'export':
            export_window()
            break
        elif output == 'tracking':
            tracking_window()
            break

    #if file == '':
    #    file = file_path_window()

    print(file)
    return True


def main():
    while True:
        app.main_app()


if __name__ == '__main__':
    main()