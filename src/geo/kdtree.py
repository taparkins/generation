from src.geo.point import Point
import math

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
        return f'{{"data":"{self.data}", "left":{str(self.left_child)}, "right":{str(self.right_child)}}}'


    def find_nearest(self, search_point):
        # NOTE: I made the kdtree very generic, but my distance function isn't generic, lol
        # for now I'm just going to let this smell in
        self_distance = Point.dist(
            Point(self.data[0], self.data[1]),
            Point(search_point[0], search_point[1])
        )

        # Case 1: No children
        if self.left_child is None and self.right_child is None:
            return self_distance, self.data

        # Case 2: Exactly one child
        elif self.left_child is None or self.right_child is None:
            search_child = self.left_child or self.right_child
            distance, data = search_child.find_nearest(search_point)
            if self_distance < distance:
                distance, data = self_distance, self.data
            return distance, data

        # Case 3: Two children
        else:
            check_child = None
            other_child = None
            dim_difference = search_point[self.comp_dim] - self.data[self.comp_dim]
            if dim_difference < 0:
                check_child = self.left_child
                other_child = self.right_child
            else:
                check_child = self.right_child
                other_child = self.left_child

            distance, data = check_child.find_nearest(search_point)
            if self_distance < distance:
                distance, data = self_distance, self.data

            # It's possible that the nearest point was actually on the other half-plane,
            # meaning the other child should have been checked.
            # If this happens, it means the single-coordinate difference between the
            # search point and this node's data is less than the minimum distance
            # This does the backup check, accordingly
            if math.fabs(dim_difference) <= distance:
                other_distance, other_data = other_child.find_nearest(search_point)
                if other_distance < distance:
                    distance, data = other_distance, other_data

            return distance, data


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
