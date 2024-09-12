# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# # Create your models here.
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Поле Email должно быть заполнено.')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(email, password, **extra_fields)
#
# class User(AbstractUser):
#     name = models.CharField('Имя', max_length=20)
#     avatar = models.ImageField('Фото', upload_to='avatars/', null=True)
#     phone = models.CharField('Номер телефона', max_length=15, null=False)
#     GENDER = (
#         ('Мужчина', 'Мужчина'),
#         ('Женщина', 'Женщина')
#     )
#     gender_choices = models.Choices(GENDER, default='Мужчина')
#     favorites = models.ManyToManyField('Избранное', on_delete=models.CASCADE)
#     favorite_brands = models.ManyToManyField('Любимые бренды', on_delete=models.CASCADE)
#
#     objects = UserManager()
#
# class Shippings(models.Model):
#     title = models.CharField('Название', max_length=50)
#     price = models.CharField('Цена', max_length=30)
#     delivery_time = models.DateTimeField('Срок доставки', auto_now_add=True)
#     date_placement = models.DateTimeField('Дата оформления', auto_now_add=True)
#
# class Payment(models.Model):
#     cart = models.CharField('Банковская карта', max_length=50)
#
# class Discounts(models.Model):
#     discount = models.IntegerField('Скидка', max_length=10)
#
# class CartItem(models.Model):
#     def __init__(self, product_id, name, price, quantity=1):
#         self.product_id = product_id
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def update_quantity(self, quantity):
#         self.quantity = quantity
#
#     def total_price(self):
#         return self.price * self.quantity
#
#
# class Cart(models.Model):
#     def __init__(self):
#         self.items = {}
#
#     def add_item(self, product_id, name, price, quantity=1):
#         if product_id in self.items:
#             self.items[product_id].update_quantity(self.items[product_id].quantity + quantity)
#         else:
#             self.items[product_id] = CartItem(product_id, name, price, quantity)
#
#     def remove_item(self, product_id):
#         if product_id in self.items:
#             del self.items[product_id]
#         else:
#             print("Товар не найден в корзине.")
#
#     def update_item_quantity(self, product_id, quantity):
#         if product_id in self.items:
#             self.items[product_id].update_quantity(quantity)
#             if self.items[product_id].quantity <= 0:
#                 self.remove_item(product_id)
#         else:
#             print("Товар не найден в корзине.")
#
#     def get_total_quantity(self):
#         return sum(item.quantity for item in self.items.values())
#
#     def get_total_price(self):
#         return sum(item.total_price() for item in self.items.values())
#
#     def list_items(self):
#         return [(item.product_id, item.name, item.price, item.quantity) for item in self.items.values()]
#
#     def __str__(self):
#         items_str = "\n".join([f"{item.product_id}: {item.name}, ${item.price:.2f} x {item.quantity}" for item in self.items.values()])
#         return f"Cart:\n{items_str}\nTotal Quantity: {self.get_total_quantity()}\nTotal Price: ${self.get_total_price():.2f}"
#
#
