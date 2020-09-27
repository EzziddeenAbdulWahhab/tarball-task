#!/usr/local/bin/python3.8

import logging 
import traceback
from tarball_builder import *

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)

try:
	create_release_note()
	logging.info("Started creating the manifest")
	create_manifest()
	logging.info("Started downloading rpms")
	download_rpms()
	logging.info("Started creating tarball")
	create_tarball()
	logging.info("Finished creating tarball")
except Exception as err:
	logging.error(traceback.format_exc())
