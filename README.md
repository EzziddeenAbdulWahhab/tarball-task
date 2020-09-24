# tarball-task
This project is a simple task for patching some CVEs through rpms. The goal is to create a tarball with the required rpms and some information related to the CVEs and the patch
in general

<h3>Installation</h3>
Run the python scripts in the following order
<ol>
<li>generate-manifest-release.py</li>
<li>download-and-tar.py</li>
</ol>
This should produce 7 files:
<ul>
<li>Manifest</li>
<li>Release note</li>
<li>SQLite rpm</li>
<li>Sudo rpm</li>
<li>Python pillow rpm</li>
<li>Java jdk rpm</li>
<li>tarball containing all items mentioned above</li>
</ul>
The tarball is the final file needed for the patch.
<h4>generate-manifest-release.py</h4>
This file is responsible for producing both the manifest.json and the release-notes files. It parses the data in data.yaml and directly fills it into 
the manifest.json file.
As for the release notes , they are produced using a template and only a small portion of the data in data.yaml.
<h4>download-and-tar.py</h4>
This script extracts rpm download URLs from the data.yaml file and downloads all required rpms for the tarball using wget.
As soon as the download finishes it creates the tarball using six files , four rpms and the manifest as well as the release-notes file.
