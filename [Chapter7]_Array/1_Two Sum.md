> 매우 쉬운 문제.
> 단, 최적화 할 수 있는 여러가지 방법이 숨어 있어서 코딩 인터뷰시 높은 빈도로 출제되는 문제.

# [풀이 1] : 브루트 포스로 계산

## 설명

가장 비효율적인 풀이법 1번..

## 최종 코드

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```

## 시간복잡도 : O(n^2)

문제가 풀리기는 하나 지나치게 느리다. 좀더 최적화 할 수 있는 방안을 고민해야 한다.

# [풀이 2] : in을 이용한 탐색

## 설명

모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫번째 값을 뺀 값 target-n 이 존재하는지 탐색하는 문제로 변경해보자.

## 최종 코드

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            complement = target-n

        if complement in nums[i+1]:
            return [nums.index(n), nums[i+1:].index(complement)+(i+1)]
```

## 시간복잡도 : O(n^2)

-   여기서 in의 시간복잡도는 O(n)이고 따라서 전체 시간 복잡도는 이전과 동일한 O(n^2)이다.
-   하지만 여기선 같은 시간복잡도라 하더라도 in 연산쪽이 훨씬 빠르고 가볍다.
-   시간복잡도만으로는 드러나지 않지만, 여기서 생략된 상수항은 이전 풀이에 비해 훨씬 더 작은 값이라고 말할 수 있다.

# [풀이 3] : 첫번째 수를 뺀 결과 키 조회

## 설명

-   이번엔 시간복잡도를 개선해 속도를 높여본다.
-   비교나 탐색 대신 한번에 정답을 찾을 수 있는 방법을 찾는다.

## 최종 코드

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i,num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과로 키를 조회
        for i, num in enumerate(nums):
            if target - num in nums and i != nums_map[target-num]:
                return [i, nums_map[target-num]]
```

타겟에서 첫번째 수를 뺀 결과를 키로 조회해보면 두번째 수의 인덱스를 즉시 조회할 수 있다.

## 시간복잡도 : O(n)

-   딕셔너리는 해시 테이블로 구현되어 있고, 이 경우 조회는 평균적으로 O(1)에 가능하다.
-   (최악의 경우에는 O(n)이 될 수 있지만 일단 최악의&드문 경우 이므로 불할 상환 분석에 따른 시간복잡도는 O(1)이다.)
-   따라서 전체는 O(n)이 된다.
-   앞선 풀이 1,2 에 비해 훨씬 빠른 속도를 보여준다.

# [풀이 4] : 조회 구조 개선

## 설명

-   딕셔너리 저장과 조회를 2개의 for문으로 각각 처리했던 방식을 좀더 개선해 하나의 for로 합쳐서 처리한다.
-   이 경우 전체를 모두 저장할 필요 없이 정답을 찾게 되면 함수를 바로 빠져나올 수 있다.

## 최종 코드

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num],i]
            nums_map[num] = i
```

코드는 한결 더 간결해진다. 그러나 두번쨰 값을 찾기 위해 어차피 매번 비교해야 하기 때문에 앞서 풀이에 비해 성능상의 큰 이점은 없다.
