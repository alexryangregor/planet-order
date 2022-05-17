import ipyvuetify as v

from traitlets import HasTraits, Any
from sepal_ui import mapping as sm
from sepal_ui import sepalwidgets as sw
from ipyleaflet import WidgetControl
from ipywidgets import jslink

from component.message import cm
from component import parameter as cp


class DownMap(sm.SepalMap, HasTraits):

    combo = Any(cp.planet_colors[0]).tag(sync=True)

    def __init__(self):

        # create the extra widget
        self.state = sw.StateBar(loading=False)
        self.color = v.ListItemGroup(
            v_model=cp.planet_colors[0],
            children=[v.ListItem(children=[c], value=c) for c in cp.planet_colors[:4]],
        )
        self.palette = v.Menu(
            offset_x=True,
            value=False,
            v_slots=[
                {
                    "name": "activator",
                    "variable": "menu",
                    "children": v.Btn(
                        style_="min-width: 0px; padding-left: .5em; padding-right: .5em",
                        v_model=False,
                        outlined=True,
                        v_on="menu.on",
                        color="primary",
                        # icon=True,
                        children=[v.Icon(children=["mdi-palette"])],
                    ),
                }
            ],
            children=[
                v.List(dense=True, outlined=True, rounded=True, children=[self.color])
            ],
        )

        # create the map
        super().__init__(gee=False)

        # add the widget to the map (as to left and right items)
        self.add_control(WidgetControl(widget=self.state, position="topleft"))
        self.add_control(WidgetControl(widget=self.palette, position="topleft"))

        # create jslinks
        jslink((self, "combo"), (self.color, "v_model"))
