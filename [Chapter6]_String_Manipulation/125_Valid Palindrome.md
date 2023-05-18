# 🧚‍♀️ [풀이 1] : 리스트로 변환

## 설명

1. 대소문자 여부를 구훈하지 않으며 영문자, 숫자만을 대상으로 해야하므로 전처리 진행

```python
    strs = []
    for char in s:
        if char.isalnum(): # isalnum() : 영문자, 숫자 여부를 판별하는 함수
            strs.append(char.lower())
```

2. 리스트의 pop()을 활용해 팰린드롬 여부 판별

```python
    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): # list.pop(idx)을 하면 해당 idx element pop 가능
            return False
    # 모두 통과했다면 True return
    return True
```

## 최종 코드

```python
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # isalnum() : 영문자, 숫자 여부를 판별하는 함수
                strs.append(char.lower())
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop(): # list.pop(idx)을 하면 해당 idx element pop 가능
                return False
        # 모두 통과했다면 True return
        return True
```

---

# 🧚 [풀이 2] : 데크 자료형을 이용한 최적화

리스트로도 풀 수 있지만 명시적으로 deque를 선언해 사용하면 좀더 속도를 높힐 수 있다.

## 설명

리스트로도 풀 수 있지만 명시적으로 deque를 선언해 사용하면 좀더 속도를 높힐 수 있다.

### 자료형 데크로 선언하기

```python
    strs : Deque = collections.deque()
```

1번 풀이에 비해 5배 가까이 더 속도를 낼 수 있다.
이는 리스트의 pop(0)이 O(n)인데 반해, deque의 popleft()는 O(1)이기 때문이다.
-> 각각 n번씩 반복하면, 리스트구현은 O(n^2), 데크구현은 O(n)으로 성능차이가 크다.

## 최종 코드

```python
    def isPalindrome(self, s: str) -> bool:
        # 자료형 deque로 선언
        strs : Deque = collections.deque()
        for char in s:
            if char.isalnum(): # isalnum() : 영문자, 숫자 여부를 판별하는 함수
                strs.append(char.lower())
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.popLeft() != strs.pop(): # deque는 popleft(), pop() 둘다 가능
                return False
        # 모두 통과했다면 True return
        return True
```

---

# 🧚‍♂️ [풀이 3] : 슬라이싱 사용

> 파이썬의 최적화된 내부 기능을 활용해 성능을 더 높였다!

## 설명

1. 정규식으로 불필요한 문자열을 필터링한다.

```python
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-zA-Z0-9]','',s)
```

2. s == s[::-1] 로 팰린드롬 여부를 확인한다.

```python
    return s == s[::-1]
```

[::-1]을 사용하면 뒤집을 수 있다.

## 최종 코드

```python
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-zA-Z0-9]','',s)

        return s == s[::-1]
```

> 코드가 훨씬더 줄어듦은 물론, 내부적으로 c로 빠르게 구현되어 있어 훨씬 더 좋은 속도를 기대할 수 있다.
> 앞선 풀이 2 에 비해 약 2배 정도 더 속도를 높일 수 있다.

## 관련 추가자료 by 교재

### 🧞‍♂️ 문자열 슬라이싱

-   파이썬에서 문자열 슬라이싱은 내부적으로 매우 빠르게 동작한다.
-   위치를 지정하면 해당 위치의 배열 포인터를 얻게 되며 이를 통해 연결된 객체를 찾아 실제 값을 찾아내는데,
-   이 과정은 매우 빠르게 진행되므로 문자열을 조작할때는 항상 슬라이싱을 우선적으로 사용하는 편이 속도 개선에 유리하다.
    > 대부분의 문자열 작업은 슬라이싱으로 처리하는 편이 가장 빠르다.

```python
    s ='안녕하세요'
    s[:] # '안녕하세요' : 사본을 return
    s[1:4] # '녕하세' : 첫번째 인자는 포함, 두번쨰 인자는 불포함
    s[-3:] # '하세요' : 뒤에서 3번쨰 문자에서 마지막까지
    s[::1] # '안녕하세요' : 세번쨰 인자에서의 1은 기본값으로 동일하다.
    s[::-1] # '요세하녕안' : 뒤집는다.
    s[::2] # '안하요' : 2칸씩 앞으로 이동한다.
```
