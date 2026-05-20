import random

# A helper to build quotes from a name.

def make_quotes(name):
    return [
        f"{name}, believe in yourself — you are capable of more than you think.",
        f"{name}, small steps every day lead to big results.",
        f"{name}, your potential is endless; keep pushing forward.",
        f"{name}, challenges are opportunities in disguise.",
        f"{name}, progress, not perfection, is the key to success.",
        f"{name}, you are stronger than your toughest day, keep pushing forward.",
        f"{name}, every effort you make today builds your future, don’t stop trying.",
        f"{name}, don’t wait for motivation — create it through action.",
        f"{name}, your dreams are valid; start working on them now.",
        f"{name}, consistency beats talent when talent doesn’t work hard."
    ]


def get_random_quote(name=None, *args, **kwargs):
    """Return a random motivational quote for a name."""
    if name is None:
        name = kwargs.get('name', 'Friend')
    quotes = make_quotes(name)
    return random.choice(quotes)


def main(name=None, *args, **kwargs):
    """Run the motivation generator. Name can be passed in or prompted."""
    if name is None:
        name = input("Enter your name: ").strip() or "Friend"
    print("=== Motivation Generator ===")
    while True:
        print("\n " + get_random_quote(name=name))
        choice = input("Do you want another quote? (y/n): ").strip().lower()
        if choice not in ('y', 'yes'):
            print("Stay motivated! Goodbye and have a great day!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Stay positive! ")