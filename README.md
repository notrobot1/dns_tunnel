# dns_tunnel
dnscheck.py - отправка dns запроса на 8.8.8.8, получаем ответ. Отправляем "AA AA 01 00 00 01 00 00 00 00 00 00 " + "07 65 78 61 6d 70 6c 65 03 63 6f 6d" +" 00 00 01 00 01". Здесь 65 78 61 6d 70 6c 65 03 63 6f 6d - ссылка example.com.

dns-server.py - установить на виртуальный сервер. Программа запускается на 53 порту и принимает DNS запросы, выцепляет из запроса ссылку (в нашем примере - "https://docs.python.org/3/library/ssl.html" ) и отправляет GET запрос по данному адресу. Получает html код страницы и отправляет обратно клиенту. 
dns-client.py - запускаю на телефоне через термукс, программа отправляет DNS запрос, вместо доменного имени передает полный путь на сайт (с https://). Ждет ответа и выводит html код страницы в терминал. 

Есть много багов, требует доработки!
 
