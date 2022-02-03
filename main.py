from vrms import Background


def main() -> None:
    b = Background()
    b.listen()
    b.close()


if __name__ == "__main__":
    main()
