
class Model(object):
    ''' Represents the base model that all models extend from '''

    def __init__(self, collection_list):
        ''' initialises the list that holds items of the given model '''

        self.collection = collection_list

    def all(self):
        ''' Returns all items in the collection list '''

        return self.collection

    def save(self, data):
        ''' Saves the new model to the list of items '''
        
        data['id'] = self.__generate__id()
        self.collection.append(data)

    def where(self, key, value):
        '''
        :param key - key to check
        :param value - value to check for given key
        
        returns list of item found with value of given key '''

        self.query = []
        
        for item in self.collection:
            if item[key] == value:
                self.query.append(item)

        return self.query

    def exists(self, key, value):
        '''
        :param key - key to check
        :param value - value to check for given key
        
        returns true if atleast 1 item found '''
        return len(self.where(key, value)) > 0

    def delete(self, id):
        ''' Deletes item with given id from database '''
        item = self.find(id)

        if not item:
            return None
        else:
            self.collection.remove(item)
            return item
    
    def find(self, id):
        '''Returns data item with id given, if data is not found, return None.'''

        for item in self.collection:
            if item['id'] == id:
                return item

        return None

    def __generate__id(self):
        ''' Generates ID for the new model '''

        if len(self.collection):
            return self.collection[-1]['id'] + 1
        else:
            return 1
    