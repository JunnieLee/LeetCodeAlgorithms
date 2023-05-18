> 요구조건을 얼마나 깔끔하게 처리할 수 있는지를 묻는 문제.
> 실무에서도 이 같은 로직은 매우 자주 쓰이는 만큼 매우 실용적인 문제라고 볼 수 있다.

# [풀이 1] :람다와 + 연산자를 이용

## 설명

1. 일단 숫자부분의 경우 string에 들어가 있다 하더라도 isdigit()을 통해 실제 string안의 내용이 digit인지 아닌지 판별할 수 있음.

```python
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)
```

2. letters의 경우, 식별자를 제외한 문제열 [1:]을 키로 하여 정렬하며, 동일한 경우 후순위로 식별자 [0]을 지정해 정렬되도록, Lambda Expression을 이용해 정렬한다.

```python
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
```

3. letters 배열과 digits 배열을 합쳐준다.

```python
    return letters + digits
```

## 최종 코드

```python
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 2개의 key를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
```

## 관련 추가자료 by 교재

### 🧚‍♀️ 람다 표현식

-> 람다 표현식이란 식별자 없이 실행 가능한 함수를 말하며, 함수 선언 없이도 하나의 식으로 함수를 단순하게 표현할 수 있다.
만약 위의 코드에서 람다를 사용하지 않고 직접 함수를 선언한다면 다음과 같은 형태가 된다.

```python
    def func(x):
        return x.split()[1], x.split()[0]

    s.sort(key=func)
```

위 대신 람다 표현식을 사용하면, 별도 함수를 선언하지 않고도 간단한 함수를 선언한것처럼 쉽게 처리할 수 있다.

> 그러나 람다 표현식은 코드가 길어지고 map이나 filter와 함꼐 섞어서 사용하기 시작하면 가독성이 매우 떨어질 수 있으므로 주의가 필요하다.

## 관련 추가자료 by 나

### 🧚‍♂️ python array 정렬 : 특정 key 기준으로 정렬하기

#### (1) sorted()

```python
    sorted( <list> , key = <function> , reverse = <bool>)
    # <list> 뿐 아니라, <Tuple>, <Dictionary>, <Str>에도 사용 가능하다.
```

-   원본 내용을 바꾸지 않고, 정렬한 값을 반환한다.
-   List, tuple, Dictionary, str에 모두 사용 가능하다.
-   key 를 통하여 정렬할 기준을 정할 수 있다.
-   reverse 가 True이면 내림차순, False이면 오름차순으로 정렬된다.

#### (2) sort()

```python
    <list>.sort(key = <function>, reverse = <bool>)
```

-   원본 자체를 수정한다.
-   반환값은 None
-   Tuple , Dictionary, Str 에는 사용이 불가하다.

###### 1. 예시 1 : 2중 리스트에서 정렬하기

```python
    array = [[50, "apple"], [30, "banana"] , [400, "melon"]]
```

위와 같이 [Int, Str]형식의 요소를 가진 리스트가 존재할때
Int를 기준으로 정렬하려면...

-   .sort() 함수 사용

```python
    array.sort(key = lambda x:x[0])
    print(array)
    >>>>> [[30, 'banana'], [50, 'apple'], [400, 'melon']]
```

-   sorted() 함수 사용

```python
    print(sorted(array, key = lambda x: x[0]))
    >>>>> [[30, 'banana'], [50, 'apple'], [400, 'melon']]
```

###### 2. 예시 2 : key가 여러개일때 (다중조건 정렬)

```python
    array = [("A", 18, 300000) , ("F", 24, 10000), ("T", 24, 200000),("Q",24,5000000), ("B", 70, 5000)]
    # (<이름> , <나이> , <재산>) 이라고 하면
```

-   위의 리스트처럼 정렬해야 할때 고려해야 많은 경우가 있을때는 튜플형식으로 `key = lambda x: (x[0] , x[2])` lambda식을 세워주면 된다.
-   그리고 내림차순으로 하고 싶다면 마이너스 부호를 붙여주면 된다. key= lambda x: (-x[0], x[2])

나이를 기준으로 오름차순 정렬하고 , 같은 나이라면 재산을 내림차순으로 정렬한다 하면 아래와 같이 작성 가능.

```python
    array.sort(key = lambda (x: x[1], -x[2]))
    print(array)

    >>> [('A', 18, 300000), ('Q', 24, 5000000), ('T', 24, 200000), ('F', 24, 10000), ('B', 70, 5000)]
```

(참고 from: <https://infinitt.tistory.com/122>)
