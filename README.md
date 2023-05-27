# Базовые алгоритмы

Решение задач по алгоритмам на языке Python

---

## 1. Введение в алгоритмы

[contest.yandex.ru](https://contest.yandex.ru/contest/26365/problems/)

---

<details>
<summary>
<b>Застежка-молния (<a href="introduction/zipper.py">zipper.py</a>)</b>
</summary>
  
#### Условие
Даны два массива чисел длины n. Составьте из них один массив длины 2n,
в котором числа из входных массивов чередуются (первый — второй — первый — второй — ...).
При этом относительный порядок следования чисел из одного массива должен быть сохранён. 
  
#### Формат ввода
В первой строке записано целое число n –— длина каждого из массивов, 1 ≤ n ≤ 1000.
Во второй строке записано n чисел из первого массива, через пробел.
В третьей строке –— n чисел из второго массива.
Значения всех чисел –— натуральные и не превосходят 1000.

#### Формат вывода
Выведите 2n чисел из объединённого массива через пробел.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      3<br>
      1 2 3<br>
      4 5 6<br>      
    </td>
    <td valign='top'>
      1 4 2 5 3 6<br>
    </td>      
  </tr>
</tbody></table>
  
#### Пример 2
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      1<br>
      1<br>
      2<br>
    </td>
    <td valign='top'>
      1 2<br>
    </td>
  </tr>    
</tbody></table>
  
#### Пример 3
<table><tbody>
  <tr>
   <td><b>Ввод</b></td>
   <td><b>Вывод</b></td>    
  </tr>
  <tr>
    <td valign='top'>
      3<br>
      1 8 9<br>
      2 3 1<br>
    </td>
    <td valign='top'>
      1 2 8 3 9 1<br>
    </td>
  </tr>
</tbody></table>
  
</details>

------

<details>
  <summary>
  <b>Скользящее среднее (<a href="introduction/moving_average.py">moving_average.py</a>)</b>
  </summary>
</details>
