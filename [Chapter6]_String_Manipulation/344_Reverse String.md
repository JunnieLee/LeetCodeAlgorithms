# 🧚‍♀️ [풀이 1] : 투 포인터를 이용한 스왑

## 설명

-   투 포인터를 이용한 전통적인 방법
-   투 포인터 풀이 방식 = 단어 그대로 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식.
-   여기서는 점점 더 범위를 좁혀가며 스왑하는 형태로 풀이할 수 있음.

## 최종 코드

```python
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
```

# 🧚 [풀이 2] : 파이썬다운 방식

## 설명

입력값이 리스트로 제공되므로 다음과 같이 reverse() 함수를 사용하면 뒤집을 수 있다.

```python
    s.reverse()
```

-   reverse()는 리스트에만 제공된다.
-   만약 입력값이 문자열이라면 아래와 같이 문자열 슬라이싱을 사용할 수 있다.
    슬라이싱은 리스트에도 사용할 수 있으며, 성능또한 매우 좋다.

```python
    s = s[::-1]
```

하지만 이 문제는 in-place로 풀어야 하므로 슬라이싱으로 풀 수 없다.

## 최종 코드

```python
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
```
