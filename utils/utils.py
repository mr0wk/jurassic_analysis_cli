import json
import os
import requests
import matplotlib.pyplot as plt

from exceptions import ReaderError, PlotterError

API_URL = os.getenv("API_URL")


class Reader:
    @staticmethod
    def read_dinosaurs_by_properties(property_value_dict: dict):
        try:
            url = f"{API_URL}?"
            for property_name, property_value in property_value_dict.items():
                url += f"{property_name}={property_value}&"

            response = requests.get(url)

            if response.status_code != 200:
                return f"Error: {response.status_code}"

            data = json.loads(response.text)
            return data
        except Exception as e:
            raise ReaderError(f"Error reading dinosaurs by properties: {e}")

    @staticmethod
    def read_dinosaurs():
        try:
            response = requests.get(API_URL)
            data = json.loads(response.text)

            return data
        except Exception as e:
            raise ReaderError(f"Error reading dinosaurs: {e}")


class Plotter:
    @staticmethod
    def bar_plot_diet(df):
        try:
            plt.figure(figsize=(10, 6))
            df["diet"].value_counts().plot(kind="bar")
            plt.title("Number of Dinosaurs by Diet")
            plt.xlabel("Diet")
            plt.ylabel("Count")
            plt.show()
        except Exception as e:
            raise PlotterError(f"Error plotting bar plot by diet: {e}")

    @staticmethod
    def bar_plot_period(df):
        try:
            plt.figure(figsize=(10, 6))
            df["period"].value_counts().plot(kind="bar")
            plt.title("Number of Dinosaurs by Period")
            plt.xlabel("Period")
            plt.ylabel("Count")
            plt.show()
        except Exception as e:
            raise PlotterError(f"Error plotting bar plot by period: {e}")

    @staticmethod
    def scatter_plot_length(df):
        try:
            plt.figure(figsize=(10, 6))
            for diet in df["diet"].unique():
                subset = df[df["diet"] == diet]
                plt.scatter(subset["type"], subset["length"], label=diet)
            plt.title("Length of Dinosaurs by Type and Diet")
            plt.xlabel("Type")
            plt.ylabel("Length")
            plt.legend()
            plt.show()
        except Exception as e:
            raise PlotterError(f"Error plotting scatter plot by length: {e}")

    @staticmethod
    def histogram_dinosaur_lengths(df):
        try:
            plt.figure(figsize=(10, 6))
            df["length"].plot(kind="hist", bins=20)
            plt.title("Distribution of Dinosaur Lengths")
            plt.xlabel("Length")
            plt.ylabel("Frequency")
            plt.show()
        except Exception as e:
            raise PlotterError(f"Error plotting histogram of dinosaur lengths: {e}")

    @staticmethod
    def pie_chart_country_lived_in(df):
        try:
            plt.figure(figsize=(10, 6))
            df["lived_in"].value_counts().plot(kind="pie", autopct="%1.1f%%")
            plt.title("Dinosaurs by Country Lived In")
            plt.ylabel("")  # Hide the y-label
            plt.show()
        except Exception as e:
            raise PlotterError(f"Error plotting pie chart by country lived in: {e}")
