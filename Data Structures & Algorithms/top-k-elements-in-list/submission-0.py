class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for j in nums:
            seen[j]=seen.get(j,0)+1
        s=sorted(seen,key=seen.get,reverse=True)[:k]
        return s