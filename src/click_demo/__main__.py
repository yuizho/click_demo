import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", help="your name", required=True)
def main(count, name):
    for _ in range(count):
        print(f"hello {name}!!!!")
