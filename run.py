import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from tqdm import tqdm
import json
import os
import sys

def main():
	option = 'all'
	if len(sys.argv) > 1:
		option = sys.argv[1]

	with open('notebook_list.json', 'r') as f:
		nb_list = json.load(f)

	if option == 'all':
		folders_to_run = nb_list.keys()
	else:
		if option not in nb_list.keys():
			print('Please enter valid folders to run!')
			return
		folders_to_run = [option]

	for folder in folders_to_run:
		print('Running folder: ' + folder)
		for nb in tqdm(nb_list[folder]):
			nb_path = os.path.join(folder, nb) + '.ipynb'

			with open(nb_path, 'r') as f:
				nb = nbformat.read(f, as_version=4)
			ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
			ep.preprocess(nb, {'metadata': {'path': folder + '/'}})

			with open(nb_path, 'w') as f:
				nbformat.write(nb, f)

if __name__ == '__main__':
	main()


