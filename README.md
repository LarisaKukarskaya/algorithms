# Базовые алгоритмы

Решение задач по алгоритмам на языке Python

---

## 1. Введение в алгоритмы

[contest.yandex.ru](https://contest.yandex.ru/contest/23389/problems/)

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
  
#### Условие
Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
Измерения велись n секунд.
В секунду i поступает qi запросов.
Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат. 
  
#### Формат ввода
В первой строке передаётся натуральное число n, количество секунд, в течение которых велись измерения. 1 ≤ n ≤ 105
Во второй строке через пробел записаны n целых неотрицательных чисел qi, каждое лежит в диапазоне от 0 до 103.
В третьей строке записано натуральное число k (1 ≤ k ≤ n) – окно сглаживания.
Примечание для Go:
Заметьте, что в данной задаче достаточно большой размер ввода. Поэтому необходимо задавать размер буфера для сканнера хотя бы 600 Кб.

#### Формат вывода
Выведите через пробел результат применения метода скользящего среднего к серии измерений.
Должно быть выведено n - k + 1 элементов, каждый элемент — вещественное (дробное) число.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      7<br>
      1 2 3 4 5 6 7<br>
      4<br>      
    </td>
    <td valign='top'>
      2.5 3.5 4.5 5.5<br>
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
      9<br>
      9 3 2 0 1 5 1 0 0<br>
      3<br>
    </td>
    <td valign='top'>
      4.6666666667 1.666666667 1 2 2.333333335 2 0.3333333<br>
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
      5<br>
      1 2 3 4 5<br>
      5<br>
    </td>
    <td valign='top'>
      3<br>
    </td>
  </tr>
</tbody></table>

</details>

------

<details>
<summary>
<b>Две фишки (<a href="introduction/two_chips.py">two_chips.py</a>)</b>
</summary>
  
#### Условие
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.
  
#### Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 104.
Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне от -105 до 105.
В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

#### Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
Если таких пар несколько, то можно вывести любую из них.
Если таких пар не существует, то вывести «None».
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      6<br>
      -1 -1 -9 -7 3 -6<br>
      2<br>      
    </td>
    <td valign='top'>
      -1 3<br>
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
      8<br>
      6 2 8 -3 1 1 6 10<br>
      100<br>
    </td>
    <td valign='top'>
      None<br>
    </td>
  </tr>    
</tbody></table>

</details>

------

<details>
<summary>
<b>Соседи (<a href="introduction/neighbours.py">neighbours.py</a>)</b>
</summary>
  
#### Условие
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.
Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.
  
#### Формат ввода
В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m.
Числа m и n не превосходят 1000. В следующих n строках задана матрица.
Элементы матрицы — целые числа, по модулю не превосходящие 1000.
В последних двух строках записаны координаты элемента, соседей которого нужно найти.
Индексация начинается с нуля.

#### Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      4<br>
      3<br>
      1 2 3<br>
      0 2 6<br>
      7 4 1<br>
      2 7 0<br>
      3<br>
      0<br>
    </td>
    <td valign='top'>
      7 7<br>
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
      4<br>
      3<br>
      1 2 3<br>
      0 2 6<br>
      7 4 1<br>
      2 7 0<br>
      0<br>
      0<br>
    </td>
    <td valign='top'>
      0 2<br>
    </td>
  </tr>    
</tbody></table>

</details>

------
