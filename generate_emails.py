import argparse
import random
import string


DOMAIN = "@student.bham.ac.uk"


def generate_email() -> str:
    letters = "".join(random.choices(string.ascii_lowercase, k=3))
    num_digits = random.choice([3, 4])
    digits = "".join(random.choices(string.digits, k=num_digits))
    return f"{letters}{digits}{DOMAIN}"


def generate_emails(count: int, output_file: str = "email.txt") -> None:
    with open(output_file, "w", encoding="utf-8") as f:
        for _ in range(count):
            f.write(generate_email() + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate random student email strings and save them to a file."
    )
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=100,
        help="Number of email strings to generate (default: 100)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="emails.txt",
        help="Output file path (default: email.txt)",
    )
    args = parser.parse_args()

    generate_emails(args.count, args.output)
    print(f"Generated {args.count} emails and saved them to {args.output}")


if __name__ == "__main__":
    main()
