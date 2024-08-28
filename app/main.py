from pyurbandict import UrbanDict

def main():
    word = UrbanDict("python")
    results = word.search()
    print(results[0])

if __name__ == "__main__":
    main()