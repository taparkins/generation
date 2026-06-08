

class KDTree(object):
    def __init__(self, data, comp_dim):
        self.data = data
        self.dim = len(data)
        self.comp_dim = comp_dim
        self.left_child = None
        self.right_child = None

        assert self.comp_dim < self.dim


    def add_child(self, child_data):
        assert len(child_data) == self.dim
        child_comp_dim = (self.comp_dim + 1) % self.dim

        def _add_left(child_data):
            if self.left_child is None:
                self.left_child = KDTree(child_data, child_comp_dim)
            else:
                self.left_child.add_child(child_data)

        def _add_right(child_data):
            if self.right_child is None:
                self.right_child = KDTree(child_data, child_comp_dim)
            else:
                self.right_child.add_child(child_data)

        if child_data[self.comp_dim] < self.data[self.comp_dim]:
            _add_left(child_data)
        else:
            _add_right(child_data)


    def __repr__(self):
        return f'{{"data":{self.data}, "left":{str(self.left_child)}, "right":{str(self.right_child)}}}'


    @staticmethod
    def from_list(data_list):
        # we can't determine dimension of the tree from an empty list,
        # so this is considered an invalid input for now
        assert len(data_list) > 0

        # It will be an error down the line if any of the later data
        # points have a mismatched dimension length
        dim = len(data_list[0])

        def _from_list(sublist, cur_dim):
            if len(sublist) == 0:
                return None

            sorted_list = sorted(sublist, key=lambda d: d[cur_dim])
            median = sorted_list[len(sorted_list)//2]
            left_sublist = sorted_list[:len(sorted_list)//2]
            right_sublist = sorted_list[len(sorted_list)//2 + 1:]

            root = KDTree(median, cur_dim)
            new_dim = (cur_dim + 1) % dim
            root.left_child = _from_list(left_sublist, new_dim)
            root.right_child = _from_list(right_sublist, new_dim)

            return root

        return _from_list(data_list, 0)
