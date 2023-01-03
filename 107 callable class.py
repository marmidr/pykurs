import logging
logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(asctime)s:    %(message)s")

class NoDuplicates:
    def __init__(self):
        self.list = []

    def __call__(self, new_items: list):
        for item in new_items:
            if not item in self.list:
                self.list.append(item)


my_no_dup_list = NoDuplicates()
logging.debug(my_no_dup_list.list)

my_no_dup_list(['keyboard','mouse'])
logging.info(my_no_dup_list.list)

my_no_dup_list(['keyboard','mouse','pendrive'])
logging.warning(my_no_dup_list.list)

my_no_dup_list(['charger','pendrive'])
logging.error(my_no_dup_list.list)
