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
			os.chdir('..')
			cwd = os.getcwd()
			if id_maps:
			  save_dir = cwd + '/data/preprocessed/' + column_name + '_' + id_maps[column_name][str(ids)] +'.pkl'
			else:
			  save_dir = cwd + '/data/preprocessed/' + column_name + '_' + column_name + '_' + str(ids) +'.pkl'
		result.to_pickle(save_dir)
	return result

def list_to_dict(dict_list):
        """Convert a list of dictionaries into a single dictionary.
           Will be used to modify columns such as genres, keywords, and cast.
           
        Args:
                dict_list: list of dictionaries, e.g. [{"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"},
                                                       {"id": 28, "name": "Action"}, {"id": 10749, "name": "Romance"}]

        Returns:
                Dictionary where values are lists, e.g. {'id': [12, 14, 28, 10749], 'name': ['Adventure', 'Fantasy', 'Action', 'Romance']}
        """
        new_dict = {}
        for k,v in [(key, d[key]) for d in dict_list for key in d]:
                if k not in new_dict: 
                    new_dict[k]=[v]
                else: 
                    new_dict[k].append(v)
        
        return new_dict

def convert_to_dict(df, subset):
        """Take an input dataframe and modify columns that store a list of dictionaries (e.g. genres, keywords, and cast)

        Args:
                df: the dataframe under consideration
                subset: the columns that need to be converted (e.g. genre, keywords, and cast)

        Returns:
                A new dataframe with the modified columns.

        """
        data = df.copy()
        
        for column in subset:                                   # Iterate through columns that need to be converted to dict
                for i in range(len(df)):                        # Iterating through every movie
                    str_entry = data[column][i]                 # Get contents of entry as string
                    list_of_dict = json.loads(str_entry)        # Convert string into a list of dictionaries
                    df[column][i] = list_to_dict(list_of_dict)  # Convert list of dictionaries to one dictionary

        df.to_pickle(main_dir + data_dir + "pre-processed/movie_details_neat.pkl")
    
        return df

def make_id_maps(df, subset):
        """Construct dictionaries that map id to name.
        
        """
        data_copy = df.copy()
        
        id_maps = {'genres'               : {},
                   'keywords'             : {}, 
                   'production_companies' : {},
                   'production_countries' : {},
                   'spoken_languages'     : {}}

        for column in subset: 
                dict_list = []
                for i in range(len(data_copy)):
                    dict_list.append(data_copy[column][i]) # Add all dictionaries into one list

        # Create a new dictionary from the list, this only has as many entries as there are unique values
        new_dict = list_to_dict(dict_list)
        keys = list(new_dict)
        assert len(keys) == 2 #only id and name corresponding to the id

        id_list = []
        name_list = []
        new_dict
        for i in range(len(new_dict[keys[0]])):
            if column == 'production_companies': #id and name are rversed but only for production companies
                id_list += new_dict[keys[1]][i]
                name_list += new_dict[keys[0]][i]
            else:    
                id_list += new_dict[keys[0]][i]
                name_list += new_dict[keys[1]][i]
        id_map_per_column = dict(zip(id_list, name_list))
        id_maps[column] = id_map_per_column

        # Save file as json
        with open(cwd+data_dir+'pre-processed/id_maps.json', 'w') as fp:
                json.dump(id_maps, fp)
    
        return id_maps