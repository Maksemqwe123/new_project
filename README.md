Первым делом я создал парсер, который парсил сайт погоды.
Потом создал файл где хранится логика кнопки и создал файл конфига.
И создал файл бота, и теперь начались появлятся трудности.
первая трудность возникла в том что нужно было как то передать парсер, в файл конфига, и чтобы благодаря вызова кнопки по ключю, передовалась инфа ключа конфига, а значение парсера.
я пытался сделать импорт класса парсера, и как то передать значение в конфига.
но так как у меня этого не вышло, я принял решение объединить файл бота и файл парсера, в следствии мне не понадобился файл конфига и файл парсера, теперь я только использовал bot_main и buttons.
Оригинналы можно посмотреть в users_data, config, buttons, parser_weather.
Работающий файл это  bot_main, buttons.
И что то даже наверное начало работать, но трудности не закончились во первых я не мог вывести прогноз на сегодня, выводился прогноз на вчера и на сегодня.
И ещё одна трудность заключается в том что я немогу сделать обработчик if, температуру не могу приравнять к значению, if temp_1 < -10: Print(оставайся дома)
