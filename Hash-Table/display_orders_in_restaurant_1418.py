"""
URL of problem:
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
"""


class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        tables = set()
        food_dict = dict()
        for _, table, food in orders:
            tables.add(int(table))
            if food not in food_dict:
                food_dict[food] = dict()

            if int(table) not in food_dict[food]:
                food_dict[food][int(table)] = 1
            else:
                food_dict[food][int(table)] += 1

        sorted_tables = sorted(tables)
        sorted_foods = sorted(food_dict.keys())
        result = [["Table"] + sorted_foods]
        for table in sorted_tables:
            row = [str(table)] + [str(food_dict[food].get(table, 0)) for food in sorted_foods]
            result.append(row)

        return result


def main():
    print(Solution().displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))


if __name__ == "__main__":
    main()
