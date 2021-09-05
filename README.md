# BINSPRINT
Want to have a tool that will quickly look at every file in a path, and check if their
SHA256 hashsums match against an input "true" hash value. 

For instance, a repository could be cloned to `/tmp/Example` and compared to same 
repository at `/home/Users/Example` using:
```python
python3 main.py -create /home/Users/Example
python3 main.py -run /tmp/Example
```
An Example of the output (and how long this comparison might take) is shown below:
```
[-] 1748 Files/Hashes Ready for comparison
[-] 1747 Files/Hashes loaded from Truth File
[x] Exta File Found: target_sprint.json

real	0m1.264s
user	0m0.916s
sys	0m0.348s
```
