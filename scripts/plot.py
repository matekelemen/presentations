# --- External Imports ---
import numpy
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties

# --- STD Imports ---
import argparse
import pathlib


labelFont = {
    #"family" : "Nexus",
    "weight" : "normal",
    "size" : 24
}

legendFont = {
    #"family" : "Nexus",
    "weight" : "normal",
    "size" : 16
}

tickFont = {
    #"fontname" : "Nexus",
    "fontsize" : 16
}

colors = [numpy.array(rgb) / 255.0 for rgb in (
    [0, 82, 147],
    [227, 114, 34],
    [162, 173, 0]
)]


parser = argparse.ArgumentParser()
parser.add_argument("-i",
                    dest = "inputs",
                    type = pathlib.Path,
                    nargs = "+",
                    required = True)
parser.add_argument("-o",
                    dest = "output",
                    type = pathlib.Path,
                    required = True)
parser.add_argument("-l",
                    "--legend",
                    dest = "legend",
                    type = str,
                    required = True,
                    nargs = "+")
parser.add_argument("-e",
                    "--end-time",
                    dest = "endTime",
                    type = float,
                    default = 1.0)
parser.add_argument("--x-label",
                    dest = "xLabel",
                    type = str,
                    default = "time")
parser.add_argument("--y-label",
                    dest = "yLabel",
                    type = str,
                    default = "tip displacement")

args = parser.parse_args()
values: "list[numpy.ndarray]" = []
samples: "list[numpy.ndarray]" = []
for input in args.inputs:
    values.append(numpy.fromfile(input))
    samples.append(numpy.linspace(0.0, args.endTime, len(values[-1])))

for i_line, (x, y) in enumerate(zip(samples, values)):
    pyplot.plot(x, y, color = colors[i_line])

pyplot.legend(args.legend,
              prop = FontProperties(**legendFont))
pyplot.xticks(**tickFont)
pyplot.xlabel(args.xLabel,
              fontdict = labelFont)
pyplot.yticks(**tickFont)
pyplot.ylabel(args.yLabel,
              fontdict = labelFont)
pyplot.tight_layout()
pyplot.savefig(args.output)

