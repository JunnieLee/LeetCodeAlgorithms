# [풀이 1] : 재귀 구조로 연결

## 설명

-   정렬된 리스트라는 점이 중요

## 최종 코드

```python
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

```

-   l1과 l2의 값을 비교해 작은 값이 왼쪽에 오게 하고, nEXT는 그 다음 값이 엮이도록 재귀 호출하는게 이 코드의 전부임.

![두 연결 리스트 병합 과정](image.png)

1. 위 그림에서 L1과 L2는 두 연결 리스트의 첫 번쨰 값을 각각 가리킴.
2. 스왑하면서 그 다음 값이 엮이도록 계속 재귀호출하면, 그림의 순서대로 연결 리스트가 점점 하나로 병합되면서 엮이게 됨.
3. 마지막에는 L1이 null이 되면서, 즉 코드에서는 l1이 None이 되면서 재귀가 끝나고 리턴을 시작함. 마지막에 리턴을 시작하면 백트래킹 되면서 엮이게 됨.
4. 백트래킹이 종료되면 이제 두 정렬 리스트가 병합되어 하나의 연결 리스트가 됨.

# 참고

> 파이썬은 다중할당을 지원하기 때문에 스왑이 굉장히 간편하다.

```python
    l1, l2 = l2, l1
```
