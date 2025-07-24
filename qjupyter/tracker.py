# qjupyter/tracker.py

import matplotlib.pyplot as plt


class MetricTracker:
    """
    Tracks training metrics like loss, accuracy, fidelity, etc.
    """

    def __init__(self):
        self.history = {}

    def log(self, metric_name, value):
        """
        Log a new value to a given metric.

        Args:
            metric_name (str): Name of the metric (e.g., 'loss', 'fidelity')
            value (float): Value to log
        """
        if metric_name not in self.history:
            self.history[metric_name] = []
        self.history[metric_name].append(value)

    def get(self, metric_name):
        """
        Retrieve the list of values for a metric.

        Args:
            metric_name (str): Metric name

        Returns:
            List[float]: All logged values
        """
        return self.history.get(metric_name, [])

    def plot(self, save_path=None):
        """
        Plot all tracked metrics.

        Args:
            save_path (str, optional): If provided, saves the plot to this file
        """
        plt.figure(figsize=(10, 6))
        for metric, values in self.history.items():
            plt.plot(values, label=metric)

        plt.xlabel("Epoch")
        plt.ylabel("Metric Value")
        plt.title("Training Metrics")
        plt.legend()
        plt.grid(True)

        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

    def reset(self):
        """Clear all logged metrics."""
        self.history = {}
