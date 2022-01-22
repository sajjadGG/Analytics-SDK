import matplotlib.pyplot as plt

# TODO: dashboard panel organiztion and layout
# TODO: state, datasource


class DataSource:
    def fetch():
        pass


class ViewComponent:
    def __init__(self, datasource: DataSource) -> None:
        self.datasource = datasource

    def set_datesource(self, **kwargs):
        pass

    def render() -> None:
        pass


class Dashboard(ViewComponent):
    def __init__(self, layout) -> None:
        self.viewCompoent = []
        self.layout = layout

    def render(self):
        for v in self.viewCompoent:
            v.render()


# TODO: config of chart required data and type
class Chart(ViewComponent):

    pass


class BarChart(Chart):
    def set_datesource(self, **kwargs):
        self.heights = kwargs["heights"].fetch()
        self.widths = kwargs["widths"].fetch()

    def render(self) -> None:
        plt.bar(self.heights, self.widths)
