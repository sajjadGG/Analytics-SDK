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


class Panel:
    def __init__(self) -> None:
        self.components = []

    def addComponent(self, comp: ViewComponent):
        pass

    def render() -> None:
        pass


class GridPanel(Panel):
    def __init__(self, n_h, n_w) -> None:
        self.number_rows = n_h
        self.number_width = n_w

    def addComponent(self, comp: ViewComponent):
        self.components.append(comp)

    def render() -> None:
        pass


# TODO: auth , profile , ...
class Dashboard:
    def __init__(self, panel: Panel) -> None:
        self.panel = panel

    def addComponent(self, comp: ViewComponent):
        self.panel.components.append(comp)

    def render(self):
        self.panel.render()


# TODO: config of chart required data and type
class Chart(ViewComponent):

    pass


class BarChart(Chart):
    def set_datesource(self, **kwargs):
        self.heights = kwargs["heights"].fetch()
        self.widths = kwargs["widths"].fetch()

    def render(self) -> None:
        plt.bar(self.heights, self.widths)
