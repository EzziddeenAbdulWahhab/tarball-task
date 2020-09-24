from string import Template
import yaml
import json
import logging

def create_manifest():
	with open("data.yaml") as yaml_file:
		yaml_content = yaml.safe_load(yaml_file)
	with open("CVM_RPM_LIST_MANIFEST.json",'w') as manifest_output:
		manifest_output.write(json.dumps(yaml_content))

def create_release_note():
	with open("data.yaml",'r') as yaml_file:
		yaml_content = yaml.safe_load(yaml_file)
	with open("release-note-template.txt",'r') as template_file:
		release_template = Template(template_file.read())
	image_version = yaml_content["goldimage_ver"]
	cesa_list = (cesa["CESA"] for cesa in yaml_content["CESA_list"])
	rpm_packages = (rpm["rpm_pkg"] for cesa in yaml_content["CESA_list"] for rpm in cesa["RPM_list"])
	targeted_releases = yaml_content["goldimage_ver_dep"]
	template_data = {
	"image_version":image_version,
	"CESA_list":'\n'.join(cesa_list),
	"rpm_packages":'\n'.join(rpm_packages),
	"targeted_releases":'\n'.join(targeted_releases)}
	with open(image_version + "-x86_64.release_notes",'w') as release_output:
		release_output.write(release_template.substitute(template_data))

try:
	logging.info("Started creating the release note")
	create_release_note()
	logging.info("Started creating the manifest")
	create_manifest()
	logging.info("finished creating both the release note and the manifest")
except Exception as err:
	logging.error(traceback.format_exc())
