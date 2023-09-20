#!/bin/bash

mkdir /compute_scratch/${job_id}

cd ${result_folder}

cp *.tif /compute_scratch/${job_id}/
