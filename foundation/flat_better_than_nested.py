def main():
    download_nested()
    download_flat()


# Yuck
def download_nested():
    print("Lets download a file")
    if s.check_download_url():
        if s.check_network():
            if s.check_dns():
                if s.check_access_allowed():
                    print("Sweet! we can download...")
                else:
                    print("No-access")
            else:
                print("No DNS")
        else:
            print("No network")
    else:
        print("Bad url")


# Much better
def download_flat():
    print("Lets download a file")
    if not s.check_download_url():
        print("Bad url")
        return

    if not s.check_network():
        print("No network")
        return

    if not s.check_dns():
        print("No DNS")
        return

    if not s.check_access_allowed():
        print("No-access")
        return

    print("Sweet! we can download...")


if __name__ == '__main__':
    main()
