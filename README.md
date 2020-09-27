# tarball-task
This project is a simple task for patching some CVEs through rpms. The goal is to create a tarball with the required rpms and some information related to the CVEs and the patch in general

<h3>Installation</h3>
Run the following python script 
<ol>
<li>create-tarball.py</li>
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
<h4>create-tarball.py</h4>
This file utilizes the tarball_builder module to build the tarball and log the different phases of building it.
<h4>tarball_builder.py</h4>
This module contains various functions, each represents a stage in the building of the final tarball.</br>
These are the functions contained:
<ul>
  <li>create_manifest</li>
  <li>create_release_note</li>
  <li>download_rpms</li>
  <li>create_tarball</li>
</ul>
The function create_manifest is responsible for reading the data.yaml file and converting it to json format.</br>
The function create_release_note is responsible for extracting data from the data.yaml file and building the release note file from it using a template.</br>
The function download_rpms extracts the rpm download links from the manifest json file and downloads them for tarring.</br>
The last function , create_tarball simply runs the tar command on the various components set up in the previous steps.
