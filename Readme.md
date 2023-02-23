# Plot HL usage

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
