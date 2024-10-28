try:
    import foo3 as mod
except:
    mod = "cannot import foo3"

def main():
    print( f"foo1 says: {mod}" )


if __name__ == '__main__':
    main()
