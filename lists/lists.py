class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        max_value: int = 0
        result: list[int] = []

        for value in input_list:
            if value > max_value:
                max_value = value

        for value in input_list:
            if value >= 0:
                result.append(max_value)
            else:
                result.append(value)

        return result

    @staticmethod
    def search(input_list: list[int], query: int, low: int = 0, high: int = None) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if high is None:
            high = len(input_list) - 1
        if not input_list or low > high:
            return -1

        mid = (low + high) // 2
        midValue = input_list[mid]

        if midValue == query:
            return mid
        if midValue > query:
            return ListExercise.search(input_list, query, low, mid - 1)
        else:
            return ListExercise.search(input_list, query, mid + 1, high)
        pass
