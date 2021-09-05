import multiprocessing
import hashlib
import json
import sys 
import os


def hashfile(fname):
	sha = hashlib.sha256()
	if not os.path.isfile(fname):
		return False
	sha.update(open(fname,'rb').read())
	return sha.hexdigest()

def test_files(inputPath, files):
	base = inputPath
	for item in os.listdir(inputPath):
		f = os.path.join(base,item)
		if os.path.isfile(f):
			files[hashfile(f)] = f
		else: # else be recursive? 
			files = test_files(f,files)
	return files


def verify_dicts(real, unsure):
	failed = False
	failures = {}
	for hashval, fname in unsure.items():
		if fname not in real.values():
			print('[x] Exta File Found: %s' % fname)
			failed = True
		elif hashval in real.keys() and unsure[hashval] != real[hashval]:
			print('[x] Bad Hash Found for %s' % fname)
			failed = True
	return failed


def main():
	# Pull items from arguments
	if '-run' in sys.argv:
		target_path = sys.argv[2]
			# Load Target File List/Path
		targets = test_files(target_path, {})
		print('[-] %d Files/Hashes Ready for comparison' % len(targets.keys()))

		# Load Base Truth File List/Path
		if os.path.isfile('target_sprint.json'):
			truth = json.loads(open('target_sprint.json','r').read())
			print('[-] %d Files/Hashes loaded from Truth File' % len(truth.keys()))

		# DO the comparison
		verified, errors = verify_dicts(truth, targets)
		if not verified:
			print('[+] File Hashes Match')

	# Create a target_sprint.json file 
	elif '-create' in sys.argv:
		# Create a sprint file based on path given
		found = test_files(sys.argv[2],{})
		print('[-] %d File Hashes put into sprint file' % len(found.keys())) 
		open('target_sprint.json','w').write(json.dumps(found))
	else:
		print('[!] No input targets given')
		exit()
	



if __name__ == '__main__':
	main()