import os
import yaml
import logging

def download_rpms():
	with open("data.yaml") as yaml_file:
		yaml_content = yaml.safe_load(yaml_file)
	download_urls = (rpm["download_url"] for cesa in yaml_content["CESA_list"] for rpm in cesa["RPM_list"])
	os.system("wget " + ' '.join(download_urls))

def create_tarball():
	with open("data.yaml") as yaml_file:
		yaml_content = yaml.safe_load(yaml_file)
	image_version = yaml_content["goldimage_ver"]
	tar_command = "tar czf CVM_PE_GI-7.7r1.6.1-20200303-x86_64.tar.gz "
	manifest_file_name = "CVM_RPM_LIST_MANIFEST.json "
	release_file_name = image_version + "-x86_64.release_notes "
	rpm_packages = ' '.join((rpm["rpm_pkg"] for cesa in yaml_content["CESA_list"] for rpm in cesa["RPM_list"]))
	os.system(tar_command + manifest_file_name + release_file_name + rpm_packages)
try:
	logging.info("Started downloading rpms")
	download_rpms()
	logging.info("Started creating tarball")
	create_tarball()
	logging.info("Finished downloading rpms and creating tarball")
except Exception as err:
	logging.error(traceback.format_exc())
