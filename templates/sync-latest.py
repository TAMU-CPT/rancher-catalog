#!/usr/bin/env python
import yaml
import glob
import os


for tpl in glob.glob("*"):
    if '.py' in tpl: continue

    # Get the subdirs + files
    contents = glob.glob(os.path.join(tpl, '*'))
    # Filter out files
    contents = [x[len(tpl) + 1:] for x in contents if '.' not in x]
    # Map to integers
    latest = max(map(int, contents))

    with open(os.path.join(tpl, str(latest), 'rancher-compose.yml'), 'r') as handle:
        data = yaml.load(handle)
        config = data['.catalog']

    with open(os.path.join(tpl, 'config.yml'), 'r+') as handle:
        main_conf = yaml.load(handle)
        for prop in ('name', 'description', 'version'):
            if prop in config:
                main_conf[prop] = str(config[prop]).strip()

        handle.seek(0)
        handle.truncate()
        yaml.dump(main_conf, handle, default_flow_style=False)
