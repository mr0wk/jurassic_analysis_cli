import click
import pandas as pd

import utils.plot_utils as plot_utils
from utils.read_utils import (
    read_dinosaurs,
    read_dinosaurs_by_properties,
    stringify_dinosaur,
)


def validate_output(ctx, param, value):
    if value and not value.endswith(".csv"):
        raise click.BadParameter("Output file must be a csv file.")
    return value


@click.command()
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
@click.option(
    "--plot",
    "-p",
    "plot_name",
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
@click.option(
    "--print-dinosaurs",
    "-pd",
    help="Print the stringified dinosaurs data.",
    is_flag=True,
)
@click.option(
    "--output",
    "-o",
    help="Output csv file name.",
    callback=validate_output,
)
def cli(
    property_value_pairs: tuple[tuple],
    sort_by: str,
    plot_name: str,
    print_dinosaurs: bool,
    output: str,
):
    if property_value_pairs:
        property_value_dict = dict(property_value_pairs)
        dinosaurs = read_dinosaurs_by_properties(property_value_dict)
    else:
        dinosaurs = read_dinosaurs()

    if not dinosaurs:
        click.echo("No dinosaurs found.")
        return

    if sort_by:
        dinosaurs = sorted(dinosaurs, key=lambda dino: dino[sort_by])

    if print_dinosaurs:
        for dinosaur in dinosaurs:
            click.echo(stringify_dinosaur(dinosaur))

    if plot_name:
        df = pd.DataFrame(dinosaurs)
        plot_func = getattr(plot_utils, plot_name)
        plot_func(df)

    if output:
        df = pd.DataFrame(dinosaurs)
        df.to_csv(output, index=False)

    return dinosaurs


if __name__ == "__main__":
    cli()
