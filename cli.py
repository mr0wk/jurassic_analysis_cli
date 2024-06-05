import click
import pandas as pd

import utils.plot_utils as plot_utils
from utils.read_utils import (
    read_dinosaurs,
    read_dinosaurs_by_properties,
    stringify_dinosaur,
)


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--property-value",
    "-pv",
    "property_value_pairs",
    help="Filter dinosaurs by property-value pairs.",
    multiple=True,
    nargs=2,
)
@click.option(
    "--sort-by",
    "-s",
    help="Sort by property.",
    type=click.Choice(
        [
            "name",
            "diet",
            "period",
            "lived_in",
            "type",
            "length",
            "species",
        ]
    ),
)
def read(property_value_pairs: tuple[tuple], sort_by: str):
    if property_value_pairs:
        property_value_dict = dict(property_value_pairs)
        dinosaurs = read_dinosaurs_by_properties(property_value_dict)
    else:
        dinosaurs = read_dinosaurs()

    if sort_by:
        dinosaurs = sorted(dinosaurs, key=lambda dino: dino[sort_by])

    if not dinosaurs:
        click.echo("No dinosaurs found.")
        return

    for dino in dinosaurs:
        click.echo(stringify_dinosaur(dino))


@cli.command()
@click.option(
    "--name",
    "-n",
    help="Name of the plot to generate.",
    type=click.Choice(
        [
            "bar_plot_diet",
            "bar_plot_period",
            "scatter_plot_length",
            "histogram_dinosaur_lengths",
            "pie_chart_country_lived_in",
        ]
    ),
)
def plot(name: str):
    dinosaurs = read_dinosaurs()
    df = pd.DataFrame(dinosaurs)

    plot_func = getattr(plot_utils, name)
    plot_func(df)


if __name__ == "__main__":
    cli()
