# [풀이 1] : 리스트 변환

## 설명

-   팰린드롬 여부를 판별하기 위해서는 앞뒤로 모두 추출할 수 있는 자료구조가 필요.
-   일반적인 스택 자료구조는 마지막 요소를 추출하는 연산만 있지만, 파이썬의 리스트는 pop() 함수에 인덱스를 지정할 수 있어 마지막 요소가 아니라도 얼마든지 원하는 위치를 자유롭게 추출할 수 있음.
-   따라서 이 문제는 연결 리스트를 파이썬의 리스트로 변환하여 리스트의 기능을 이용하면 쉽게 풀이할 수 있을 것으로 보임.
-   자유롭게 인덱스를 지정할 수 있는 파이썬 리스트의 강력함을 확인해볼 수 있다.

## 최종 코드

```python
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        # 탤린드롬 판별
        while len(q)>1:
            if q.pop(0) != q.pop():
                return False

        return True
```

-   이렇게도 충분히 풀이할 수 있지만, 연결 리스트 자료형을 변환하지 않고 풀이하면 더욱 깔끔할 것 같다. (마지막 풀이에서...)

# [풀이 2] : 데크를 이용한 최적화

## 설명

-   위 리스트 풀이를 데크를 활용해 좀더 최적화 시킬 수 있다.

```python
    if q.pop(0) != q.pop():
```

-   앞선 풀이의 문제점은 pop으로 앞쪽 아이템을 추출할때의 속도 문제임.
-   동적 배열로 구성된 리스트는 맨 앞 아이템을 가져오기에 적합한 자료형이 아님. 첫번째 값을 꺼내오면 모든 값이 한칸씩 shifting되며, 시간복잡도 O(n)이 발생하기 때문.
-   이때문에 최적화를 위해서는 맨 앞 데이터를 가져올때 O(n) 이내에 처리할 수 있는 자료형이 필요함.
-   파이썬의 데크(Deque)는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는데 시간 복잡도 O(1)에 실행됨.

> 만약 리스트로 처리했을때 타임아웃이 발생하거나, 오프라인 코딩 인터뷰에서 면접관이 어떻게 하면 더 효율적일지를 질문한다면, 양방향 모두 O(1)
> 에 가능한 데크를 설명한 다음 이 자료형을 적용할 것이라는 점을 이야기 해 볼 수 있을 것이다.

파이썬에서 리스트를 데크로 수정하려면 아래와 같이 딱 두군데만 수정하면 됨.

```python
    q: Deque = collections.deque()
    ...
    if q.popleft() != q.pop():
    ...
```

## 최종 코드

```python
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        # 탤린드롬 판별
        while len(q)>1:
            if q.popleft() != q.pop():
                return False

        return True
```

-   수정된 부분은 두 군데에 불과하지만 데크의 명시적인 선언만으로 상당한 (2배 이상) 속도 개선 효과가 있음.
-   매우 간단하면서도 효율적인 최적화 방법임.

# [풀이 3] : 런너를 이용한 우아한 풀이

## 설명

> 사실 이 팰린드롬 연결 리스트 문제의 제대로 된 풀이법은 런너(Runner) 기법을 활용하는 것임.

![런너 풀이](https://github.com/mod-haus/cosmo-app/assets/33515577/abf6e39c-ea59-481a-999e-b4563c9066d6)

-   파란색으로 표시된 1,2,3,4는 실행순서를 보여줌.
-   순서에 따라 2개의 런너, 즉 Fast Runner와 Slow Runner를 각각 출발시키면, Fast Runner가 끝에 다다를때 Slow Runner는 정확히 중간 지점에 도달하게 될 것임.
-   느린 런너는 중간까지 이동하면서 역순으로 연결 리스트 rev를 만들어 나간다.
-   이제 중간에 도달한 느린 런너가 나머지 경로를 이동할때, 역순으로 만든 연결리스트의 값들과 일치하는지 확인해나가면 됨.

1. 빠른 런너 fast와 느린 런너 slow의 초깃값은 다음과 같이 모두 head에서 시작함.

```python
    slow = fast = head
```

2. 이제 런너를 이동할 차례. 다음과 같이 next가 존재하지 않을때까지 이동함. 빠른 런너인 fast는 두칸씩, 느린 런너 slow는 한칸씩 이동함.

```python
    while fast and fast.next:
        fast = fast.next.next
        ...
        slow = slow.next
```

3. 그러면서 역순으로 연결 리스트 rev를 생성하는 로직을 slow 앞에 덧붙임. 첫 rev의 값은 None에서 시작하고, 런너가 이동하면서 위 그림에서처럼 1->None, 2->1->None로 점점 이전 값으로 연결되는 구조가 됨.

```python
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
```

4. 역순 연결 리스트는 현재 값을 slow로 교체하고 rev.next는 rev가 됨. 즉 앞에 계속 새로운 노드가 추가되는 형태가 됨. 결국 이 연결 리스트는 slow의 역순 연결 리스트가 될 것임.

```python
    rev, rev.next, slow = slow, rev, slow.next
```

5. 입력값이 홀수일때와 짝수일때 마지막 처리가 다른데, 홀수일 때는 slow 런너가 한칸 더 앞으로 이동하며 중앙의 값을 빗겨나가야함. 왜냐면 여기서 3은 중앙에 위치한 값으로, 팰린드롬 체크에서 배제되어야 하기 때문. 이는 fast가 아직 None이 아니라는 경우로 간주할 수 있으며, 따라서 이 경우 다음과 같이 slow를 한칸 더 이동해 마무리함.

```python
    if fast:
        slow = slow.next
```

6. 이제 팰린드롬 여부를 확인함. 다음과 같이 역순으로 만든 연결 리스트 rev를 반복함.

```python
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
```

slow의 나머지 이동 경로와 역순으로 만든 rev의 노드를 하나씩 풀어가면서 비교함.

7. 정상적으로 비교가 종료됐다면 slowDHK rev가 모두 끝까지 이동해 둘 다 None이 될 것임.
   따라서 최종결과는 return not rev 또는 return now slow 모두 가능함.

## 최종 코드

```python
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이요해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
```

## comment about this 풀이

데크로 구현한 풀이와 성능은 비슷하지만, 연결 리스트를 다른 자료형으로 변환하거나 편볍읋 사용하지 않고 그 자리에서 바로 풀이함으로써 좀더 연결 리스트 답게 위아한 방식으로 풀 수 있음.

## 관련 추가자료 by 교재

### 🧚‍♀️ 런너 기법

-> runner는 연결 리스트를 순회할때 2개의 포인터를 동시에 사용하는 기법임. 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있음.

![런너 풀이](https://github.com/mod-haus/cosmo-app/assets/33515577/cfc05840-55d1-4191-9786-f3a08d28dca8)

-   2개의 포인터는 위 그림처럼 각각 빠른 런너(Fast Runner), 느린 런너(Slow Runner)라고 부름.
-   대개 빠른 런너(포인터)는 두칸씩 건너뛰고 느린 런너(포인터)는 한칸씩 이동하게 됨.
-   이때 빠른 런너가 연결 리스트의 끝에 도달하면, 느린 런너는 정확히 연결 리스트의 중간 지점을 가리키게 됨.
-   이 같은 방식으로 중간 위치를 찾아내면, 여기서부터는 값을 비교하거나 뒤집기를 시도하는 등 여러모로 활용할 수 있어 연결 리스트 문제에서는 반드시 쓰이는 기법임.
