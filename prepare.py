
# Copyright 2022, Frank Sauerburger

"""Module to prepare the ROOT file for the PyHEP conference"""

import argparse
import array
import requests
import ROOT

DATA_URL = "https://gitlab.cern.ch/fsauerbu/uhepp/-/raw/master/docs/toyhisto.json"

def download():
    """Download the example data file"""
    toydata = requests.get(DATA_URL).json()
    return toydata


def create_th1f(bin_edges, base, stat):
    """Create a histogram from the central values and stat uncertainties"""
    n_bins = len(bin_edges) - 1
    bins = array.array('f', bin_edges)
    histo = ROOT.TH1F("", "", n_bins, bins)
    for i, (base_val, stat_val) in enumerate(zip(base, stat)):
        histo.SetBinContent(i + 1, base_val)
        histo.SetBinError(i + 1, stat_val)

    return histo


def create_file(toy_data, filename):
    """Create toy ROOT file"""
    root_file = ROOT.TFile.Open(filename, "RECREATE")
    
    bin_edges = toy_data["bin_edges"]
    sig = create_th1f(bin_edges, toy_data["sig"], toy_data["sig_stat"])
    sig.SetName("signal")

    data = create_th1f(bin_edges, toy_data["data"], toy_data["data_stat"])
    data.SetName("data")

    bkg = create_th1f(bin_edges, toy_data["bkg"], toy_data["bkg_stat"])
    bkg.SetName("bkg")

    root_file.Write()
    root_file.Close()


def default_parser():
    """Return default argument parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument("output", metavar="OUTFILE", default="data.root",
                        help="Output root file")
    return parser


def main(args):
    """Main CLI entrypoint"""
    toy_data = download()
    create_file(toy_data, args.output)


if __name__ == "__main__":
    parser = default_parser()
    args = parser.parse_args()
    main(args)
