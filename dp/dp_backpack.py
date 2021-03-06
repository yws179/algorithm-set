# coding=utf8

"""
    题目来源 : LintCode (https://www.lintcode.com/problem/backpack/description)
    描述
    在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]

    样例
    如果有4个物品[2, 3, 5, 7]
    如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。
    如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。
    函数需要返回最多能装满的空间大小

    通过测试数据： 100%
"""

from utils.timer import timer


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    @timer
    def backPack(self, m, A):
        len_a = len(A)
        A.sort()
        # 使用滚动数组降低空间复杂度
        dp = [[0 for _ in range(m + 1)] for _ in range(2)]
        for i in range(len_a):
            c_row = i % 2
            o_row = (i + 1) % 2
            dp_o_row = dp[o_row]
            dp[c_row] = dp_o_row.copy()
            dp_c_row = dp[c_row]
            ai = A[i]
            for j in range(ai, m + 1):
                dp_c_row[j] = max(dp_o_row[j], dp_o_row[j - ai] + ai)
        return dp[(len_a + 1) % 2][m]


if __name__ == '__main__':
    s = Solution()
    print(s.backPack(10, [3, 4, 8, 5]))

    print(s.backPack(90, [12, 3, 7, 4, 5, 13, 2, 8, 4, 7, 6, 5, 7]))

    print(s.backPack(9000,
                     [988, 417, 92, 268, 313, 293, 530, 134, 311, 918, 355, 826, 94, 580, 793, 731, 320, 101, 612, 410,
                      640, 393, 278, 660, 842, 543, 130, 793, 407, 797, 176, 685, 521, 776, 473, 756, 597, 376, 615,
                      547, 310, 579, 177, 450, 842, 677, 640, 687, 515, 178, 583, 271, 161, 401, 595, 354, 868, 773, 74,
                      178, 626, 192, 747, 716, 148, 499, 654, 584, 886, 127, 171, 121, 563, 222, 802, 818, 546, 230, 50,
                      470, 134, 689, 276, 948, 261, 794, 680, 674, 444, 580, 313, 125, 473, 940, 888, 899, 75, 243, 792,
                      568, 173, 872, 376, 513, 719, 302, 96, 369, 163, 314, 61, 58, 181, 262, 85, 432, 695, 728, 759,
                      969, 305, 826, 345, 388, 79, 953, 838, 648, 692, 240, 645, 675, 352, 257, 711, 536, 272, 779, 99,
                      332, 909, 175, 711, 561, 170, 390, 814, 820, 383, 690, 460, 664, 395, 831, 420, 876, 413, 824,
                      605, 812, 581, 343, 518, 213, 236, 957, 273, 707, 561, 922, 681, 985, 282, 493, 299, 261, 382,
                      560, 263, 361, 936, 746, 224, 509, 578, 149, 993, 989, 730, 354, 587, 662, 184, 924, 70, 422, 344,
                      794, 459, 277, 286, 572, 970, 947, 665, 287, 675, 239, 208, 596, 907, 685, 714, 544, 90, 706, 305,
                      538, 558, 182, 798, 924, 211, 245, 613, 416, 63, 514, 830, 641, 421, 858, 238, 968, 77, 612, 864,
                      524, 988, 302, 332, 402, 751, 421, 992, 94, 836, 953, 445, 600, 197, 894, 195, 630, 792, 762, 844,
                      993, 80, 186, 471, 725, 265, 132, 939, 509, 653, 347, 837, 877, 601, 941, 418, 784, 677, 351, 673,
                      734, 790, 465, 965, 600, 267, 478, 868, 927, 825, 697, 400, 116, 708, 520, 792, 129, 448, 464,
                      336, 570, 888, 100, 352, 300, 717, 65, 999, 673, 595, 376, 480, 782, 929, 288, 810, 400, 546, 78,
                      991, 566, 494, 904, 461, 110, 741, 757, 743, 351, 570, 713, 615, 589, 838, 433, 970, 895, 767,
                      862, 314, 601, 205, 316, 831, 912, 453, 701, 919, 778, 843, 891, 794, 612, 287, 403, 358, 812,
                      336, 455, 114, 758, 116, 456, 467, 895, 108, 273, 887, 561, 586, 841, 858, 548, 352, 216, 425,
                      537, 990, 305, 568, 138, 985, 274, 436, 483, 749, 693, 817, 789, 325, 667, 481, 723, 725, 742,
                      420, 851, 666, 849, 893, 169, 911, 320, 696, 241, 108, 633, 877, 343, 898, 690, 986, 721, 819,
                      160, 238, 780, 185, 143, 473, 208, 506, 829, 747, 640, 407, 734, 84, 724, 873, 492, 798, 839, 161,
                      141, 696, 571, 688, 866, 111, 795, 651, 983, 664, 748, 875, 814, 710, 556, 219, 72, 462, 948, 89,
                      114, 497, 176, 68, 409, 826, 181, 118, 781, 394, 123, 644, 149, 665, 739, 381, 912, 256, 693, 752,
                      810, 697, 50, 739, 315, 219, 930, 411, 453, 362, 845, 609, 485, 461, 920, 290, 815, 283, 778, 635,
                      787, 154, 987, 404, 60, 414, 462, 919, 864, 356, 124, 169, 133, 586, 242, 302, 428, 68, 517, 576,
                      300, 432, 203, 228, 932, 657, 916, 997, 852, 197, 625, 157, 603, 475, 937, 215, 710, 234, 645,
                      281, 569, 645, 912, 390, 361, 853, 661, 981, 290, 303, 303, 342, 215, 716, 136, 293, 579, 555,
                      197, 299, 969, 619, 279, 696, 820, 374, 748, 521, 788, 482, 538, 896, 600, 574, 189, 318, 857,
                      125, 752, 190, 104, 987, 617, 531, 929, 602, 423, 242, 328, 461, 780, 409, 474, 903, 675, 388,
                      625, 80, 230, 500, 653, 546, 990, 138, 576, 888, 481, 402, 487, 948, 226, 441, 431, 145, 765, 222,
                      933, 276, 182, 769, 228, 91, 935, 728, 385, 543, 466, 415, 574, 227, 319, 572, 752, 759, 239, 724,
                      956, 709, 861, 512, 157, 294, 950, 265, 741, 373, 498, 767, 1000, 957, 168, 149, 668, 811, 573,
                      658, 971, 711, 662, 352, 473, 404, 868, 750, 793, 614, 532, 853, 620, 918, 283, 301, 547, 221,
                      486, 164, 664, 275, 287, 360, 79, 680, 59, 461, 874, 283, 438, 512, 358, 378, 559, 378, 681, 841,
                      479, 454, 513, 419, 310]))
