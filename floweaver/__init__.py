"""View flow data as Sankey diagrams."""

__version__ = '2.1.0-dev'

from .dataset import Dataset
from .partition import Partition, Group
from .sankey_definition import SankeyDefinition, ProcessGroup, Waypoint, Bundle, Elsewhere
from .view_graph import view_graph
from .results_graph import results_graph
from .augment_view_graph import elsewhere_bundles, augment
from .hierarchy import Hierarchy
from .sankey_data import SankeyData, SankeyLink, SankeyNode, SankeyLayout
from .color_scales import CategoricalScale, QuantitativeScale
from .weave import weave
from .diagram_optimisation import optimise_node_order, optimise_node_positions, optimise_hybrid_model
from .dataset_manipulation import generate_nodes, generate_ordering, generate_waypoints_bundles

__all__ = ['Dataset', 'Partition', 'Group', 'SankeyDefinition', 'ProcessGroup',
           'Waypoint', 'Bundle', 'Elsewhere', 'view_graph', 'results_graph',
           'elsewhere_bundles', 'augment', 'Hierarchy', 'weave', 'SankeyData',
           'SankeyLink', 'SankeyNode', 'SankeyLayout', 'CategoricalScale', 'QuantitativeScale',
           "optimise_node_order", "optimise_node_positions", "optimise_hybrid_model",
           "generate_nodes", "generate_ordering", "generate_waypoints_bundles"]
