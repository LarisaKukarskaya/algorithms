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

<details>
<summary>
<b>Хаотичность погоды (<a href="introduction/random_weather.py">random_weather.py</a>)</b>
</summary>
  
#### Условие
Метеорологическая служба вашего города решила исследовать погоду новым способом.
Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней, в которые температура строго больше, 
чем в день до (если такой существует) и в день после текущего (если такой существует).
Например, если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов,
то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.
Заметим, что если число показаний n=1, то единственный день будет хаотичным.
  
#### Формат ввода
В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105. 
Во второй строке даны n целых чисел –— значения температуры в каждый из n дней.
Значения температуры не превосходят 273 по модулю.

#### Формат вывода
Выведите единственное число — хаотичность за данный период.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      7<br>
      -1 -10 -8 0 2 0 5<br>
    </td>
    <td valign='top'>
      3<br>
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
      5<br>
      1 2 5 4 8<br>
    </td>
    <td valign='top'>
      2<br>
    </td>
  </tr>    
</tbody></table>

</details>

------

<details>
<summary>
<b>Самое длинное слово (<a href="introduction/longest_word.py">longest_word.py</a>)</b>
</summary>
  
#### Условие
Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному менеджменту.
Так как Гоша хочет спланировать день заранее, ему необходимо оценить сложность статьи.
Он придумал такой метод оценки: берётся случайное предложение из текста и в нём ищется самое длинное слово.
Его длина и будет условной сложностью статьи.
Помогите Гоше справиться с этой задачей.
  
#### Формат ввода
В первой строке дана длина текста L (1 ≤ L ≤ 105).
В следующей строке записан текст, состоящий из строчных латинских букв и пробелов.
Слово —– последовательность букв, не разделённых пробелами. 
Пробелы могут стоять в самом начале строки и в самом её конце.
Текст заканчивается переносом строки, этот символ не включается в число остальных L символов.

#### Формат вывода
В первой строке выведите самое длинное слово. Во второй строке выведите его длину.
Если подходящих слов несколько, выведите то, которое встречается раньше.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      19<br>
      i love segment tree<br>
    </td>
    <td valign='top'>
      segment<br>
      7<br>
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
      21<br>
      frog jumps from river<br>
    </td>
    <td valign='top'>
      jumps<br>
      5<br>
    </td>
  </tr>    
</tbody></table>

</details>

------

<details>
<summary>
<b>Палиндром (<a href="introduction/palindrom.py">palindrom.py</a>)</b>
</summary>
  
#### Условие
Помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.
  
#### Формат ввода
В единственной строке записана фраза или слово.
Буквы могут быть только латинские. Длина текста не превосходит 20000 символов.
Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.

#### Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      A man, a plan, a canal: Panama<br>
    </td>
    <td valign='top'>
      True<br>
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
      zo<br>
    </td>
    <td valign='top'>
      False<br>
    </td>
  </tr>    
</tbody></table>

</details>

------

<details>
<summary>
<b>Двоичная система (<a href="introduction/binary_system.py">binary_system.py</a>)</b>
</summary>
  
#### Условие
Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя.
Помогите Гоше решить задачу.
Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.
  
#### Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке.
Длина каждого числа не превосходит 10 000 символов.

#### Формат вывода
Одно число в двоичной системе счисления.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      1010<br>
      1011<br>
    </td>
    <td valign='top'>
      10101<br>
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
    </td>
    <td valign='top'>
      10<br>
    </td>
  </tr>    
</tbody></table>

</details>

------

<details>
<summary>
<b>Степень четырех (<a href="introduction/degree_of_four.py">degree_of_four.py</a>)</b>
</summary>
  
#### Условие
Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.
Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое неотрицательное число.
  
#### Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.

#### Формат вывода
Выведите «True», если число является степенью четырёх, «False» –— в обратном случае.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      15<br>
    </td>
    <td valign='top'>
      False<br>
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
      16<br>
    </td>
    <td valign='top'>
      True<br>
    </td>
  </tr>    
</tbody></table>

</details>

------

<details>
<summary>
<b>Ближайший ноль (<a href="introduction/nearest_zero.py">nearest_zero.py</a>)</b>
</summary>
  
#### Условие
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.
Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка.
Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.
Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. 
Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены.
Пустые участки обозначены нулями.
  
#### Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106).
В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули).
Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 109.

#### Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      5<br>
      0 1 4 9 0 0<br>
    </td>
    <td valign='top'>
     0 1 2 1 0<br>
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
      6<br>
      0 7 9 4 8 20<br>
    </td>
    <td valign='top'>
      0 1 2 3 4 5<br>
    </td>
  </tr>    
</tbody></table>

</details>

------

<details>
<summary>
<b>Ловкость рук (<a href="introduction/sleight_of_hands.py">sleight_of_hands.py</a>)</b>
</summary>
  
#### Условие
«Тренажёр для скоростной печати» представляет собой квадратную клавиатуру из шестнадцати клавиш размером 4x4.
На каждой клавише может быть изображена либо точка, либо цифра от 1 до 9.
Занятие на тренажёре делится на раунды :
каждый раунд состоит из нескольких игр;
в разных раундах число игр может быть разным;
номер каждой игры в раунде обозначается счётчиком t.
Для каждого раунда на клавишах устанавливаются определённые значения, которые остаются неизменными в течение всех игр раунда.
Значение счётчика игр t не может превысить значение самого большого числа, отображённого на клавиатуре в текущем раунде.
В упражнении на тренажёре принимают участие два игрока, они играют вдвоём на одной клавиатуре.
Для каждого раунда устанавливается максимальное число клавиш, которые может нажать один игрок (оно обозначается переменной k и не изменяется в течение раунда).
В каждой отдельной игре участники должны вместе нажать на клавиши, на которых изображена цифра, соответствующая номеру игры t.
Например, во второй игре раунда игроки должны нажать все те клавиши, на которых изображена двойка.
В раунде могут быть игры, где не требуется нажимать кнопки: например, в приведённом варианте раунда в играх от t = 4 до t = 8 кнопки нажимать не потребуется: на клавиатуре нет цифр от 4 до 8.
Если в очередной игре у участников есть возможность нажать все необходимые клавиши — они их нажимают и получают 1 балл.
Предположим, что для раунда задан набор кнопок, как на картинке, и k = 3 (каждый из участников может нажать не более трёх кнопок).
Тогда во второй игре (t = 2), где должны быть нажаты двойки, игроки вдвоём смогут нажать только 6 клавиш (k * 2 = 6). 
Но на клавиатуре семь двоек; участники не смогут нажать их все и не получат балл.

Напишите программу, которая будет принимать данные для определённого раунда:
значение k, значения для кнопок и вычислит количество баллов, которое будут заработано в этом раунде.
  
#### Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках заданы значения для кнопок –— по 4 символа в каждой строке. Каждый символ —– либо точка, либо цифра от 1 до 9.
Символы одной строки идут подряд и не разделены пробелами.

#### Формат вывода
Выведите единственное число –— количество баллов, которое игроки наберут в раунде.
  
#### Пример 1
<table><tbody>
  <tr>
  <td><b>Ввод</b></td>
  <td><b>Вывод</b></td>  
  </tr>
  <tr>
    <td valign='top'>
      3<br>
      1231<br>
      2..2<br>
      2..2<br>
      2..2<br>
    </td>
    <td valign='top'>
     2<br>
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
      1111<br>
      9999<br>
      1111<br>
      9911<br>
    </td>
    <td valign='top'>
      1<br>
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
      4<br>
      1111<br>
      1111<br>
      1111<br>
      1111<br>
    </td>
    <td valign='top'>
      0<br>
    </td>
  </tr>    
</tbody></table>

</details>

------

## 2. Основные структуры данных

[contest.yandex.ru](https://contest.yandex.ru/contest/23758/problems/)

---

<details>
<summary>
<b>Список дел (<a href="basic_data_structures/business_list.py">business_list.py</a>)</b>
</summary>
  
#### Условие
Васе нужно распечатать свой список дел на сегодня. Помогите ему: напишите функцию, которая печатает все его дела. Известно, что дел у Васи не больше 5000.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову списка и печатает его элементы.
Ниже дано описание структуры, которая задаёт узел списка.
Используйте заготовки кода для данной задачи, расположенные по ссылкам:
c++
Java
js
Python
C#
go
Решение надо отправлять только в виде файла с расширением, которое соответствует вашему языку. Иначе даже корректно написанное решение не пройдет тесты.
  
#### Формат ввода
В качестве ответа сдайте только код функции, которая печатает элементы списка. Длина списка не превосходит 5000 элементов. Список не бывает пустым.
Следуйте следующим правилам при отправке решений:
- По умолчанию выбран компилятор Make, выбор компилятора в данной задаче недоступен.
- Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования.
- Для Java файл должен называться Solution.java, для C# – Solution.cs
- Для остальных языков программирования это имя использовать нельзя (имя «solution» тоже).
- Для Go укажите package main.

#### Формат вывода
Функция должна напечатать элементы списка по одному в строке.
  
</details>

------

<details>
<summary>
<b>Нелюбимое дело (<a href="basic_data_structures/unloved_business.py">unloved_business.py</a>)</b>
</summary>
  
#### Условие
Вася размышляет, что ему можно не делать из того списка дел, который он составил. Но, кажется, все пункты очень важные! Вася решает загадать число и удалить дело, которое идёт под этим номером. Список дел представлен в виде односвязного списка. Напишите функцию solution, которая принимает на вход голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову списка и номер удаляемого элемента и возвращает голову обновлённого списка.
Используйте заготовки кода для данной задачи, расположенные по ссылкам:
c++
Java
js
Python
C#
go
Решение надо отправлять только в виде файла с расширением, которое соответствует вашему языку. Иначе даже корректно написанное решение не пройдет тесты.
  
#### Формат ввода
Функция принимает голову списка и индекс элемента, который надо удалить (нумерация с нуля). Список содержит не более 5000 элементов. Список не бывает пустым.
Следуйте следующим правилам при отправке решений:
- По умолчанию выбран компилятор Make, выбор компилятора в данной задаче недоступен.
- Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования.
- Для Java файл должен называться Solution.java, для C# – Solution.cs
- Для остальных языков программирования это имя использовать нельзя (имя «solution» тоже).
- Для Go укажите package main.

#### Формат вывода
Верните голову списка, в котором удален нужный элемент.
  
</details>

------
