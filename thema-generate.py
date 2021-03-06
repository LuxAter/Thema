#!/usr/bin/env python3

import json
import os
import glob
from argparse import ArgumentParser

import chevron

def generate_data(base):
    output = {}
    for key, val in base.items():
        output[f"hex {key}"] = val
        output[f"Hex {key}"] = val[1:]
    return output

def generate_templates(source):
    color_data = {}
    with open(source) as template:
        color_data = json.load(template)

    data = generate_data(color_data)

    templates = glob.glob('./_template/**/*', recursive=True)

    if "variant" in color_data:
        output = f"./{color_data['name']}/{color_data['variant']}/"
    else:
        output = f"./{color_data['name']}/"

    for template in templates:
        outfile = f"{output}{os.path.basename(template)}"
        if os.path.exists(outfile):
            continue
            print(f"Skipping {template}")
        if template == "./_template/_colors.json":
            continue
        print(f"Rendering {template} to {outfile}")
        with open(template, 'r') as temp:
            ren = chevron.render(temp, data)
            if not os.path.exists(os.path.dirname(outfile)):
                os.makedirs(os.path.dirname(outfile))
            with open(outfile, 'w') as outfile:
                outfile.write(ren)

def main():
    parser = ArgumentParser('thema-generate')
    parser.add_argument('source', nargs='*', help='Theme definition JSON file')

    args = parser.parse_args()

    if len(args.source) == 0:
        args.source = glob.glob('./**/_colors.json', recursive=True)

    for source in args.source:
        generate_templates(source)




if __name__ == "__main__":
    main()
