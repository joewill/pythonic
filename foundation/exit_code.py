import time
import sys


def main():
    confirm = input(
        "Are you sure you want to format your hard drive? [yes, no] ")
    if not confirm or confirm.lower() != 'yes':
        print("Format cancelled")
        # let the consumer of the program know if the program succeeded or failed
        # 0 means everything is good to go, non-zero means something went wrong
        sys.exit(1)

    for _ in range(40):
        time.sleep(.15)
        print('.', end='')
        sys.stdout.flush()
    print()
    print("Format completed. Enjoy your new hard drive space")


main()
