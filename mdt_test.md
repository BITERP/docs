# Преамбула
## Что проверяем?

1. Соответствие кода стандартам разработки 1С
2. Навыки встраивания в типовые конфигурации фирмы 1С (ERP/КА/УТ11)
3. Соответствие кода требованиям, предъявляемым к тиражному продукту (читаемость, сопровождаемость, масштабируемость, расширяемость и т.п.)

## Зачем?
Решение задание позволит вам ознакомиться с примером реальной задачи, а также получить обратную связь, и понять наши требования до выхода на работу.

## Ожидания по трудоемкости
Кроме отличий в качестве кода, которые сложно точно количественно измерить, трудоемкость выполнения задания для разработчиков разных уровней отличается:

1. Для архитектора (верхняя граница зарплатной вилки - 300+ тыс. руб.): до 4 часов
2. Для старшего разработчика (нижняя граница зарплатной вилки - 200+ тыс. руб.): до 12 часов
3. Для разработчика (ниже 200 тыс. руб.): до 20 часов
4. Кандидаты, у которых трудоемкость выполнения работ составит более 20 часов в продуктовую команду БИТ.MDT на позицию разработчика не рассматриваются.

# Требования к выполнению

1. Задание нужно выполнить на типовой ЕРП2.5 последней стабильной версии. Конфигурацию не снимать с поддержки. Все доработки выполнить в расширении.
2. Показывать на демо-базе, входящей в комплект поставки.
3. Код должен быть написан исходя из следующих соображений:
3.1. это часть тиражного продукта, с открытым исходным кодом, который может дорабатываться на внедрениях сторонними командами
3.2. тиражный продукт обновляется вслед за выходом новых релизов 1С
3.3. код должен соответствовать стандартам разработки 1С
3.4. код должен быть рассчитан на работу при высоких нагрузках (десятки тысяч марок в одном документе, десятки миллионов марок в справочнике)
3.5. код должен написан таким образом, чтобы корректно отрабатывать во всех ситуациях (т.е. проведение/распроведение/редактирование в том числе изменение даты документов, изменение их порядка, и т.п.)
4. Необходимо будет расшарить экран и показать код, а также работу в режиме исполнения
5. Мы никак не контролируем время, которое у Вас занимает выполнение задачи: после выхода на работу данные о скорости вашей разработки будут использоваться в качестве референсного значения. Скорость разработки (как и качество) влияют не только на уровень оплаты труда, но и на объем и сложность задач, выполнение которых от вас ожидается в конкретный срок.

# Контекст

1. Заказчик (группа компаний ШинПромТоргИнвест) есть несколько юридических лиц. 
2. Основной бизнес заказчика - торговля шинами (и сопутствующей продукции). 
3. Все юридические лица ведут учет в одной базе 1С:ERP 2. 
4. Между юридическими лицами есть операции купли-продажи, но схему интеркампани не используют (т.е. оформляют зеркальные документы продажи и покупки). 
5. Товары разных юридических лиц хранятся на одном и том же складе.
6. На складах используются ТСД.
7. На ТСД организована выгрузка элементов справочника Штрихкоды упаковок товаров, при отгрузке на ТСД осуществляется проверка наличия считанного штрихкода в этом справочнике.

# Прикладная задача
Иногда на складе возникает ситуация, когда в отгрузку подбирают марки, принадлежащие другой организации (отличной от той, которая указана в документе отгрузки). Необходимо исключить данную ситуацию, выводя сообщение пользователю, объясняя запрет подбора конкретной шины в документ.

# Ограничения тестовой задачи

1. Рассматриваем только два документа, которые меняют владельца (остальные документы игнорируем):
   
   
   1. Маркировка товаров ИС МП
   1. Приобретение товаров и услуг
1. Стандартный процесс (без отклонений) выглядит следующим образом (все операции в одной базе но между разными организациями):
   
   
   1. Производитель шин производит шины и вводит марки в оборот маркировкой товаров (Маркировка товаров)
   1. Торговый дом1 покупает шины у производителя для дальнейшей реализации (Приобретение товаров и услуг)
   1. Торговый дом2 покупает шины у Торговый дом1 для дальнейшей реализации (Приобретение товаров и услуг)
1. Допускаются многочисленные внутренние купли-продажи, а также изменение документов задним числом. При этом владелец марки должен оставаться всегда корректным.
1. Доработки мобильного приложения (и обмена с мобильным приложением) не входят в рамки данной задачи

# Задача на разработку

1. Добавить реквизит Владелец марки в справочник Штрихкоды упаковок товаров. Нам нужна актуальная информация о владельце именно в справочнике, поскольку справочник синхронизируется с ТСД, где потребуется реализовать проверку (реализация функционала на ТСД не входит в данную задачу)
1. При работе пользователей с документами, при проведении документа определять у каких марок нужно изменить владельца и выполнить данные изменения.

# Дополнительно
Если вы затрудняетесь показать код своих доработок типовой ERP2/КА2/УТ11 по любым причинам, то просим вас дополнительно реализовать ввод на основании РТиУ зеркального документа. Т.е. предполагаем, что заказчик не хочет использовать схему интеркампани (будет хорошо, если вы на собеседовании сможете назвать возможные причины), но хочет чтобы одной базе работало два его юр. лица, и для того, чтобы исключить двойной ввод информации, а также для автоматического контроля сходимости данных необходимо реализовать ввод на основании.