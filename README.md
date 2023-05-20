# Tenzor_calculator
Калькулятор для тензоров:
- Перемножение
- Переход в новый базиз 
- Альтернирование 
- Симметрирование

---

### **!! ВНИМАНИЕ !!** 
**Программа является полностью консольным приложение и может выполнятся ТОЛЬКО В консоли!**

**_Данный код является временным - его оптимизация, эстетичность и логичность не являлись первостепенной задачей!
На данный момент выстраивается только функционал и архитектура программы, удобство и практичность будут добавлены после всех необходимых действий!
Это только пробная версия - файлы и код в них могут и будут впоследствии изменены для более практичного и универсального использования!_**

----

## ***Инструкция***

1) Запускаете через консоли программу ```python Calculator_of_Tensor.py``` или ```python3 Calculator_of_Tensor.py```
2) Выбираете нужное действие
3) Дальше действуете по инструкции в консоли

---

### Дополнения и возможные ошибки ввода

1. Матрицы необходимо вписывать по строкам для каждого слоя!
2. При перемножении перед вводом тензора обращайте внимание на комментарий сверху!
3. При изменении программы **НЕ МЕНЯЙТЕ ИНДЕКСЫ**, _они были выверены и тщательно проверены_!
4. Возможные ошибки:
    - В поле размерности указано последовательность чисел или иные значения
    - Введённый тензор не совпадает с заданной размерностью
    - При задании старого и нового базисов матрицы оказались вырожденными (базисные вектора _линейно зависимы_)
    - В **альтернировании и симметрировании** индексы заданы не по порядку, через пробел или указаны неверные индексы (_отличные от **ijk**_)
    - Другие ошибки ещё не были найдены или сочлись малозначимыми или редкими.

---

#### Начальный экран программы
![Начальный экран](https://github.com/Yaroslem15/Tenzor_calculator/assets/110384995/d3ca8b97-dbeb-4f5d-9b37-4ba5a5acbe01)
