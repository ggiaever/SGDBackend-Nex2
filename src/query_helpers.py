import pdb


class QueryHelpers(object):

    def get_all_chebi_dict(self, chebi_data, key_flag=False):

        #chebi_items = DBSession.query(Chebi).all()
        dict_obj = {}
        if key_flag == True:
            for item in chebi_data:
                if item.chebi_id not in dict_obj:
                    dict_obj[item.chebi_id] = []
                dict_obj[item.chebi_id].append(item)
            return dict_obj
        else:
            for item in chebi_data:
                if item.display_name not in dict_obj:
                    dict_obj[item.display_name] = []
                dict_obj[item.display_name].append(item)
            return dict_obj

    def get_chebi_item_by_display_name(self, display_name, chebi_data):
        chebi_data = chebi_data
        if display_name:
            if chebi_data is not None:
                temp_list = chebi_data.get(display_name)
                if len(temp_list) > 0:
                    #pdb.set_trace()
                    return temp_list[0]

        return None
