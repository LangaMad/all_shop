from enum import unique

from django.db import models

class TestCategory(models.Model):
    name = models.CharField('Название категории', max_length=40)
    slug = models.SlugField('Cлаг', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class TestProduct(models.Model):
    name = models.CharField('Название товара', max_length=200)
    is_active = models.PositiveIntegerField('Активный', unique=True)
    articul = models.PositiveIntegerField('Артикул', unique=True, null=True, blank=True)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, related_name='products',
                                 null=True, blank=True)
    price = models.PositiveIntegerField('Цена', null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='products', null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)

class Brand(models.Model):
    name = models.CharField('Название бренда', max_length=100)
    slug = models.SlugField('Cлаг', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class Car(models.Model):
    name = models.CharField('Название машины', max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    color = models.CharField('Цвет машины', max_length=100)
    engine_type = models.CharField('Тип двигателя', max_length=100)
    drivers_location = models.CharField('Расположение водительского кресла', max_length=100)
    drive_type = models.CharField('Тип привода', max_length=100)
    volume = models.DecimalField('Объем', max_digits=4, decimal_places=2)
    year_manufacture = models.CharField('Год выпуска', max_length=100)
    body = models.CharField('Кузов', max_length=100)
    Country_origin = models.CharField('Страна производства', max_length=200)



#
# class Category(models.Model):
#     name = models.CharField('Название категории', max_length=100)
#     slug = models.SlugField('Cлаг', max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
# class Subcategory(models.Model):
#     name = models.CharField('Название подкатегории', max_length=100)
#     slug = models.SlugField('Cлаг', max_length=100, unique=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Подкатегория'
#         verbose_name_plural = 'Подкатегории'
#
# class Subsubcategory(models.Model):
#     name = models.CharField('Название подподкатегории', max_length=100)
#     slug = models.SlugField('Cлаг', max_length=100, unique=True)
#     category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subsubcategory')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Подподкатегория'
#         verbose_name_plural = 'Подподкатегории'
#
# class Size(models.Model):
#     size_name = models.CharField('Размер', max_length=20)
#
#     def __str__(self):
#         return self.size_name
#
# class Product(models.Model):
#     name = models.CharField('Название товара', max_length=200)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
#     subsubcategory = models.ForeignKey(Subsubcategory, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
#     sizes = models.ManyToManyField(Size, related_name='products')
#     articul = models.PositiveIntegerField(unique=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField('Изображение', upload_to='products')
#     description = models.TextField('Описание')
#     color = models.CharField('Цвет', max_length=100)
#     compound = models.CharField('Состав', max_length=200, null=True, blank=True)
#     season = models.CharField('Сезон', max_length=200, null=True, blank=True)
#     shoe_sole_material = models.CharField('Материал подошвы обуви', max_length=200, null=True, blank=True)
#     shoe_lining_material = models.CharField('Материал подкладки обуви', max_length=200, null=True, blank=True)
#     insole_material = models.CharField('Материал стельки', max_length=200, null=True, blank=True)
#     sole_height = models.CharField('Высота подошвы', max_length=200, null=True, blank=True)
#     country_of_origin = models.CharField('Страна производства', max_length=200, null=True, blank=True)
#     equipment = models.CharField('Комплектация', max_length=200, null=True, blank=True)
#     clasp_type = models.CharField('Вид застежки', max_length=200, null=True, blank=True)
#     model_features = models.CharField('Особенности модели', max_length=200, null=True, blank=True)
#     product_model = models.CharField('Модель', max_length=200, null=True, blank=True)
#     warranty_period = models.CharField('Гарантийный срок', max_length=200, null=True, blank=True)
#     nutrition = models.CharField('Питание', max_length=200, null=True, blank=True)
#     wireless_interfaces = models.CharField('Беспроводные интерфейсы', max_length=200, null=True, blank=True)
#     effect = models.CharField('Эффект средства', max_length=200, null=True, blank=True)
#     item_width = models.CharField('Ширина предмета', max_length=200, null=True, blank=True)
#     item_height = models.CharField('Высота предмета', max_length=200, null=True, blank=True)
#     quantity_package = models.CharField('Количество в упаковке', max_length=200, null=True, blank=True)
#     housing_material = models.CharField('Материал корпуса', max_length=200, null=True, blank=True)
#     handle_type = models.CharField('Тип ручки', max_length=200, null=True, blank=True)
#     number_branches = models.CharField('Количество отделений', max_length=200, null=True, blank=True)
#     backpack_size = models.CharField('Размер рюкзака', max_length=200, null=True, blank=True)
#     lining_material = models.CharField('Материал прокладки', max_length=200, null=True, blank=True)
#     backpack_capacity = models.CharField('Вместимость рюкзака', max_length=200, null=True, blank=True)
#     pockets = models.CharField('Карманы', max_length=200, null=True, blank=True)
#     product_material = models.CharField('Материал изделия', max_length=200, null=True, blank=True)
#     max_load = models.CharField('Максимальная нагрузка', max_length=200, null=True, blank=True)
#     mounting_type = models.CharField('Тип крепления', max_length=200, null=True, blank=True)
#     package_length = models.CharField('Длина упаковки', max_length=200, null=True, blank=True)
#     package_height = models.CharField('Высота упаковки', max_length=200, null=True, blank=True)
#     package_width = models.CharField('Ширина упаковки', max_length=200, null=True, blank=True)
#     battery_capacity = models.CharField('Ёмкость аккумулятора', max_length=200, null=True, blank=True)
#     battery_life = models.CharField('Время работы от аккумулятора', max_length=200, null=True, blank=True)
#     screen_size = models.CharField('Размер экрана', max_length=200, null=True, blank=True)
#     resolution = models.CharField('Разрешение экрана', max_length=200, null=True, blank=True)
#     connectivity = models.CharField('Подключение', max_length=200, null=True, blank=True)
#     storage_capacity = models.CharField('Ёмкость памяти', max_length=200, null=True, blank=True)
#     operating_system = models.CharField('Операционная система', max_length=200, null=True, blank=True)
#     processor_type = models.CharField('Тип процессора', max_length=200, null=True, blank=True)
#     weight = models.CharField('Вес', max_length=200, null=True, blank=True)
#     color_variants = models.CharField('Варианты цвета', max_length=200, null=True, blank=True)
#     size_variants = models.CharField('Варианты размера', max_length=200, null=True, blank=True)
#     environmental_rating = models.CharField('Экологический рейтинг', max_length=200, null=True, blank=True)
#     energy_rating = models.CharField('Энергетический рейтинг', max_length=200, null=True, blank=True)
#     compatibility = models.CharField('Совместимость', max_length=200, null=True, blank=True)
#     expiry_date = models.DateField('Срок годности', null=True, blank=True)
#     release_date = models.DateField('Дата выпуска', null=True, blank=True)
#     usage_area = models.CharField('Область применения', max_length=200, null=True, blank=True)
#     safety_warnings = models.TextField('Предупреждения о безопасности', null=True, blank=True)
#     price_range = models.CharField('Ценовой диапазон', max_length=200, null=True, blank=True)
#     model_year = models.CharField('Год модели', max_length=200, null=True, blank=True)
#     seasonal_offer = models.CharField('Сезонное предложение', max_length=200, null=True, blank=True)
#     production_batch = models.CharField('Партийный номер', max_length=200, null=True, blank=True)
#     import_status = models.CharField('Статус импорта', max_length=200, null=True, blank=True)
#     shelf_life = models.CharField('Срок хранения', max_length=200, null=True, blank=True)
#     certification_marks = models.CharField('Сертификационные знаки', max_length=200, null=True, blank=True)
#     eco_friendly = models.CharField('Экологически чистый', max_length=200, null=True, blank=True)
#     manufacturer_name = models.CharField('Имя производителя', max_length=200, null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Товар'
#         verbose_name_plural = 'Товары'
#
#
#
