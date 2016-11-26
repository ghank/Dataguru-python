import ctypes
import random

class Array(object):
    def __init__(self, size):
        """
        用传入的大小参数创建一个数组
        :param size: int
        """
        assert size > 0, "数组必须大于0"
        self._size = size
        # 用ctypes模块创建数组
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        # Initialize each element
        self.clear(None)

    def __len__(self):
        """
        返回数组的长度
        :return: int
        """
        return self._size

    def __getitem__(self, index):
        """
        返回索引的元素
        :param index: int
        :return: elements in Array
        """
        assert 0 <= index < len(self), "数组下标越界。"
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        为索引的元素赋值
        :param index: int
        :param value: any type
        """
        assert 0 <= index < len(self), "数组下标越界。"
        self._elements[index] = value

    def clear(self, value):
        """
        将数组的每个元素设置为给定的值
        :param value: any type
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        返回数组的迭代器
        :return: iter
        """
        return _ArrayIterator(self._elements)

    def __str__(self):
        """
        返回可打印数据
        :return: str
        """
        return str([element for element in self._elements])


class _ArrayIterator(object):
    # 初始化类，下标指向第一位
    def __init__(self, the_array):
        """
        数组的迭代器类
        :param the_array: Array
        """
        self._arrayRef = the_array
        self._curNdx = 0

    def __iter__(self):
        """
        返回迭代器本身
        :return: iter
        """
        return self

    # 下标没有越界，返回对应元素，下标+1；下标越界，抛出StopIteration异常
    def next(self):
        """
        迭代器的next实现
        :return: element of Array
        """
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


class Vector(Array):
    def __add__(self, other):
        """
        向量加法，如果其中一个是int或float型，将向量的每一个元素与其相加，如果两个是Vector型，将两个向量中对应的元素相加
        :param other: Vector or int or float
        :return: Vector
        """
        # 创建一个Vector类型的tmp变量
        tmp = Vector(len(self))
        # 判断other是否是int或float型
        if isinstance(other, int) or isinstance(other, float):
            # 将向量中每一个元素都加上other
            for i in range(len(self)):
                tmp[i] = self._elements[i] + other
        # 判断other是否是Vector型
        elif isinstance(other, Vector):
            assert len(self) == len(other), '向量长度不相等'
            # 将向量中每一个元素与other中对应元素相加
            for i in range(len(self)):
                tmp[i] = self._elements[i] + other[i]
        # 如果other是其他类型，发起TypeError异常
        else:
            raise TypeError

        return tmp

    def __mul__(self, other):
        """
        向量乘法，如果其中一个是int或float型，将向量的每一个元素与其相乘，如果两个是Vector型，将两个向量中对应的元素相乘
        :param other: Vector or int or float
        :return: Vector
        """
        tmp = Vector(len(self))
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self)):
                tmp[i] = self._elements[i] * other

        elif isinstance(other, Vector):
            assert len(self) == len(other), '向量长度不相等'
            for i in range(len(self)):
                tmp[i] = self._elements[i] * other[i]
        # 如果other是其他类型，发起TypeError异常
        else:
            raise TypeError
        return tmp

    def dot(self, other):
        """
        计算向量点积，将两个向量对应元素相乘，并将结果相加
        :param other: Vector
        :return: Vector
        """
        assert isinstance(other, Vector), '传入参数非Vector类型'
        assert len(self) == len(other), '向量长度不相等'
        sums = 0
        for x, y in zip(self, other):
            sums += x * y

        return sums


if __name__ == '__main__':
    x1 = Vector(4)
    x1[0] = 1
    x1[1] = 2
    x1[2] = 3
    x1[3] = 4

    x2 = Vector(4)
    x2[0] = 1
    x2[1] = 2
    x2[2] = 3
    x2[3] = 4

    print x1 + 4.5
    print x1 + x2
    print x1 * 3.4
    print x1 * x2

    print x1.dot(x2)