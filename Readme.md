# Plot HL usage
## Preparation
```
apt install python3.10-venv
python3 -m venv .
. ./bin/activate
python -m pip install matplotlib dash pandas
```

## Usage
1. copy `docker-auslastung.log` from vm-docker-01 to this folder
2. run `prepare.sh` and this will create the cvs output file `source-log`

```
./prepare.sh docker-auslastung.log
```

3. run `plot-stats.py` and this will create the graph

```
./plot-stats.py -f source-log
```

example
* https://www.hacking-lab.com/blog/docker-stats
