## JSON API
Этот проект - решение к [тестовому заданию](https://github.com/avito-tech/verticals/blob/master/trainee/backend.md)

Запустить проект можно используя `docker-compose`. Для этого нужно:
```
cd ads_api
docker-compose up
```

### Получение списка объявлений
Получить список объявлений можно отправив GET запрос на `/ads`
Для сортировки используется параметр `ordering`.
```
/ads?ordering=created_at    # сортировка по дате создания (по убыванию -created_at)
/ads?ordering=price         # сортировка по стоимости (по убыванию -price)
```

### Получение одного объявления
```
/ads/12
```
Для дополнительных полей нужно передать параметр `fields`
```
/ads/12?fields=description,photos   # получаем доп. поля описания и всех фотографий
```

### Создание объявления
Создать объявление можно отправив POST запрос на `/ads`
Формат JSON:
```
{
    "title": "title",
    "description": "description",
    "price": 23.00,
    "photos": [
		{    	
    		"url": "6.jpg"
		},
		{    	
    		"url": "4.jpg"
		},
		{    	
    		"url": "10.jpg"
		}
    ]
}
```
