# File with utility functions

import pandas as pd
import os

def retrieve_category(df, column_name, ids, id_key_name, id_maps=None, save=False, save_dir=''):
	"""Example function with PEP 484 type annotations.

	Args:
		df: the dataframe to be queried.
		column_name: name of the column to query. e.g. genres.
		ids: id of the category.
		id_key_name: The actual key to the ids. e.g. 'id', 'crew_id', 'cast_id'
		id_maps: Collection of maps from ids to category for different columns.
		save: If True it will save the file to the data/pre-processed directory.
		save_dir: Location to save the generated DataFrame.

	Returns:
		The resulting DataFrame from the query.

	"""
	dicts = df.to_dict('records')
	result_dict = []
	for row in dicts:
		if id_key_name in row[column_name].keys():
			if ids in row[column_name][id_key_name]:
				result_dict.append(row)
	result = pd.DataFrame(result_dict)
	if save:
		if not save_dir:
			cwd = os.getcwd()
			if id_maps:
			  save_dir = cwd + '/data/pre-processed/' + column_name + '_' + id_maps[column_name][str(ids)] +'.pkl'
			else:
			  save_dir = cwd + '/data/pre-processed/' + column_name + '_' + column_name + '_' + str(ids) +'.pkl'
		result.to_pickle(save_dir)
	return result