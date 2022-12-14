class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """

        answer = 0
        dic = dict()

        for a, b in reservedSeats:
            if a not in dic:
                dic[a] = [b]
            else:
                dic[a].append(b)

        for k, v in dic.items():
            # if len(v)<=2 and 1 and 10 in v or 1 in v or 10 in v:
            # answer += 2
            flag = 0
            if 2 not in v and 3 not in v and 4 not in v and 5 not in v:
                answer += 1
                flag = 1
            if 6 not in v and 7 not in v and 8 not in v and 9 not in v:
                answer += 1
                flag = 1
            if 4 not in v and 5 not in v and 6 not in v and 7 not in v and not flag:
                answer += 1
        answer += (n - len(dic)) * 2
        return answer
