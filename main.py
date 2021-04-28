from pyshorteners import Shortener

ACCESS_TOKEN = "09db4f13704ba6b5204607caab3a67dbe53ab428"


def short(address):
    return Shortener().tinyurl.short(address)


def expand(address):
    return Shortener().tinyurl.expand(address)


def main():
    long_url = input("Enter a Address: ")
    shortened = short(long_url)
    print(shortened)

    ## Expand A Short Url
    already_shortened = input("Enter a Shortened version or press 'P' to use previously shortened address: ").upper()
    if already_shortened == "P":
        already_shortened = shortened

    print(expand(already_shortened))






if __name__ == '__main__':
    main()
