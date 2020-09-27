from string import Template
import yaml
import json
import subprocess

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

def download_rpms():
	with open("CVM_RPM_LIST_MANIFEST.json") as json_file:
		json_content = json.loads(json_file.read())
	download_urls = (rpm["download_url"] for cesa in json_content["CESA_list"] for rpm in cesa["RPM_list"])
	subprocess.run("wget " + ' '.join(download_urls),check = True,shell= True)

def create_tarball():
	with open("data.yaml") as yaml_file:
		yaml_content = yaml.safe_load(yaml_file)
	image_version = yaml_content["goldimage_ver"]
	tar_command = "tar czf CVM_PE_GI-7.7r1.6.1-20200303-x86_64.tar.gz "
	manifest_file_name = "CVM_RPM_LIST_MANIFEST.json "
	release_file_name = image_version + "-x86_64.release_notes "
	rpm_packages = ' '.join((rpm["rpm_pkg"] for cesa in yaml_content["CESA_list"] for rpm in cesa["RPM_list"]))
	subprocess.run(tar_command + manifest_file_name + release_file_name + rpm_packages,check=True,shell=True)
