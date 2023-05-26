# [풀이 1] : 투 포인터를 최대로 이동

## 설명

가장 높이가 높은 막대는 얼마나 높냐(ex.3이냐 100이냐)와는 무관하게, 전체 부피에 영향을 끼치지 않으면서 그저 왼쪽과 오른쪽을 가르는 장벽 역할을 한다.

1. 최대 높이의 막대까지 각각 좌우 기둥 최대 높이 left_max, right_max가 현재 높이와의 차이만큼 물 높이 volume을 더해 나간다.

```python
    volume += left_max - height[left]
    ...
    volume += right_max - height[right]
```

2. 적어도 낮은 쪽은 그만큼 항상 채워질 것이기 때문에, 좌우 어느쪽이든 낮은 쪽은 높은 쪽을 향해서 포인터가 점점 가운데로 이동한다.

```python
    if left_max <= right_max:
        volume += left_max - height[left]
        left += 1
    else:
        volume += right_max - height[right]
        right -= 1
```

오른쪽이 크다면 left+=1 로 왼쪽이 이동하고, 왼쪽이 크다면 right+=1 로 오른쪽이 이동한다.

3. 이렇게 하면 가장 높이가 높은 막대, 즉 '최대' 지점에서 좌우 포인터가 서로 만나게 되며 O(n)에 풀이가 가능하다.

## 최종 코드

```python
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터로 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume
```

# [풀이 2] : 스택 쌓기

## 설명

1. 스택에 쌓아나가면서 현재 높이가 이전 높이보다 높을때, 즉 꺾이는 부분 변곡점(Inflection Point)을 기준으로 격차만큼 물 높이 volume을 채운다.

2. 이전 높이는 고정된 형태가 아니라 들쑥날쑥하기 때문에, 계속 스택으로 채워 나가다가 변곡점을 만날때마다 스택에서 하나씩 꺼내면서 이전과의 차이만큼 물 높이를 채워 나간다.

3. 스택으로 이전 항목들을 되돌아보며 체크하기는 하지만, 기본적으로 한번만 살펴보기 때문에 마찬가지로 O(n)에 풀이가 가능하다.

## 최종 코드

```python
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()
                if not len(stack):
                    break
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)
        return volume
```

# 문제에 대한 저자의 comment

> 상당히 어려운 문제임.
> 만약 온사이트 인터뷰일 경우엔 화이트보드에 그림을 그려가며 개념을 잘 잡아 설명하면 보다 원활하게 문제를 풀어나갈 수 있을것임.
