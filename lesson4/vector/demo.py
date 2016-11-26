import ctypes
import random

class Array(object):
    def __init__(self, size):
        """
        �ô���Ĵ�С��������һ������
        :param size: int
        """
        assert size > 0, "����������0"
        self._size = size
        # ��ctypesģ�鴴������
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        # Initialize each element
        self.clear(None)

    def __len__(self):
        """
        ��������ĳ���
        :return: int
        """
        return self._size

    def __getitem__(self, index):
        """
        ����������Ԫ��
        :param index: int
        :return: elements in Array
        """
        assert 0 <= index < len(self), "�����±�Խ�硣"
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Ϊ������Ԫ�ظ�ֵ
        :param index: int
        :param value: any type
        """
        assert 0 <= index < len(self), "�����±�Խ�硣"
        self._elements[index] = value

    def clear(self, value):
        """
        �������ÿ��Ԫ������Ϊ������ֵ
        :param value: any type
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        ��������ĵ�����
        :return: iter
        """
        return _ArrayIterator(self._elements)

    def __str__(self):
        """
        ���ؿɴ�ӡ����
        :return: str
        """
        return str([element for element in self._elements])


class _ArrayIterator(object):
    # ��ʼ���࣬�±�ָ���һλ
    def __init__(self, the_array):
        """
        ����ĵ�������
        :param the_array: Array
        """
        self._arrayRef = the_array
        self._curNdx = 0

    def __iter__(self):
        """
        ���ص���������
        :return: iter
        """
        return self

    # �±�û��Խ�磬���ض�ӦԪ�أ��±�+1���±�Խ�磬�׳�StopIteration�쳣
    def next(self):
        """
        ��������nextʵ��
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
        �����ӷ����������һ����int��float�ͣ���������ÿһ��Ԫ��������ӣ����������Vector�ͣ������������ж�Ӧ��Ԫ�����
        :param other: Vector or int or float
        :return: Vector
        """
        # ����һ��Vector���͵�tmp����
        tmp = Vector(len(self))
        # �ж�other�Ƿ���int��float��
        if isinstance(other, int) or isinstance(other, float):
            # ��������ÿһ��Ԫ�ض�����other
            for i in range(len(self)):
                tmp[i] = self._elements[i] + other
        # �ж�other�Ƿ���Vector��
        elif isinstance(other, Vector):
            assert len(self) == len(other), '�������Ȳ����'
            # ��������ÿһ��Ԫ����other�ж�ӦԪ�����
            for i in range(len(self)):
                tmp[i] = self._elements[i] + other[i]
        # ���other���������ͣ�����TypeError�쳣
        else:
            raise TypeError

        return tmp

    def __mul__(self, other):
        """
        �����˷����������һ����int��float�ͣ���������ÿһ��Ԫ��������ˣ����������Vector�ͣ������������ж�Ӧ��Ԫ�����
        :param other: Vector or int or float
        :return: Vector
        """
        tmp = Vector(len(self))
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self)):
                tmp[i] = self._elements[i] * other

        elif isinstance(other, Vector):
            assert len(self) == len(other), '�������Ȳ����'
            for i in range(len(self)):
                tmp[i] = self._elements[i] * other[i]
        # ���other���������ͣ�����TypeError�쳣
        else:
            raise TypeError
        return tmp

    def dot(self, other):
        """
        �������������������������ӦԪ����ˣ�����������
        :param other: Vector
        :return: Vector
        """
        assert isinstance(other, Vector), '���������Vector����'
        assert len(self) == len(other), '�������Ȳ����'
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