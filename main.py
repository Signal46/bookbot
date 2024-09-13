
def main():
    path = "//home/ericsignal/workspace/github.com/Signal46/bookbot/books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

main()
