#!/bin/env python3

import yaml
import os

demreproj_jobid = os.environ['param_raster_path']
input_path = f'/compute_scratch/{demreproj_jobid}'

processor_dict = {'$1': {'DEMClip': {'raster_path':os.environ['param_input_path'],'site_id':os.environ['param_site_id'],'resolution':os.environ['param_resolution']}}}

with open('/job/executable/demclip.yml','w') as demfile:
    yaml.dump(processor_dict,demfile)
