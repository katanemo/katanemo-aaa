# Katanemo CLI (katutil)

katutil is command line utility to interact with Katanemo's REST based API endpoint. It covers most API calls exposed by Katanemo API.

## Installation

katutil is written in python and can be installed by just adding katutil from bin to path. For example,

```
$ cd cli
$ export PATH=$PATH:$PWD/bin
```

On first run katutil will build a docker image with all the python dependencies that are needed to run katutil. You can verify installation by running following command,

```
$ katutil get-default-service
```

On first run you might see output something similar to this,

```
➜  cli git:(adil/helper_script_readme) ✗ bin/katutil get-default-service | jq .serviceId
...
katutil image not found, building ...
[+] Building 0.7s (10/10) FINISHED
...
"kyzhyk993"
```
