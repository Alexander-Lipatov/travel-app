const form = document.getElementById('myForm');
const coordsField = document.getElementById('id_coords')
const addressField = document.getElementById('id_address')
const imageMapField = document.getElementById('id_image_screen_url')


// Функция ymaps.ready() будет вызвана, когда
// загрузятся все компоненты API, а также когда будет готово DOM-дерево.
ymaps.ready(init);
function init() {

    // Создание карты.
    const myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 7,
        controls: ['searchControl']
    });

    // Создание поискового контрола
    searchControl = myMap.controls.get('searchControl');

    // Добавление или обновление отметки на карту при клике
    let placemark = null;

    myMap.events.add('click', function (e) {
        const coords = e.get('coords');

        // Удаление предыдущей метки, если она есть
        if (placemark) {
            myMap.geoObjects.remove(placemark);
        }

        placemark = new ymaps.Placemark(coords);
        myMap.geoObjects.add(placemark);

        // Геокодирование координат для получения адреса
        ymaps.geocode(coords).then(function (res) {
            const firstGeoObject = res.geoObjects.get(0);

            // Адрес местоположения
            const address = firstGeoObject.getAddressLine();
            // Создание ссылки для скачивания картинки с указанным местоположением
            const staticImageUrl = `https://static-maps.yandex.ru/1.x/?ll=${coords[1]},${coords[0]}&spn=0.005,0.005&size=410,225&l=map`
            
            // Меняем значения в полях формы 
            addressField.value = address
            coordsField.value = coords
            imageMapField.value = staticImageUrl
        
        });
    });

    

    // Добавление обработчика события resultselect на поисковый контрол
    searchControl.events.add('resultselect', function (e) {

        // Получение выбранного результата
        const selectedResult = searchControl.getResultsArray()[e.get('index')];
        
        // Получение координат из выбранного результата
        const coords = selectedResult.geometry.getCoordinates();

        // Удаление предыдущей метки, если она есть
        if (placemark) {
            myMap.geoObjects.remove(placemark);
        }

        placemark = new ymaps.Placemark(coords);
        myMap.geoObjects.add(placemark);

        // Геокодирование координат для получения адреса
        ymaps.geocode(coords).then(function (res) {
            const firstGeoObject = res.geoObjects.get(0);

            const address = firstGeoObject.getAddressLine();
            const staticImageUrl = `https://static-maps.yandex.ru/1.x/?ll=${coords[1]},${coords[0]}&spn=0.005,0.005&size=410,225&l=map`
            
            addressField.value = address;
            coordsField.value = coords;
            imageMapField.value = staticImageUrl;
        });
    });

    




}
